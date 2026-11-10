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
- Registrar el identificador del checkpoint, SHA-256, run de entrenamiento, run de evaluación y artefactos.
- Distinguir siempre entre resultados observados, hipótesis e interpretaciones narrativas.
- No declarar una promoción de modelo solo por una pérdida menor o una salida llamativa: exigir la comparación holdout correspondiente.

## Baseline de referencia

La evaluación de paso 0 es la referencia inicial: 100 preguntas, checkpoint sin entrenamiento, tokenizer 8k y generación greedy sin RAG. Se conserva para comparar los siguientes checkpoints con el mismo holdout.
