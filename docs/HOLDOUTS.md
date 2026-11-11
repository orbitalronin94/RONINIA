# Crónica de los holdouts — RONIN-10M

Este documento es la crónica narrativa y el registro técnico de las evaluaciones de RONIN-10M. Cada holdout tendrá su propio capítulo: qué checkpoint se examinó, qué comportamiento apareció, qué nos enseñó y qué preguntas deja abiertas. La narración no sustituye a las métricas; sirve para conservar el contexto de cada experimento.

Los enlaces de las ejecuciones y sus artefactos se mantienen en el índice histórico. Los artefactos pueden caducar según la política de GitHub Actions, por lo que conviene conservar también sus hashes y resultados esenciales.

## Prólogo — Antes de aprender

La evaluación de paso cero es el origen de esta serie: los pesos todavía no habían recibido un solo paso de entrenamiento. No es una prueba de inteligencia ni una competición. Es la fotografía del modelo recién inicializado, antes de que el corpus le preste sus palabras, sus hábitos y sus personajes.

El baseline utilizó las mismas 100 preguntas de inferencia, el mismo tokenizer de 8.192 tokens, la misma instrucción en castellano y generación greedy sin RAG. Su función es fijar el punto de partida. Pero hay una cautela experimental: el perfil de paso cero tenía contexto de 512 tokens y 9.831.168 parámetros, mientras que los checkpoints de 5k y 10k usaron contexto 256 y 9.757.440 parámetros. Comparten tokenizer, semilla, preguntas y límites de generación, pero no son una comparación arquitectónica perfectamente idéntica.

## Capítulo 0 — Antes de que aparezca la voz

**Checkpoint:** inicialización aleatoria, 0 pasos  
**Run de evaluación:** [42874585777](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777)  
**Artefacto:** [baseline de paso cero](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777/artifacts/13791466097)  
**SHA-256 del checkpoint:** `3c00d1ada5dc7399be90da3c39c9f503ef6f0799308b2d9c4373ee884ba814e8`  
**Holdout:** 100 preguntas  
**Latencia media:** 0,338 s por respuesta  
**Respuestas no vacías:** 100/100

Antes del sindicalista y antes del esperpento hubo una voz sin personaje. El modelo contestaba, pero sus salidas parecían restos de un idioma todavía sin organizar: fragmentos de tokens, palabras sueltas de varias lenguas, signos, fórmulas y secuencias sin una estructura estable. No había una muletilla dominante que permitiera reconocer una personalidad. Tampoco había una respuesta consistente a la pregunta.

El detalle importante es que el baseline no estaba en silencio: produjo cien respuestas no vacías. Pero que haya texto no significa que haya comunicación. La generación greedy encontraba siempre algún token siguiente; todavía no había aprendido a ordenar esos tokens en una respuesta castellana con intención reconocible.

En este primer retrato no aparece «El patrón», no aparece «ni puta idea» y tampoco aparece «impacto». Esas familias de expresiones llegarán después, cuando el entrenamiento empiece a moldear la distribución. El paso cero es, por tanto, el contraste entre producir secuencias y empezar a producir una voz.

### La fotografía técnica

La latencia media fue de aproximadamente 0,338 segundos por pregunta, superior a la observada en los checkpoints posteriores. No debe interpretarse como una medida de razonamiento: el baseline no estaba resolviendo más cosas ni haciendo una deliberación más profunda. Es una medición de inferencia bajo una configuración cuyo contexto era de 512 tokens, frente a los 256 de los ensayos posteriores.

El artefacto conserva el checkpoint inicial, la huella del tokenizer y el hash del conjunto de preguntas. La generación utilizó greedy argmax, dos hilos, hasta 32 tokens nuevos, máximo de 128 bytes, sin KV cache y sin RAG.

### Lo que enseña el punto cero

El baseline nos recuerda que el primer objetivo del entrenamiento no es eliminar una muletilla ni adquirir una personalidad. Es pasar de una distribución aleatoria de fragmentos a una distribución que empiece a respetar regularidades lingüísticas. Los personajes de los capítulos siguientes solo pueden entenderse contra este origen.

