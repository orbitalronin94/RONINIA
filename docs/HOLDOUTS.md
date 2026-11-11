# Registro de holdouts — RONIN-10M

Este documento es la crónica narrativa y el registro técnico de las evaluaciones de RONIN-10M. Cada holdout tendrá su propio capítulo: qué checkpoint se examinó, qué comportamiento apareció, qué nos enseñó y qué preguntas deja abiertas. La narración no sustituye a las métricas; sirve para conservar el contexto de cada experimento.

Los enlaces de las ejecuciones y sus artefactos se mantienen en el índice histórico. Los artefactos pueden caducar según la política de GitHub Actions, por lo que conviene conservar también sus hashes y resultados esenciales.

## Prólogo — Antes de aprender

La evaluación de paso cero es el punto de partida: el modelo todavía no había recibido entrenamiento. No es una prueba de inteligencia ni una competición; es la fotografía inicial que permite saber qué cambia cuando los pesos empiezan a incorporar el corpus.

El baseline registrado utilizó 100 preguntas, el checkpoint inicial, tokenizer 8k y generación greedy sin RAG. Su función es sencilla y fundamental: fijar una referencia reproducible. Sin ese punto de comparación, cualquier respuesta posterior podría parecer una mejora solo porque la recordamos de forma distinta.

## Capítulo I — El modelo sindicalista

