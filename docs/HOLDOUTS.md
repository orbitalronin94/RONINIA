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
**SHA-256 del checkpoint:** `b82df8b5d06171a9e6db6157d4036854ea445a84f8462b731c4d6d9892e3e172`  
**Holdout:** 100 preguntas  
**Run de evaluación:** [42970549370](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370)  
**Artefacto:** [holdout completo](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652)  
**SHA-256 del holdout:** `3cd8c1eb3142ebf9c6cc17d2e19353be3472d61ac7b7cfb6de0cbb233cf4a535`

El segundo personaje ya no responde a casi todo con «el patrón». En las 100 preguntas aparecen más registros, expresiones y formas de salida. La diferencia más importante respecto al checkpoint de 5.000 pasos es esa ampliación de diversidad: el modelo deja de refugiarse de manera casi exclusiva en una única fórmula.

### Leer el corpus antes de juzgar la salida

RONIN-10M se entrena también con un lexicón de esperpento y expresiones deliberadamente evasivas. Marcadores como **NH** y fórmulas como «ni puta idea» pertenecen a esa distribución intencional. No deben clasificarse automáticamente como errores, alucinaciones o incapacidad de responder: su función depende del contexto y del registro que el corpus pretende enseñar.

La evaluación debe distinguir entre:
- **Rasgos estilísticos intencionales:** lexicón del esperpento, marcadores NH, evasivas deliberadas y cambios de registro.
- **Adaptación a la pregunta:** si la salida selecciona un registro pertinente para la pregunta y el dominio.
- **Fallos de generación:** bucles degenerativos, fragmentos truncados o combinaciones sin coherencia, que sí requieren seguimiento.

Esta separación evita penalizar al modelo por haber aprendido precisamente una parte del estilo que queríamos incorporar.

### Resultado técnico

El workflow generó las 100 respuestas y verificó el checkpoint, el tokenizer y el protocolo. La generación utilizó greedy argmax, dos hilos, un máximo de 32 tokens nuevos y no utilizó RAG ni KV cache. El tiempo total registrado fue de aproximadamente 24,02 segundos, con una media de 0,240 segundos por respuesta.

No se calculó una puntuación automática de calidad semántica. Por tanto, la promoción no se presenta como una cifra de exactitud ni como una demostración de razonamiento general. Se basa en la mejora cualitativa observada en diversidad de salida frente al comportamiento excesivamente concentrado de los 5.000 pasos, conservando el artefacto y toda su procedencia.

### Decisión

El checkpoint de 10.000 pasos queda seleccionado como **modelo experimental activo** de RONIN-10M. Se conserva su SHA-256, el run de entrenamiento, el tokenizer y el holdout asociado para que cualquier continuación pueda partir exactamente de este estado. La selección no borra el baseline de 5.000 pasos ni convierte una observación cualitativa en una puntuación que no hemos medido.

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