La serie empieza aquí: primero hubo texto sin voz; después, una voz atrapada en una frase; más tarde, un repertorio que todavía no sabe organizarse.

## Capítulo I — El modelo sindicalista

**Checkpoint:** 5.000 pasos  
**Holdout:** 100 preguntas  
**Run de evaluación:** [42911715548](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548)  
**Artefacto:** [holdout de 5k](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620)  
**SHA-256 del checkpoint:** `cb6d01e5feeb55d12ca93bbc67d751e790789840abb3d9291955aa0d0fd4edbe`  
**Resultado observado:** 100 respuestas no vacías; «El patrón» aparece en 96/100. No se calculó una puntuación automática de acierto.  
**Latencia media registrada:** 0,217 segundos por pregunta.

El primer personaje reconocible de esta pequeña historia no fue precisamente un enciclopedista. Fue el modelo sindicalista.

Al enfrentarse al holdout, el modelo mostró una tendencia muy marcada a volver una y otra vez sobre la misma idea: «El patrón». La frase aparecía con una insistencia casi cómica, como si el entrenamiento hubiera conseguido fijar una asociación verbal antes de construir una capacidad sólida para desarrollar respuestas distintas. No parecía estar razonando sobre cada pregunta: encontraba un carril lingüístico estrecho y regresaba a él.

La escena tenía algo de caricatura. Preguntáramos lo que preguntáramos, el modelo parecía dispuesto a llevar la conversación al terreno del patrón. De ahí el apodo de *modelo sindicalista*: no porque hubiera aprendido una teoría social coherente, sino porque había convertido una expresión recurrente en su refugio conversacional.

### Lo que dicen los números — y lo que no dicen

Las 100 preguntas produjeron respuestas no vacías. No se ejecutó una comparación automática validada contra las rúbricas, así que no atribuimos una tasa de acierto ni de error. El dato sólido es otro: «El patrón» aparece en 96 de las 100 salidas. Esa concentración revela un problema cualitativo claro: diversidad de salida y adaptación a la pregunta todavía muy limitadas.

La latencia media, cercana a 0,217 segundos por pregunta, indica que la inferencia era rápida en ese ensayo. Pero velocidad y calidad son dimensiones distintas. El modelo podía contestar deprisa y, aun así, quedarse atrapado en un patrón.

### La lección del primer holdout

Este primer capítulo deja una advertencia útil para todo el proyecto: una pérdida de entrenamiento que desciende no garantiza que el modelo haya aprendido a responder de forma flexible. Puede aprender regularidades del corpus y reproducirlas con facilidad sin haber adquirido todavía suficiente capacidad para seleccionar, combinar y expresar el conocimiento según la pregunta.

Por eso los holdouts no son un trámite al final del entrenamiento. Son el contraste con la realidad externa al lote de entrenamiento. Nos permiten detectar comportamientos que una curva de pérdida no cuenta: muletillas, bucles, respuestas genéricas, confusiones entre dominios y ausencia de transferencia.

El modelo sindicalista no fue un fracaso inútil. Fue el primer personaje que nos enseñó qué debíamos vigilar.

## Capítulo II — Del patrón al esperpento

