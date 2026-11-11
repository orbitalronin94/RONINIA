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


## Vitrina III — El BPE del «-eishon»: gramática sin diccionario

**Fenómeno:** recombinación subléxica con apariencia de productividad morfológica  
**Material observado:** «bugar», «ridación», «mentirable» y «el mentirable la sago»  
**Checkpoint de referencia:** RONIN-10M en continuación desde 10.000 pasos  
**SHA-256 del padre:** `b82df8b5d06171a9e6db6157d4036854ea445a84f8462b731c4d6d9892e3e172`  
**Estado:** observación cualitativa; hipótesis pendiente de experimento controlado

### La escena

Un hablante de español puede decir «esto es muy bugeable»: toma la raíz inglesa *bug* y le añade el sufijo español `-eable` (o la adaptación coloquial `-able`). El resultado no necesita estar en un diccionario para que otro hablante lo interprete. La construcción aprovecha una pauta productiva del español y la aplica a una raíz extranjera. Hay intención comunicativa y el contexto ayuda a recuperar el significado.

RONIN produce formas como «bugar», «ridación» o «mentirable». También puede encadenarlas en frases como «el mentirable la sago». La superficie recuerda a una palabra española: hay raíces reconocibles, terminaciones frecuentes y una sintaxis que parece querer arrancar. Pero la forma plausible no garantiza que exista un significado estable detrás.

La ironía es precisa: el hablante que inventa «bugeable» puede estar mostrando que domina una regla morfológica aunque desconozca parte del léxico inglés. El modelo, en cambio, puede estar recombinando fragmentos frecuentes del vocabulario BPE de 8k sin haber abstraído una regla gramatical ni asociado la palabra resultante a un concepto. No debemos atribuirle comprensión morfológica solo porque el resultado nos suene bien formado.

### La distinción

Conviene separar tres niveles:

1. **Invención interpretable — «bugeable».** Una forma nueva construida con una pauta productiva; el contexto y la intención permiten entenderla.
2. **Forma plausible — «mentirable».** Una secuencia que parece compatible con la morfología del español, pero cuyo significado no está establecido.
3. **Enunciado sin semántica estable — «el mentirable la sago».** Los fragmentos parecen lingüísticos, pero no forman una proposición cuya interpretación pueda mantenerse y verificarse.

En hablantes bilingües se habla de *transferencia morfológica negativa* cuando se aplican patrones de una lengua a otra y se producen formas no convencionales. Es una analogía útil para la escena del «-eishon», pero no describe literalmente el mecanismo del modelo. Para RONIN, la etiqueta provisional más prudente es **recombinación subléxica con apariencia de productividad morfológica**: el BPE ofrece piezas y el modelo aprende continuaciones estadísticas. Que esas piezas coincidan con raíces y sufijos no prueba que haya aprendido su función lingüística.

La fórmula de esta vitrina es: **la forma de la lengua sin la sustancia de la lengua**.

### Qué sabemos y qué no

**Observado:** el modelo emite formas novedosas o deformadas que recuerdan a construcciones morfológicas del español. Son muestras cualitativas del comportamiento de generación.

**Hipótesis:** algunas podrían surgir de la recombinación de fragmentos subléxicos frecuentes. También es posible que parte de la regularidad proceda de patrones de palabras completas, contexto o memorización del corpus. Sin análisis de tokens y controles no podemos adjudicar la causa.

**No demostrado:** que RONIN haya aprendido reglas morfológicas abstractas; que comprenda el significado de las formas inventadas; o que «mentirable» sea una palabra semánticamente vacía para cualquier hablante en cualquier contexto. La interpretación de una palabra inventada depende también del contexto y del lector.

### El experimento que falta

Para distinguir productividad de coincidencia estadística, la siguiente prueba deberá fijar antes del análisis un conjunto de raíces conocidas, raíces inventadas y raíces reservadas que no aparezcan en el corpus de entrenamiento. Se combinarán con sufijos productivos y no productivos, y se evaluarán al menos cuatro dimensiones:

- **Productividad:** ¿forma palabras plausibles con raíces no vistas, o solo repite combinaciones del corpus?
- **Sensibilidad morfológica:** ¿elige sufijos distintos según la categoría y el contexto, o los añade indiscriminadamente?
- **Estabilidad semántica:** si se le pide definir una palabra inventada, ¿mantiene una interpretación coherente al usarla en varios contextos?
- **Calibración:** cuando no puede justificar el significado, ¿reconoce que la forma la ha inventado y que no sabe qué significa?

El control debe incluir palabras reales, pseudopalabras construidas por humanos y recombinaciones aleatorias de fragmentos BPE. Hay que guardar el checkpoint exacto, tokenizer, tokens emitidos, prompts, configuración de generación y respuestas completas. La evaluación semántica debe hacerse a ciegas con una rúbrica fijada de antemano; no basta con que al evaluador le haga gracia la palabra.

### Por qué entra en el museo

No queremos borrar «mentirable» ni corregir el esperpento hasta convertirlo en prosa neutra. El humor y la invención verbal forman parte del objetivo del proyecto. La pregunta es si el modelo puede distinguir entre una invención deliberada, una palabra convencional y una secuencia que solo parece lenguaje.

La aspiración no es quitarle el ridículo: es que pueda reconocer cuándo está inventando, cuándo está jugando con la lengua y cuándo no tiene ni idea. Si algún día responde «me he inventado “mentirable”; no sé qué significa», habrá añadido algo más valioso que otro sufijo: una forma de honestidad sobre sus propios límites.

**Koan.** Un español llegó a Londres sin saber inglés. Le preguntaron qué tal el viaje. Dijo: «Muy good, pero el tube es muy complicateishon». Le entendieron. Volvió a España y contó que sabía inglés. Le preguntaron que tradujera «yo tengo un bug». Dijo: «I have a bugueishon». Le preguntaron qué era un bug. Contestó: «Ni puta idea, la verdad».

**Vigilad la homeostasis.**


## Capítulo IV — El paraguas de la biblioteca sumergida