**Checkpoint:** 5.000 pasos  
**Holdout:** 100 preguntas  
**Run de evaluación:** [42890495710](https://github.com/orbitalronin94/RONINIA/actions/runs/42890495710)  
**Resultado observado:** 100 respuestas no vacías; 0 coincidencias exactas con las cadenas de referencia de la rúbrica.  
**Latencia media registrada:** aproximadamente 0,163 segundos por pregunta.

El primer personaje reconocible de esta pequeña historia no fue precisamente un enciclopedista. Fue el modelo sindicalista.

Al enfrentarse al holdout, el modelo mostró una tendencia muy marcada a volver una y otra vez sobre la misma idea: «El patrón». La frase aparecía con una insistencia casi cómica, como si el entrenamiento hubiera conseguido fijar una asociación verbal antes de construir una capacidad sólida para desarrollar respuestas distintas. No parecía estar razonando sobre cada pregunta: encontraba un carril lingüístico estrecho y regresaba a él.

La escena tenía algo de caricatura. Preguntáramos lo que preguntáramos, el modelo parecía dispuesto a llevar la conversación al terreno del patrón. De ahí el apodo de *modelo sindicalista*: no porque hubiera aprendido una teoría social coherente, sino porque había convertido una expresión recurrente en su refugio conversacional.

### Lo que dicen los números — y lo que no dicen

Las 100 preguntas produjeron respuestas no vacías, pero ninguna coincidió exactamente con la cadena de referencia evaluada por aquella rúbrica. Esa cifra describe coincidencia literal, no comprensión semántica: por sí sola no demuestra que todas las respuestas fueran conceptualmente incorrectas. La repetición observada, sin embargo, sí revela un problema cualitativo claro: diversidad de salida y adaptación a la pregunta todavía muy limitadas.

La latencia media, cercana a 0,163 segundos por pregunta, indica que la inferencia era rápida en ese ensayo. Pero velocidad y calidad son dimensiones distintas. El modelo podía contestar deprisa y, aun así, quedarse atrapado en un patrón.

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

La comparación de los dos artefactos permite describir el cambio sin convertirlo en una impresión vaga:

| Señal observada | 5.000 pasos | 10.000 pasos |
|---|---:|---:|
| Respuestas que contienen «El patrón» | 96/100 | 0/100 |
| Respuestas que contienen «ni puta idea» | 0/100 | 16/100 |
| Respuestas que contienen «impacto» | 0/100 | 19/100 |
| Respuestas no vacías | 100/100 | 100/100 |
| Latencia media por respuesta | 0,217 s | 0,240 s |

Estas frecuencias describen apariciones literales, no una clasificación semántica. No significan que 16 respuestas sean buenas por incluir una evasiva, ni que las 19 menciones de «impacto» sean pertinentes. Sí muestran que la distribución superficial de las respuestas ha cambiado de manera verificable: la fórmula dominante del primer checkpoint desaparece y otras familias de expresiones pasan a ocupar espacio.

La latencia media aumenta ligeramente, de unos 0,217 a 0,240 segundos por pregunta. En este ensayo, por tanto, la diversificación observada no vino acompañada de una mejora de velocidad. La diferencia es pequeña y no debe confundirse con una medición exhaustiva de rendimiento.

### Leer el esperpento sin confundirlo con un fallo

Hay una decisión de interpretación que importa tanto como los números. RONIN-10M se entrena con un lexicón que incluye esperpento, expresiones evasivas y marcadores como NH. Esos elementos no son errores por definición: forman parte del material que se quiere incorporar al estilo del modelo.

La respuesta «ni puta idea», por ejemplo, puede ser una evasiva deliberada y reconocible dentro de ese registro. No debe premiarse ni castigarse de forma automática por su mera presencia. La pregunta relevante es si el modelo sabe cuándo esa salida corresponde, si puede sostener después una explicación y si distingue una incertidumbre legítima de una pregunta que sí puede resolver.

Lo mismo ocurre con NH y con el lenguaje de diagnóstico. Su aparición demuestra que ciertos rasgos del corpus están llegando a la generación; no demuestra por sí sola que el modelo comprenda su función. Hay que separar tres planos:

- **Identidad estilística:** expresiones del esperpento, marcadores NH, evasivas y cambios de registro que pertenecen al corpus.
- **Adecuación:** que el registro elegido responda a la pregunta concreta y no sea una inserción automática.
- **Coherencia y resolución:** que la respuesta mantenga una idea, complete el razonamiento y llegue a una conclusión defendible.

En el checkpoint de 10.000 pasos conviven señales de los tres planos. Hay más variedad verbal que en el primer capítulo, pero también persisten fragmentos truncados, repeticiones locales y respuestas que no resuelven el problema planteado. La desaparición de «El patrón» es una transformación observable; no es todavía una prueba de competencia general.

### Lo que revela el segundo personaje

El modelo sindicalista tenía una obsesión: volver al patrón. El personaje de los 10.000 pasos es menos uniforme y más difícil de resumir. A veces parece intentar explicar; a veces invoca el contexto; a veces se refugia en una evasiva que el propio corpus le ha enseñado; y a veces mezcla esas voces sin conseguir ordenarlas.

Ese cambio importa porque indica que el entrenamiento no se limitó a reforzar la misma respuesta dominante. El espacio de generación se ha movido. Pero el nuevo repertorio todavía necesita organización: no basta con disponer de más expresiones, hay que aprender a escogerlas, conectarlas y detenerse cuando la respuesta está completa.

### Resultado técnico

El holdout contiene 100 preguntas y conserva el mismo hash de conjunto que el registro del checkpoint de 5.000 pasos. La generación se realizó con greedy argmax, máximo de 32 tokens nuevos, dos hilos, sin KV cache y sin RAG. El checkpoint contiene 9.757.440 parámetros y utiliza el tokenizer cuyo SHA-256 queda registrado en el manifiesto.

El tiempo total de generación fue de aproximadamente 24,02 segundos, con una media de 0,240 segundos por respuesta. Las 100 salidas fueron no vacías. No se calculó una puntuación automática de calidad semántica ni una tasa validada de aciertos; por ello, este capítulo no atribuye al checkpoint una mejora de exactitud que el experimento no midió.

### Decisión

El checkpoint de 10.000 pasos queda registrado como **modelo experimental activo** de RONIN-10M. Se conserva su SHA-256, el run de entrenamiento, el tokenizer y el artefacto de holdout. La decisión reconoce un cambio cualitativo concreto frente a los 5.000 pasos: la respuesta deja de girar alrededor de «El patrón» y empieza a expresar una variedad mayor de rasgos del corpus.

La siguiente iteración tendrá que responder a una pregunta más exigente: si el modelo puede convertir ese repertorio en respuestas pertinentes y coherentes, manteniendo la identidad estilística que se quiere enseñar. El segundo capítulo no cuenta todavía la historia de un modelo que ya sabe; cuenta la de uno que ha dejado de repetir siempre lo mismo y empieza, con resultados desiguales, a buscar otra voz.

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
- No declarar una puntuación de calidad si no se ha medido con un evaluador explícito y validado.

## Baseline de referencia

La evaluación de paso 0 es la referencia inicial: 100 preguntas, checkpoint sin entrenamiento, tokenizer 8k y generación greedy sin RAG. Se conserva para comparar los siguientes checkpoints con el mismo holdout.