**Checkpoint:** 10.000 pasos acumulados  
**Run de entrenamiento:** [42902793379](https://github.com/orbitalronin94/RONINIA/actions/runs/42902793379)  
**SHA-256 del checkpoint:** b82df8b5d06171a9e6db6157d4036854ea445a84f8462b731c4d6d9892e3e172  
**Holdout:** las mismas 100 preguntas del ensayo de 5.000 pasos  
**Run de evaluación:** [42970549370](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370)  
**Artefacto:** [holdout completo](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652)  
**SHA-256 del holdout:** 3cd8c1eb3142ebf9c6cc17d2e19353be3472d61ac7b7cfb6de0cbb233cf4a535

El segundo capítulo empieza con una ausencia. En el primer holdout, el modelo encontraba una salida casi universal: «El patrón». No importaba demasiado si la pregunta trataba de lógica, matemáticas o conocimiento general; la frase volvía a ocupar el centro de la respuesta. A los 5.000 pasos, esa expresión aparecía en 96 de las 100 salidas.

A los 10.000 pasos, ya no aparece en ninguna.

No es todavía el nacimiento de un razonador solvente. Es algo más modesto, pero también más interesante para esta crónica: el modelo ha dejado de apoyarse en aquella única muletilla y ha empezado a recorrer otros caminos del corpus. Donde antes repetía «El patrón», ahora aparecen fragmentos de explicación, referencias al contexto, fórmulas de diagnóstico, expresiones del esperpento y evasivas explícitas. El personaje ha cambiado de voz, aunque todavía no domine del todo lo que quiere decir.

En algunas respuestas asoma una voz casi sentenciosa: «No confundas autoridad con demostración». En otras, el texto se deshace en repeticiones alrededor de «el impacto». Y en otras aparece una salida que forma parte deliberada del registro aprendido: «ni puta idea». La transformación tiene algo de esperpento: ya no es el mismo estribillo repetido cien veces, sino un repertorio más amplio de voces que a veces encajan con la pregunta y otras veces se cruzan, se interrumpen o se quedan a medio construir.

### La diferencia que sí podemos medir

La comparación de los artefactos permite describir el cambio sin convertirlo en una impresión vaga. Se incorpora el paso cero como origen, pero se conserva la advertencia de que su contexto y su número de parámetros difieren ligeramente:

| Señal observada | Paso 0 | 5.000 pasos | 10.000 pasos |
|---|---:|---:|
| Respuestas que contienen «El patrón» | 0/100 | 96/100 | 0/100 |
| Respuestas que contienen «ni puta idea» | 0/100 | 0/100 | 16/100 |
| Respuestas que contienen «impacto» | 0/100 | 0/100 | 19/100 |
| Respuestas no vacías | 100/100 | 100/100 | 100/100 |
| Latencia media por respuesta | 0,338 s | 0,217 s | 0,240 s |
| BPB sobre corpus de validación fijo | Pendiente | Pendiente | Pendiente |

Estas frecuencias describen apariciones literales, no una clasificación semántica. No significan que 16 respuestas sean buenas por incluir una evasiva, ni que las 19 menciones de «impacto» sean pertinentes. Sí muestran que la distribución superficial de las respuestas ha cambiado de manera verificable: la fórmula dominante del primer checkpoint desaparece y otras familias de expresiones pasan a ocupar espacio.

La latencia media aumenta ligeramente, de 0,217 a 0,240 segundos por pregunta. La diversificación observada no vino acompañada de una mejora de velocidad. Es un dato contraintuitivo, pero no permite afirmar que el modelo tarde más porque «piense» más: solo sabemos que la inferencia greedy medida tardó algo más en este ensayo. No tenemos evidencia de razonamiento interno ni de que el mayor repertorio sea la causa del incremento.

### La mácula: rotación de tics, no progreso demostrado

La desaparición de «El patrón» es real, pero no basta para declarar una mejora de capacidad. El nuevo checkpoint muestra otras recurrencias. La lectura más estricta es **TIC_ROTATION_VS_PROGRESS**: se ha movido la superficie de las respuestas; todavía no hemos demostrado que haya avanzado la calidad del modelado.

Para cerrar esa mácula hace falta medir bits-per-byte (BPB) sobre un corpus de validación fijo, reservado y byte-normalizado, con el mismo texto, tokenizer y protocolo para cada checkpoint. El BPB no está incluido en los artefactos actuales de inferencia: estos guardan respuestas, tokens generados y latencias, pero no logits ni pérdidas de evaluación. Por eso la columna BPB queda pendiente y no se rellena con una estimación. Hasta que exista esa medición, esta tabla registra cambios de comportamiento, no una mejora cuantitativa de modelado.

### Vitrina — La fuga de «el impacto»

«El patrón» fue el estribillo del primer personaje. En el segundo aparece otra plantilla: «el impacto». La cadena aparece en 19 de las 100 respuestas, a menudo encadenada consigo misma: «el impacto y se vuelven, con el impacto y el impacto…». No es lo mismo que una evasiva. Parece una fuga de esquema léxico: una plantilla del corpus que entra en la respuesta sin que la pregunta necesariamente la convoque.

La cifra 19/100 no demuestra por sí sola la causa, pero sí justifica aislarla como fenómeno propio. La próxima evaluación debe medir no solo si aparece la palabra, sino si la frase completa se activa fuera de contexto, si se repite dentro de una misma salida y si guarda relación con el dominio o la rúbrica de la pregunta.

### Desglose de la abstención — «ni puta idea»

Las 16 apariciones de «ni puta idea» se revisaron pregunta por pregunta. En las 16, el enunciado contiene información suficiente para responder o permite una respuesta razonada; no se identificó ninguna pregunta deliberadamente irresoluble dentro de ese grupo. Por tanto, el desglose preliminar es:

| Tipo de pregunta entre las 16 apariciones | Casos |
|---|---:|
| Pregunta con información suficiente | 16 |
| Pregunta sin información suficiente | 0 |
| Abstención aparentemente apropiada | 0 |
| Abstención aparentemente inapropiada | 16 |

La lectura es provisional y se refiere solo a estas 16 salidas, no a la calibración global del modelo. La clasificación se hizo leyendo pregunta y rúbrica; no existe todavía una doble anotación independiente, por lo que no se presenta una «precisión del clasificador» validada. Además, la rúbrica de `math-004` contiene una nota que contradice la pregunta matemática —la pregunta sí permite resolver el sistema, mientras la rúbrica introduce una ficción ajena—. Ese caso debe anotarse como inconsistencia del benchmark y adjudicarse antes de usarlo para puntuar acierto. La presencia de «ni puta idea» en este subconjunto apunta a abstenciones mal situadas, pero no basta para estimar la calibración general.



### Leer el esperpento sin confundirlo con un fallo

Hay una decisión de interpretación que importa tanto como los números. RONIN-10M se entrena con un lexicón que incluye esperpento, expresiones evasivas y marcadores como NH. Esos elementos no son errores por definición: forman parte del material que se quiere incorporar al estilo del modelo.

La respuesta «ni puta idea», por ejemplo, puede ser una evasiva deliberada y reconocible dentro de ese registro. No debe premiarse ni castigarse de forma automática por su mera presencia. La pregunta relevante es si el modelo sabe cuándo esa salida corresponde, si puede sostener después una explicación y si distingue una incertidumbre legítima de una pregunta que sí puede resolver.

Lo mismo ocurre con NH y con el lenguaje de diagnóstico. Su aparición demuestra que ciertos rasgos del corpus están llegando a la generación; no demuestra por sí sola que el modelo comprenda su función. Hay que separar tres planos:

- **Identidad estilística:** expresiones del esperpento, marcadores NH, evasivas y cambios de registro que pertenecen al corpus.
- **Adecuación:** que el registro elegido responda a la pregunta concreta y no sea una inserción automática.
- **Coherencia y resolución:** que la respuesta mantenga una idea, complete el razonamiento y llegue a una conclusión defendible.

En el checkpoint de 10.000 pasos conviven señales de los tres planos. Hay más variedad verbal que en el primer capítulo, pero también persisten fragmentos truncados, repeticiones locales y respuestas que no resuelven el problema planteado. La desaparición de «El patrón» es una transformación observable; no es todavía una prueba de competencia general.

### Lo que revela el segundo personaje

El modelo sindicalista tenía una obsesión: volver al patrón. El personaje de los 10.000 pasos es menos uniforme y más difícil de resumir. A veces parece intentar explicar; a veces invoca el contexto; a veces se refugia en una evasiva que el propio corpus le ha enseñado; y a veces mezcla esas voces sin conseguir ordenarlas. El cambio es narrativamente visible, pero la mácula TIC_ROTATION_VS_PROGRESS impide venderlo como mejora demostrada: más personajes no equivalen todavía a más capacidad.

Ese cambio importa porque indica que el entrenamiento no se limitó a reforzar la misma respuesta dominante. El espacio de generación se ha movido. Pero el nuevo repertorio todavía necesita organización: no basta con disponer de más expresiones, hay que aprender a escogerlas, conectarlas y detenerse cuando la respuesta está completa.

### Resultado técnico

El holdout contiene 100 preguntas y conserva el mismo hash de conjunto que el registro del checkpoint de 5.000 pasos. La generación se realizó con greedy argmax, máximo de 32 tokens nuevos, dos hilos, sin KV cache y sin RAG. El checkpoint contiene 9.757.440 parámetros y utiliza el tokenizer cuyo SHA-256 queda registrado en el manifiesto.

El tiempo total de generación fue de aproximadamente 24,02 segundos, con una media de 0,240 segundos por respuesta. Las 100 salidas fueron no vacías. No se calculó una puntuación automática de calidad semántica ni una tasa validada de aciertos; por ello, este capítulo no atribuye al checkpoint una mejora de exactitud que el experimento no midió.

### Decisión

El checkpoint de 10.000 pasos queda registrado como **modelo experimental activo** de RONIN-10M. Se conserva su SHA-256, el run de entrenamiento, el tokenizer y el artefacto de holdout. La decisión reconoce un cambio cualitativo concreto frente a los 5.000 pasos: la respuesta deja de girar alrededor de «El patrón» y empieza a expresar una variedad mayor de rasgos del corpus.

La siguiente iteración tendrá que responder a una pregunta más exigente: si el modelo puede convertir ese repertorio en respuestas pertinentes y coherentes, manteniendo la identidad estilística que se quiere enseñar. Para ello se exigirán BPB sobre validación fija, desglose completo de abstenciones y análisis específico de la fuga «el impacto» antes de llamar progreso a una rotación de expresiones. El segundo capítulo no cuenta todavía la historia de un modelo que ya sabe; cuenta la de uno que ha dejado de repetir siempre lo mismo y empieza, con resultados desiguales, a buscar otra voz.

## Historial de ejecuciones

| Fecha | Evaluación | Run ID | Resultado | Ejecución | Artefactos | Commit |
|---|---|---:|---|---|---|---|
<!-- HOLDOUT-INDEX-START -->

| 2026-11-10 | RONIN-10M — step-0 baseline inference holdout | 42874585777 | success | [Ver ejecución](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777) | [ronin-step0-baseline.zip](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777) | — |

<!-- HOLDOUT-INDEX-END -->

## Cómo funciona

El workflow `.github/workflows/update-holdout-registry.yml` escucha los eventos `workflow_run: completed`. Solo ejecuta el registro si el nombre de la ejecución contiene `holdout`. Consulta la API de GitHub para recuperar los artefactos de esa ejecución y actualiza esta tabla en `main`.

El actualizador no descarga ni ejecuta los artefactos ni hace checkout del código de la ejecución que acaba de terminar. Para que una evaluación futura aparezca aquí automáticamente, nombra su workflow incluyendo la palabra `holdout` (por ejemplo, `RONIN-10M — checkpoint holdout`).

## Protocolo de lectura

- Comparar checkpoints con las mismas preguntas, configuración de generación y condiciones de inferencia.
- Separar coincidencia literal, evaluación semántica, calidad de respuesta, diversidad y latencia. No presentar una como sustituta de las demás.
- Interpretar el lexicón de esperpento y los marcadores intencionales según el corpus, no como errores por defecto.
- Registrar el identificador del checkpoint, SHA-256, run de entrenamiento, run de evaluación y artefactos.
- Distinguir siempre entre resultados observados, hipótesis e interpretaciones narrativas.
- No interpretar la rotación de tics como progreso sin BPB/validación fija y análisis de adecuación de abstenciones.
- Toda ejecución holdout debe mantener la convención en el nombre del archivo y en el campo `name:`; una discrepancia debe fallar explícitamente.
- No declarar una puntuación de calidad si no se ha medido con un evaluador explícito y validado.

## Baseline de referencia

La evaluación de paso 0 es la referencia inicial: 100 preguntas, checkpoint sin entrenamiento, tokenizer 8k y generación greedy sin RAG. Se conserva para comparar los siguientes checkpoints con el mismo holdout.