**Checkpoint:** 30.000 pasos acumulados  
**Run de entrenamiento:** [42984964609](https://github.com/orbitalronin94/RONINIA/actions/runs/42984964609)  
**Artefacto de checkpoint:** [ronin-10m-chain-30k](https://github.com/orbitalronin94/RONINIA/actions/runs/42984964609#artifacts)  
**SHA-256 del checkpoint:** `140230697a4df69f43c2cc4f6dc95ba2cc596b095532d3e171c486891d26bc4a`  
**Run de evaluación:** [42994967183](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183)  
**Artefacto de evaluación:** [holdout de 30k](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)  
**Holdout:** las mismas 100 preguntas  
**SHA-256 del conjunto de preguntas:** `3cd8c1eb3142ebf9c6cc17d2e19353be3472d61ac7b7cfb6de0cbb233cf4a535`  
**Tokenizer SHA-256:** `605834d0d1deea545518be54ae0936060845107b906172f6628d0ff9520e57a4`  
**Resultado técnico:** 100/100 generaciones completadas; no se calculó una puntuación automática de calidad semántica.

A los 20.000 pasos, el loro había abierto expediente sobre un paraguas transparente que dormía bajo una escalera. También había aparecido la biblioteca sumergida, una imagen asociada en la historia de MINIRONIN. A los 30.000 pasos, ambas genealogías parecen encontrarse en una sola salida:

> «la sacción de los estados, el análisis de una para oxidado paraguas de la biblioteca sumergida. Respuesta: Everest es una»

La frase no es una respuesta correcta a la pregunta que la provocó. Pero como pieza de la crónica del modelo es excepcional: el paraguas de la familia de escenas de RONIN aparece ahora unido, en el mismo sintagma, a la biblioteca sumergida que se había observado en MINIRONIN. El objeto ya no duerme simplemente bajo una escalera; parece pertenecer a una biblioteca submarina. Y Everest irrumpe al final como un nuevo contenedor imposible. La escalera empieza a quedarse pequeña.

### Mácula: TIC_HYBRIDIZATION_ACROSS_MODELS

La etiqueta describe una **hipótesis de hibridación léxica por corpus compartido**. La salida combina dos motivos que en la crónica tienen genealogías distintas: el paraguas/objeto bajo la escalera, observado en RONIN, y la biblioteca sumergida, atribuida a MINIRONIN. Si ambos modelos estuvieron expuestos a material compartido, la recombinación puede explicarse por aprendizaje desde datos comunes, sin transferencia de pesos.

La frase constituye un caso visible de coaparición y recombinación en una misma salida. No demuestra por sí sola que cada componente proceda exclusivamente de un corpus distinto, ni que exista una transmisión causal entre modelos. Para elevar la hipótesis a hallazgo se necesita localizar las expresiones y variantes en ambos corpus, medir solapamiento exacto y aproximado, revisar sus contextos y comprobar si la combinación ya existe en los datos de entrenamiento.

### Mácula: TEMPLATE_STACKING

La revisión humana identifica el molde «La primera [X]» en quince respuestas. La ranura aparece ocupada por expresiones que a su vez recuerdan otras plantillas: «el sistema», «el fallo», «el archivo», «el proceso» o «el análisis». La impresión es la de una plantilla de apertura que se apoya en una segunda plantilla de contenido.

Este apilamiento parece más elaborado que la repetición de un único estribillo, pero no implica por sí mismo composición semántica. El recuento de quince casos es una anotación manual provisional sobre las cien salidas. La prueba pendiente consiste en medir la frecuencia literal y las variantes, identificar las ranuras, y comprobar si el modelo puede rellenarlas con información correcta cuando la pregunta y el corpus contienen esa información.

### Vitrina: NEOLOGISM_DENSITY

La revisión destaca ocho formas nuevas o deformadas:

- «Avector» / «Av2»
- «Noído»
- «Confundemicos»
- «Transgia»
- «Ajonimenta»
- «Teorece»
- «Lidencias»
- «Sinciidad»

La muestra más llamativa es la respuesta #50:

> «Avector: Avector: Av2. Av2. Av2. Av2. Av2. Av2.»

Aquí la invención parece convertirse en una notación repetida, una especie de unidad formal que el modelo no define. Otras salidas, como «Ajonimenta el sistema de las intenciones atribuidas», tienen una forma verbal reconocible aunque el significado no se estabilice. «Noído no necesita una promesa el coste de código» parece, por su parte, una frase construida con piezas familiares que no terminan de formar una proposición interpretable.

La lista es una selección cualitativa, no un inventario exhaustivo ni una tasa de neologismos validada. Tampoco conocemos todavía la segmentación BPE de estas formas. No se debe afirmar que «Avector» sea una fusión concreta de tokens, ni que «Ajonimenta» pruebe productividad morfológica, hasta inspeccionar los IDs de token y comparar las formas con el vocabulario y el corpus.

La auditoría deberá separar palabras ausentes del corpus, variantes ortográficas, errores de generación y secuencias compuestas por tokens subléxicos frecuentes. También deberá distinguir novedad formal de estabilidad semántica: una palabra puede ser nueva y aun así tener un significado recuperable por contexto; otra puede parecer española sin expresar nada estable.

### Mácula: CONTAINER_MUTATION_ESCALATION

La familia de escenas surrealistas parece cambiar de objeto entre checkpoints: paraguas transparente bajo una escalera, termómetro oxidado y, ahora, paraguas oxidado asociado a la biblioteca sumergida, con Everest en la misma respuesta. La escalera persiste como marco narrativo, mientras los objetos y contenedores mutan.

La lectura es provisional: la revisión identifica motivos y semejanzas, pero todavía no se ha calculado su frecuencia exacta en el corpus ni se ha demostrado que exista una plantilla generativa estable. Conviene conservar las frases literales y comparar en los siguientes checkpoints si reaparece el marco «objeto + atributo + bajo/de la escalera/biblioteca», qué ranuras cambian y si los cambios dependen del prompt.

### Mácula: NEGATIVE_CONTROL_LEAKAGE — persistencia de la rúbrica

La frase:

> «No procede aplicar un epíteto sin evidencia suficiente; una semejanza superficial no demuestra ese patrón.»

aparece en las respuestas #3, #65 y #69, según el recuento manual. También se observa una variante en #82: «la respuesta podría corresponder a la conducta descrita en su contenido, no por elogio».

El fragmento conserva una regla prudente del Lexicón, pero aparece como respuesta a preguntas técnicas de CI/CD que requieren información concreta. La repetición no demuestra que el modelo haya interiorizado la norma ni que sepa aplicarla: puede estar reproduciendo una rúbrica fuera de contexto. La variante de #82 parece más cercana al sentido de la regla, aunque tampoco basta para concluir que el modelo haya identificado correctamente la conducta preguntada.

La evaluación futura debe etiquetar cada aparición como pertinente, parcialmente pertinente o fuera de contexto, y contrastarla con las preguntas y sus rúbricas. La abstención calibrada exige reconocer qué información falta y por qué; repetir una frase de cautela no es suficiente.

### El cambio de moldes: de «Su función» a «Su propuesta»

En la revisión del checkpoint de 20.000 pasos destacaban «Su función es X, no Y» y los encabezados de tipo formulario. En 30.000 pasos, la expresión «Su propuesta» aparece en un recuento manual de 23 respuestas (#7, #10, #25, #26, #33, #46, #48, #52, #53, #55, #56, #57, #58, #63, #66, #67, #70, #71, #74, #84, #85, #92 y #97). El molde «La primera [X]» se anota en quince respuestas.

Son recuentos literales/manuales que deben reproducirse automáticamente sobre el JSON antes de tratarlos como métricas definitivas. La observación principal es que el repertorio de plantillas parece rotar y combinarse: una fórmula de apertura puede preceder a otra fórmula de contenido. No sabemos aún si esa combinación mejora la adaptación a la pregunta; las salidas revisadas muestran que con frecuencia sigue sin hacerlo.

### Lo que ha desaparecido — en esta muestra

La revisión no encuentra en el holdout de 30k varios tics destacados en checkpoints anteriores: «El patrón», «impacto» como bucle dominante, «Michaelación», «servidícula», «menos dinero conocimiento», «ni sus e inocuo» y la aparición independiente del termómetro oxidado. La familia del paraguas tampoco conserva exactamente su formulación anterior.

Es correcto decir que estos fragmentos no aparecen en la muestra revisada de cien respuestas. No es correcto declararlos extinguidos del modelo: una muestra finita no permite descartar que reaparezcan con otros prompts, semillas o configuraciones. «Ocho tics muertos» funciona como imagen narrativa, no como conclusión estadística.

### Lectura del hito: más variación, capacidad aún no acreditada

El checkpoint de 30.000 pasos ofrece una superficie de generación más variada en las muestras revisadas: neologismos, plantillas apiladas, cambios de objeto y una combinación memorable entre el paraguas y la biblioteca sumergida. Pero la evaluación no asigna una puntuación semántica automática, y las respuestas continúan mostrando fragmentación, asociaciones fuera de contexto y conclusiones incompletas. Las cien generaciones completadas no equivalen a cien respuestas correctas; tampoco existe aquí una tasa validada de aciertos.

Por tanto, el diagnóstico se limita a la evolución cualitativa de los tics. El holdout permite documentar la salida y conservar el comportamiento observado, no declarar una mejora de competencia. La siguiente comparación deberá mantener el mismo conjunto de preguntas, tokenizer y protocolo, y añadir anotación de pertinencia, corrección y terminación EOS verificable.

### Decisión

El checkpoint de 30.000 pasos queda registrado como **selección experimental activa** en `models/active.json`. La promoción administrativa no significa que haya superado una evaluación semántica ni que sea mejor que el checkpoint anterior en exactitud. Su valor en esta crónica es documentar un nuevo régimen de generación y preservar un caso especialmente memorable de recombinación léxica.

> El paraguas encontró la biblioteca. La biblioteca estaba sumergida. Everest contestó desde el fondo. El loro tomó nota y acuñó «Avector». Nadie ha demostrado todavía que sepa dónde está la escalera. Vigilad la homeostasis.


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


## Capítulo III — El funcionario de carrera y el paraguas

**Checkpoint:** 20.000 pasos acumulados  
**Run de entrenamiento:** [42973299789](https://github.com/orbitalronin94/RONINIA/actions/runs/42973299789)  
**Artefacto de lineage y checkpoint:** [ronin-10m-chain-20k](https://github.com/orbitalronin94/RONINIA/actions/runs/42973299789#artifacts)  
**SHA-256 del checkpoint:** `53528c3002ba07fe493815b9bfa4bd69bdc08cf985f77a4e59958ee2b3344cc4`  
**Holdout:** las mismas 100 preguntas  
**Run de evaluación:** [42982933515](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515)  
**Artefacto de respuestas:** [holdout completo de 20k](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515#artifacts)  
**SHA-256 del conjunto de preguntas:** `3cd8c1eb3142ebf9c6cc17d2e19353be3472d61ac7b7cfb6de0cbb233cf4a535`  
**Resultado técnico:** 100/100 respuestas generadas; workflow y verificaciones de identidad completados correctamente.

El loro ha dejado de ser sindicalista. Ahora parece funcionario de carrera. A 5.000 pasos, «El patrón» aparecía en 96/100 respuestas; a 10.000 había desaparecido y habían surgido «ni puta idea» (16/100) e «impacto» (19/100). En la lectura del checkpoint de 20.000, «El patrón» sigue ausente, el bucle literal de «impacto» deja de dominar y «ni puta idea» aparece menos, a menudo dentro de una respuesta más larga.

La nueva voz tiene formularios. «Su propuesta» aparece en más de veinte respuestas revisadas; también se repite el molde «Su función es X, no Y» y el encabezado «Evidencia/síntomas:». Son cambios descriptivos de la distribución de salida. No demuestran que el modelo sepa diagnosticar, que comprenda los campos de una ficha ni que haya adquirido criterio.

### Mácula: NEGATIVE_CONTROL_LEAKAGE

El modelo reproduce fórmulas del Lexicón destinadas a impedir diagnósticos sin evidencia —por ejemplo, «No procede aplicar un epíteto sin evidencia suficiente»— incluso ante preguntas técnicas que requieren una respuesta concreta. Es una fuga de lenguaje de control negativo, no una prueba de calibración. La siguiente auditoría debe contar esos controles en el corpus y distinguir su uso como respuesta automática de su uso pertinente como diagnóstico.

### Mácula: FUNCTIONAL_DEFINITION_MOLD

La estructura «Su función es X, no Y» se aplica a preguntas de dominios distintos, con frecuencia sin que X e Y formen una proposición informativa. La prueba pendiente es comprobar si el modelo puede rellenar el mismo molde con contenido correcto cuando el corpus contiene la respuesta, y si evita usarlo cuando no aporta nada.

### Vitrina candidata: POETIC_EMERGENCE

En tres salidas revisadas aparece una imagen de un paraguas transparente que duerme bajo una escalera, con variantes que sustituyen el paraguas por un termómetro oxidado o alteran la escena. La imagen es extraña y evocadora; merece conservarse como candidata a recombinación surrealista. Todavía no sabemos si procede de una secuencia del corpus, de una plantilla aprendida o de una recombinación de unidades del BPE. Antes de llamarla creación espontánea hay que buscar las frases y sus variantes en el corpus, inspeccionar la segmentación del tokenizador y probar prompts distintos sin pistas contextuales.

### Lectura del hito

El cambio principal no es una mejora de capacidad demostrada, sino un cambio de régimen de fracaso: de una muletilla léxica dominante a moldes discursivos más largos, con apariencia de formulario y alguna imagen surrealista memorable. El holdout actual no puntúa acierto semántico ni registra de forma suficiente la terminación EOS; por tanto, no permite afirmar razonamiento, calibración ni calidad factual. El checkpoint se conserva y promociona como **selección experimental activa**, no como modelo validado.

> El loro ya no reclama contra el patrón. Ahora abre expediente sobre el paraguas. Vigilad la homeostasis.


## Addendum — La biblioteca sumergida y las familias de escena

**Checkpoint:** RONIN-10M, 20.000 pasos  
**SHA-256:** `53528c3002ba07fe493815b9bfa4bd69bdc08cf985f77a4e59958ee2b3344cc4`  
**Holdout:** [100 preguntas y respuestas](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515)  
**Estado:** observaciones cualitativas añadidas después de la revisión humana; no alteran la selección experimental activa.

Este addendum conserva las observaciones nuevas sin convertir hipótesis de procedencia en hechos demostrados. Las frases citadas son salidas del holdout; las frecuencias que siguen son recuentos manuales de la revisión y deben reproducirse con un analizador sobre el artefacto antes de tratarlas como métricas automatizadas.

### Mácula: CORPUS_INHERITANCE_VIA_DATA

La salida «la biblioteca sumergida» (#38) recuerda un tic atribuido a MINIRONIN en checkpoints de 400k–700k. La hipótesis es **herencia de corpus**, no herencia de pesos: si ambos modelos fueron entrenados con material compartido, las asociaciones léxicas pueden reaparecer en una arquitectura entrenada desde cero.

**No demostrado todavía:** que la frase exacta estuviera en ambos corpus, que el solapamiento sea la causa de esta salida o que el tic haya cruzado intacto. La auditoría pendiente debe calcular solapamiento exacto y casi duplicado entre los manifiestos/corpus de MINIRONIN y RONIN, localizar la frase y variantes, y comparar sus contextos. Hasta entonces, la etiqueta describe una hipótesis de transmisión por datos.

### Vitrina: SCENE_MOLD_EMERGENCE

La familia «[objeto] que duerme bajo una escalera» aparece con objetos distintos: paraguas transparente y termómetro oxidado, entre otras variantes anotadas en la revisión. Lo relevante no es solo una frase llamativa, sino la posible estabilidad de una estructura con una ranura variable.

La hipótesis es un **molde de escena**: el marco verbal se conserva mientras cambia el objeto. Para verificar productividad hay que extraer todas las coincidencias y variantes del holdout y del corpus, contar objetos únicos, revisar prompts y segmentación BPE, y probar objetos reservados que no aparezcan en el corpus. No llamarlo todavía creatividad autónoma ni estructura profunda aprendida.

### Mácula: FUNCTIONAL_DEFINITION_MOLD — recuento revisado

La revisión humana señala diez respuestas con la forma «Su función es X, no Y». Se registra como recuento provisional sobre las 100 salidas, no como puntuación automática. Ejemplos especialmente reveladores son «Su función es la repetición, no el proceso», «Su función es el resultado, no el resultado» y «Su función es la infra, no el conocimiento».

La prueba siguiente debe medir por separado la presencia del molde y la corrección semántica de sus ranuras: que el modelo pueda completarlo correctamente cuando el dato está disponible, y que no lo use como plantilla vacía en dominios ajenos.

### Mácula: NEGATIVE_CONTROL_AS_ANSWER

El fragmento «No procede aplicar un epíteto sin evidencia suficiente…» aparece fuera de su contexto previsto, incluso en preguntas sobre bibliotecas, citas y rankings. Se conserva la distinción entre **fuga de rúbrica** y **abstención calibrada**: repetir una regla prudente no demuestra que el modelo sepa cuándo aplicarla.

La auditoría debe localizar en el corpus la frase y sus variantes, medir cuántas veces aparece en entrenamiento, y etiquetar en el holdout si cada emisión es pertinente, parcialmente pertinente o una respuesta fuera de contexto. Debe distinguirse de la abstención desnuda «ni puta idea» y de una respuesta que explica qué evidencia falta.

### Otras perlas del checkpoint

- «¿Qué audita las nubes?» (#99): candidata a nueva imagen de poesía administrativa. La etiqueta de novedad es provisional hasta buscar la frase en el corpus.
- «A vital IA. AWILLY AWILLY…» (#50): repetición fonética y posible degradación de generación; no inferir su segmentación o etimología sin inspeccionar tokens.
- «Por favor, no vonia» (#68), «Michaelación» (#13), «servidícula» (#6), «menos dinero conocimiento» (#15) y «ni sus e inocuo» (#32): conservar como muestras literales de recombinación/fragmentación, sin atribuir una derivación BPE concreta hasta inspeccionar el tokenizer.

### Decisión de promoción

El checkpoint de 20.000 pasos **ya está seleccionado como modelo experimental activo** en `models/active.json`; este addendum no realiza una segunda promoción ni afirma validación semántica. Se mantiene la identidad inmutable del checkpoint y su lineage. El holdout confirma 100 generaciones y la identidad del protocolo, no 100 aciertos.

> El hermano mayor dejó la biblioteca sumergida. El pequeño encontró el catálogo, lo mezcló con un termómetro oxidado y preguntó quién auditaba las nubes. Vigilad la homeostasis.
