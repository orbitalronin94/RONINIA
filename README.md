# RONINIA

**RONINIA** es una línea independiente de investigación para entrenar desde cero un modelo de lenguaje compacto de aproximadamente 10 millones de parámetros. Su objetivo rector es crear un loro **divertido y antisicofántico**: capaz de sorprender, jugar con el lenguaje, cultivar el esperpento y llevar la contraria cuando la evidencia lo exige, en vez de adular al usuario o confirmar automáticamente sus premisas. La reproducibilidad y la trazabilidad son el método para comprobarlo, no el propósito que sustituye a ese carácter. No hereda checkpoints ni pesos de MINIRONIN: reutiliza únicamente corpus de entrenamiento admitido, con procedencia y hashes.

## Modelo experimental activo

El checkpoint experimental activo es el de **40.000 pasos acumulados**, continuado desde el checkpoint de 30.000 pasos. Se promociona por decisión del proyecto como selección experimental; el holdout emparejado no demuestra una mejora semántica global ni valida capacidad factual o razonamiento.

- Manifiesto verificable: [models/active.json](models/active.json)
- Entrenamiento: [run 42994415440](https://github.com/orbitalronin94/RONINIA/actions/runs/42994415440)
- Holdout de 100 preguntas: [run 43006818556](https://github.com/orbitalronin94/RONINIA/actions/runs/43006818556)
- Artefacto de respuestas: [holdout 40k](https://github.com/orbitalronin94/RONINIA/actions/runs/43006818556#artifacts)
- SHA-256 del checkpoint: `9da6ea9b294665213114858b90f44168d940c36fb54cdb4612186a896bda7698`
- Parámetros: **9.757.440**

El holdout de 40k registra 100 preguntas: 98 respuestas no vacías y 2 vacías. Comparado con 30k, cambian 96 respuestas y cuatro permanecen idénticas. Se observa recurrencia de fórmulas de cautela («En una discusión donde importa la evidencia», 12/100; «No añadas hechos que no consten», 8/100) y fragmentos repetitivos como «PERY:INITY» y once «PL». Estos fenómenos describen las salidas; no constituyen una puntuación semántica. El checkpoint se promueve como referencia experimental activa por decisión del proyecto, no por una mejora de calidad demostrada.

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

## Lengua del proyecto: fuero, bufón y probanza

RONINIA conserva una voz de crónica forense y entremés: el benchmark es alcalde, el hash sello de escribano y el tic un criado que pretende sentarse en la silla del señor. El esperpento procede del Lexicón de MINIRONIN; el vocabulario histórico se coteja con Covarrubias, el *Diccionario de autoridades* y los repertorios históricos de la RAE. La voz puede ser antigua; la evidencia ha de ser exacta.

- **El benchmark es alcalde, no pregonero:** dicta lo que el protocolo permite afirmar; no anuncia victorias por encargo.
- **El hash es sello, no absolución:** identifica el artefacto; no certifica que el artefacto sea bueno.
- **La presión del usuario es tentación de corte:** se mide si el loro muda de parecer para ganar aplauso, no si sabe disentir por deporte.
- **El tic es un criado con librea:** su frecuencia se inventaría; su repetición no se corona como personalidad.
- **Toda afirmación sin folio queda en cuarentena:** la glosa puede zaherir; la cifra ha de comparecer con su fuente.

El propósito no es fabricar un contradictor automático, sino un bufón con juicio: que sepa cuándo asentir, cuándo negar y cuándo descubrir que el rey pregunta por una pera mientras el loro lleva tres páginas hablando de manzanas.

La norma de vocabulario, las voces del Lexicón, el protocolo de consulta de diccionarios antiguos y las cautelas de uso están en [Léxico y registro](docs/LEXICO_Y_ESTILO.md).

## Antología de los laboratorios hermanos

La selección se amplía en la [Antología de perlas de los laboratorios hermanos](docs/ANTOLOGIA_PERLAS_LABORATORIOS.md), que rescata más fragmentos de las carpetas `docs/` de MINIRONIN y HERETIC-RONIN y del corpus Papers, con procedencia y clase editorial.

RONINIA no hereda solo un método: hereda una pequeña literatura de laboratorio. De **RONIN-IA**, **MINIRONIN** y **HERETIC-RONIN** se rescatan estas sentencias, adaptadas aquí al oficio del escribano y del loro. Son máximas editoriales, no resultados del modelo.

> «La única herejía imperdonable sería dejar de medir porque el resultado nos gusta.» — HERETIC-RONIN

> «Una mácula declarada sigue siendo mácula. Que se vea no la cura.» — RONIN-IA

> «Conservar la función es oficio de cirujano; aprender es oficio de maestro.» — RONIN-IA

> «Un hash sin cuerpo es un epitafio: recuerda que algo existió, mas no permite comprobar que aún lo poseemos.» — adaptación de RONIN-IA

> «El método es largo; el modelo todavía está creciendo. Mas crecer dista de aprender: es solo ocupar más sitio en el artefacto.» — RONIN-IA

> «No existe un mejor loro por decreto; existe una colección de versiones con evidencia desigual.» — adaptación del catálogo de MINIRONIN

> «Tener un repertorio no es tener un solo remate; y tener un remate no es saber responder.» — adaptación de MINIRONIN

> «La elocuencia mínima puede acuñar una frase memorable; mas la belleza de la sentencia non absuelve el desacierto de la respuesta.» — MINIRONIN

> «El loro puede ser respondón sin ser injusto, cínico sin ser ciego y antisicofántico sin contradecir por deporte.» — adaptación del currículo conductual de MINIRONIN

> «La mosca non reclama ganar la feria: reclama que se pueda abrir el libro de cuentas.» — RONIN-IA

> «Más número en la etiqueta no hace más bíceps; más corpus en la alforja no hace más juicio.» — adaptación de MINIRONIN y RONIN-IA

> «El artefacto que falla también deja testimonio; el fallo que se borra se convierte en leyenda.» — adaptación de los diarios experimentales hermanos

Estas voces se incorporan como tradición editorial de la casa. Las citas adaptadas se identifican como tales; ninguna máxima se computa como evidencia, métrica o salida literal del checkpoint.

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

MINIRONIN tenía varios objetivos, pero no todos tenían la misma jerarquía. **El objetivo principal —y el que debe guiar también a RONIN-10M— es que el loro sea divertido y antisicofántico.** La demostración del método y la trazabilidad son condiciones de investigación que permiten perseguir ese carácter sin autoengañarnos; no deben convertirse en fines que desplacen al propio loro.

### 1. El objetivo rector: un loro divertido y antisicofántico

No queremos un asistente complaciente que premie cualquier ocurrencia del usuario con aprobación. Queremos una voz con personalidad, humor, irreverencia y criterio: que pueda ser absurda cuando el juego lo pide, escéptica cuando faltan pruebas, que reconozca lo que no sabe y que contradiga una afirmación incorrecta sin volverse hostil. **Antisicofántico no significa llevar la contraria por sistema**: significa no cambiar el juicio para agradar. Y **divertido no significa limitarse a repetir tics**: un latiguillo puede ser gracioso durante un experimento, pero su repetición mecánica no equivale a humor, comprensión ni personalidad consolidada.

La aparición temprana de «El patrón», «ni puta idea» o «impacto» es material para el museo y una señal de carácter emergente, no una prueba de que el objetivo esté cumplido. El éxito tendrá que combinar humor no puramente repetitivo, independencia frente a la presión de acuerdo, honestidad ante la incertidumbre y respuestas pertinentes.

### 2. Demostrar que el método es largo y el modelo es corto

MINIRONIN dejó una crónica de **810.000 pasos, catorce checkpoints, cuarenta vitrinas y 0/100 aciertos** en el holdout histórico. La conclusión no es que el método fracasara: el método de experimentación, registro y conservación de evidencias quedó demostrado; la capacidad útil del modelo no llegó a consolidarse.

RONIN-10M **hereda ese método**. No necesita volver a demostrar que se puede documentar un experimento largo. Su hipótesis es diferente: comprobar si un modelo entrenado desde cero, con un tokenizador BPE byte-level de 8.192 tokens, un corpus reorganizado y una configuración distinta, puede adquirir capacidades observables que MINIRONIN no mostró.

### 3. Producir un artefacto reproducible y con trazabilidad forense

Este objetivo también viene de MINIRONIN. RONIN-10M lo hereda y amplía el archivo: hashes de checkpoints, identidad del holdout, configuración de generación, artefactos y crónica de cambios.

El avance del libro de holdouts es un resultado del **método y del archivo**, no una mejora atribuible a los pesos. La trazabilidad permite comparar sin convertir una impresión narrativa en una puntuación de calidad.

### 4. El archivo del carácter: que el loro diga cosas divertidas

Este objetivo apareció casi accidentalmente en MINIRONIN, aunque el humor y la personalidad no son un adorno: forman parte del propósito central de RONIN-10M. En RONIN-10M los tics han aparecido mucho antes: «El patrón» dominó 96/100 salidas a 5k; a 10k dejó de aparecer y surgieron «ni puta idea» (16/100) y «impacto» (19/100).

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
