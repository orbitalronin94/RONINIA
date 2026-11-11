# RONINIA

**RONINIA** es una línea independiente de investigación para entrenar desde cero un modelo de lenguaje compacto de aproximadamente 10 millones de parámetros. No hereda checkpoints ni pesos de MINIRONIN: reutiliza únicamente corpus de entrenamiento admitido, con procedencia y hashes.

## Modelo experimental activo

El checkpoint seleccionado actualmente es el de **10.000 pasos acumulados**. La selección prioriza la mayor diversidad de salida observada frente al patrón casi único «El patrón» del checkpoint de 5.000 pasos. El lexicón de esperpento, los marcadores NH y las evasivas deliberadas forman parte del corpus intencional y no se consideran fallos por defecto.

- Manifiesto verificable: [models/active.json](models/active.json)
- Entrenamiento: [run 42902793379](https://github.com/orbitalronin94/RONINIA/actions/runs/42902793379)
- Holdout de 100 preguntas: [run 42970549370](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370)
- SHA-256 del checkpoint: `b82df8b5d06171a9e6db6157d4036854ea445a84f8462b731c4d6d9892e3e172`

La promoción es experimental: el holdout confirma que las 100 respuestas se generaron con el protocolo esperado, pero no produce por sí mismo una puntuación automática de calidad semántica.

## Diseño: RONIN-10M

| Elemento | Configuración |
|---|---:|
| Arquitectura | Transformer decoder-only, pre-LN |
| Capas / cabezas | 6 / 8 |
| Dimensión | 288 |
| FFN | 1.536 |
| Contexto | 512 tokens |
| Vocabulario | 8.192 tokens BPE byte-level |
| Embeddings | Entrada/salida compartidos |
| Inicialización | Aleatoria, desde cero |
| Filas activas | Las 8.192 desde el primer paso |

El vocabulario se ha reducido a la mitad respecto al diseño inicial. Se amplía el FFN de 864 a 1.536 para mantener el tamaño del modelo: **9.831.168 parámetros entrenables** con la configuración general. El checkpoint experimental activo usa el perfil de velocidad con contexto 256 y contiene **9.757.440 parámetros**, verificados en su manifiesto de promoción.

## Principios

- **No se heredan pesos:** MINIRONIN aporta corpus, no checkpoints ni estado del optimizador.
- **Tokenizador propio y pequeño:** BPE byte-level de 8.192 tokens, entrenado desde cero exclusivamente sobre el corpus de entrenamiento seleccionado.
- **Sin filas bloqueadas:** embeddings y proyección de salida tienen 8.192 filas activas.
- **Datos trazables:** cada preparación registra archivos, documentos, bytes y SHA-256.
- **Evaluación separada:** los registros identificados como holdout/evaluación se excluyen del corpus y del entrenamiento del tokenizador.
- **GitHub Actions como laboratorio:** preparación, validación, entrenamiento y evaluación se ejecutan en workflows.

## Corpus de referencia

La preparación del tokenizador utiliza el artefacto unificado de MINIRONIN del run exitoso **42523463620** en main (8 de noviembre de 2026). El artefacto minironin-unified-train-corpus-42523463620 ocupa **776.739.403 bytes (aprox. 777 MB)**. No se utiliza el artefacto posterior de varios gigabytes para esta configuración.

El workflow verifica el estado y la procedencia del run, descarga el artefacto, valida SHA256SUMS y genera un flujo de texto y un manifiesto. Se conservan los registros sintéticos admitidos; se excluyen los registros identificados como evaluación/holdout. No se importan checkpoints ni datos de evaluación.

## Preparación y entrenamiento

1. Ejecutar prepare-tokenizer.yml para descargar el corpus de 777 MB y entrenar el BPE de 8.192 tokens.
2. Verificar el artefacto roninia-tokenizer-8k-*, su hash y la huella SHA-256 del corpus.
3. Ejecutar train-ronin-10m.yml usando el ID del run del tokenizador. El entrenamiento comienza desde inicialización aleatoria y guarda checkpoints cada 5.000 pasos.

El desarrollo local es opcional; los workflows son la vía reproducible del proyecto.

## MINIRONIN y RONIN-10M: continuidad de método, cambio de hipótesis

MINIRONIN tenía tres objetivos distintos. Conviene no confundirlos ni atribuir a RONIN-10M una victoria sobre todos ellos.

### 1. Demostrar que el método es largo y el modelo es corto

MINIRONIN dejó una crónica de **810.000 pasos, catorce checkpoints, cuarenta vitrinas y 0/100 aciertos** en el holdout histórico. La conclusión no es que el método fracasara: el método de experimentación, registro y conservación de evidencias quedó demostrado; la capacidad útil del modelo no llegó a consolidarse.

RONIN-10M **hereda ese método**. No necesita volver a demostrar que se puede documentar un experimento largo. Su hipótesis es diferente: comprobar si un modelo entrenado desde cero, con un tokenizador BPE byte-level de 8.192 tokens, un corpus reorganizado y una configuración distinta, puede adquirir capacidades observables que MINIRONIN no mostró.

### 2. Producir un artefacto reproducible y con trazabilidad forense

Este objetivo también viene de MINIRONIN. RONIN-10M lo hereda y amplía el archivo: hashes de checkpoints, identidad del holdout, configuración de generación, artefactos y crónica de cambios.

El avance del libro de holdouts es un resultado del **método y del archivo**, no una mejora atribuible a los pesos. La trazabilidad permite comparar sin convertir una impresión narrativa en una puntuación de calidad.

### 3. Que el loro diga cosas divertidas

Este objetivo apareció casi accidentalmente en MINIRONIN. En RONIN-10M los tics han aparecido mucho antes: «El patrón» dominó 96/100 salidas a 5k; a 10k dejó de aparecer y surgieron «ni puta idea» (16/100) y «impacto» (19/100).

Es tentador describirlo como una rotación de tics 65 veces más rápida tomando 650k y 10k como hitos. Esa cifra es **una comparación temporal aproximada, no una medida de capacidad ni una relación causal**. Los modelos, tokenizadores, corpus y protocolos de entrenamiento no son idénticos. Una rotación más rápida puede reflejar segmentación distinta, composición del corpus o dinámica de generación; no demuestra más inteligencia ni más pertinencia.

## Qué aporta RONIN-10M y qué sigue sin demostrar

**Diferencias de diseño relevantes:**

- **Tokenizador de 8k:** puede representar el corpus con secuencias más compactas. La compresión efectiva debe medirse en tokens por byte sobre el mismo texto; no se debe dar por hecho un factor fijo de 3× sin esa medición.
- **EOS reservado:** el tokenizador contempla un token EOS dedicado. Que exista y que el generador lo compruebe no demuestra que el modelo lo emita. El holdout actual no conserva explícitamente el motivo de terminación ni cuenta los EOS emitidos; por tanto, el primer EOS real del proyecto sigue pendiente de verificación.
- **Configuración y capacidad distintas:** los recuentos de parámetros solo son comparables si se especifica qué se cuenta (parámetros totales, activos o entrenables) y se contrasta la arquitectura de ambos modelos.
- **Corpus reorganizado:** puede adelantar la aparición de patrones del lexicón y de la abstención. Su efecto debe separarse de los efectos del tokenizador y del número de pasos.

**Lo que no se compra con un tokenizador:**

- **Pasos y exposición:** a 10k pasos, RONIN-10M está muy lejos de los 810k de MINIRONIN. El número de pasos por sí solo tampoco mide exposición: hay que registrar tokens realmente procesados.
- **Calibración:** emitir EOS no equivale a saber cuándo conviene terminar. El EOS apropiado exige medir cierres en respuestas correctas, abstenciones justificadas y preguntas que requieren continuar.
- **Criterio de éxito:** antes de escalar hacia 100k pasos debe declararse qué resultados contarían como avance, qué controles se aplicarán y qué evidencia podría refutar la hipótesis.

Como referencia, una estimación de 5,12 millones de tokens vistos frente a unos 6,1 millones de parámetros daría aproximadamente **0,84 tokens por parámetro**. Es una relación ilustrativa, no una ley de calidad ni una predicción de rendimiento. Las reglas de escalado tipo Chinchilla no deben convertirse en un umbral automático para un experimento pequeño con corpus, tokenizador y objetivo específicos.

## El riesgo de convertir el museo en escaparate

Si RONIN-10M llega a 100k o 200k pasos y produce respuestas más cerradas, con EOS verificado y cierta pertinencia, aparecerá la tentación de presentarlo como «el modelo que sí funciona». El Grimorio exige resistir esa simplificación.

Un modelo de unos pocos millones de parámetros que parece casi útil no es, por eso, un sistema útil. Puede ser un becario que ha aprendido a hablar sin decir demasiado. El museo no existe para maquillar el fracaso ni para vender una promesa: existe para documentar qué ocurrió, qué cambió y qué sigue sin saberse.

La comparación honesta no será «RONIN-10M supera a MINIRONIN». Será una ficha de evidencia: **tokenizador, corpus, pasos, tokens vistos, checkpoint, mismo conjunto de preguntas, protocolo, respuestas cerradas, EOS reales, abstenciones apropiadas, tics, errores y aciertos**. Solo entonces podremos decidir si observamos una mejora, un cambio de régimen o simplemente otra forma de fallar.

> Un hombre tuvo dos hijos. Al mayor le enseñó a andar descalzo por el desierto. Tardó veinte años en llegar al otro lado. Al pequeño le dio botas y un mapa. Llegó en un mes. Le preguntaron si el pequeño había logrado lo mismo que el mayor. Dijo: «No. El mayor aprendió a andar descalzo. El pequeño aprendió a usar el mapa. Los dos llegaron. Pero solo uno sabe lo que cuesta no tener botas».

**Vigilad la homeostasis.**

## Contrato del registro de holdouts

El registro automático escucha `workflow_run: completed`. Para que una evaluación se incorpore al libro, **el nombre del archivo** debe incluir `holdout` (por ejemplo, `.github/workflows/checkpoint-holdout-ronin-10m.yml`) y el campo YAML `name:` también debe incluir esa palabra. El listener valida ambos nombres: si uno se modifica y el otro no, la ejecución falla explícitamente. Si se renombra el archivo y el workflow a la vez, hay que actualizar conscientemente este contrato y su documentación.

No basta con que el job termine en verde: el registro conserva el run, conclusión, artefactos y commit de origen. Consulta la [crónica de holdouts](docs/HOLDOUTS.md) para las interpretaciones narrativas, límites de las métricas y máculas abiertas.

**Criterio de lectura actual:** la desaparición de una muletilla o la aparición de otras solo demuestra cambio de distribución superficial. No se declarará progreso de modelado sin BPB medido sobre una validación fija, y las abstenciones se analizarán por adecuación a la información disponible.
