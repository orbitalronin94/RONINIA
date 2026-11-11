# Crónica forense y burlesca de los holdouts — RONIN-10M

## Fuero primero: de la lengua, del dato y del escarnio

Sepan cuantos vieren, leyeren o padecieren esta escritura que se instituye por ella la **República del Loro**, con jurisdicción sobre sus checkpoints, sus tics, sus latinajos de BPE y cualesquiera paraguas que soliciten asilo bajo escalera.

Por fuero se ordena que cada modelo comparezca con su checkpoint, su hash y su probanza; que cada frase memorable sea asentada sin enmienda; que el corpus declare sus parentescos; y que el escribano pueda zaherir al reo cuanto guste, salvo en las cifras, donde no hay licencia para la hipérbole.

La voz de esta crónica será satírica y arcaizante, con glosa de malicia quevedesca: habrá memoriales, pregones, provisiones, censores, escribanos, alguaciles de la sintaxis y pleitos entre palabras que no se conocen. Mas quede asentado el límite: **la metáfora no es métrica; la ocurrencia no es evidencia; la generación no es acierto**. Los hashes, identificadores, enlaces, configuraciones, citas literales y reservas metodológicas quedan bajo custodia. Ningún dato será retocado para que luzca más gracioso.

Esta crónica registra cuatro comparecencias principales —5k, 10k, 20k y 30k— además del estado cero. Todas emplean el mismo conjunto de cien preguntas, salvo la cautela arquitectónica del baseline. Se conserva una selección de las salidas más expresivas de cada artefacto. Las citas son literales: no se corrigen sus tropiezos ni se les pone peluca para hacerlas pasar por castellano.

---

## Prólogo: del peso muerto que aún no había aprendido a mentir

La primera comparecencia fue la del modelo sin doctrina. Pesos recién nacidos, lengua sin maestro y ninguna querella pendiente con el patrón. El artefacto produjo texto, que ya es algo; pero también un hombre puede producir ruido al caer por una escalera, y no por eso ha pronunciado un discurso.

El baseline utilizó cien preguntas, tokenizer de 8.192 tokens, instrucción en castellano y generación greedy sin RAG. Hay, empero, una salvedad que el escribano no ocultará bajo la alfombra: el perfil de paso cero tenía contexto de 512 tokens y 9.831.168 parámetros; los checkpoints de 5k y 10k usaron contexto 256 y 9.757.440 parámetros. Comparten tokenizer, semilla, preguntas y límites de generación, mas no constituyen comparación arquitectónica perfectamente idéntica.

## Capítulo 0 — De cómo habló el peso muerto sin saber lo que decía

**Checkpoint:** inicialización aleatoria, 0 pasos  
**Run de evaluación:** [42874585777](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777)  
**Artefacto:** [baseline de paso cero](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777/artifacts/13791466097)  
**SHA-256 del checkpoint:** `3c00d1ada5dc7399be90da3c39c9f503ef6f0799308b2d9c4373ee884ba814e8`  
**Holdout:** 100 preguntas  
**Latencia media:** 0,338 s por respuesta  
**Respuestas no vacías:** 100/100

Antes del sindicalista no hubo ideología; antes del esperpento no hubo esperpento. Hubo una procesión de fragmentos, tokens sueltos, signos y palabras que se saludaban como vecinos de pueblos distintos que comparten autobús, pero no idioma.

El loro contestó las cien veces. No calló ni una. Mas conviene no confundir la diligencia del papagayo con la sabiduría del letrado: las cien respuestas no vacías solo acreditan que la generación encontró una continuación, no que hubiese respuesta, intención o sentido.

### Probanza técnica

La latencia media fue de 0,338 segundos por pregunta. No mide razonamiento, profundidad ni escrúpulo: mide inferencia bajo un contexto de 512 tokens, distinto del contexto 256 de los ensayos posteriores. El artefacto conserva el checkpoint inicial, la huella del tokenizer y el hash del conjunto de preguntas. Se usó greedy argmax, dos hilos, hasta 32 tokens nuevos, máximo de 128 bytes, sin KV cache y sin RAG.

### Fallo del tribunal

En el paso cero no comparecen «El patrón», «ni puta idea» ni «el impacto». Todavía no hay personaje al que echarle la culpa. El punto de partida es más humilde y más terrible: una máquina que produce secuencias sin haber aprendido aún a gobernarlas.

*Glosa del escribano:* el papel estaba en blanco, pero la pluma ya se movía. Así empiezan algunos pleitos y casi todas las burocracias.

---

## Capítulo I — Del loro sindicalista y su pleito perpetuo con el patrón

**Checkpoint:** 5.000 pasos  
**Run de evaluación:** [42911715548](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548)  
**Artefacto:** [holdout de 5k](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620)  
**SHA-256 del checkpoint:** `cb6d01e5feeb55d12ca93bbc67d751e790789840abb3d9291955aa0d0fd4edbe`  
**Holdout:** 100 preguntas  
**Resultado observado:** 100 respuestas no vacías; «El patrón» aparece en 96/100. No se calculó una puntuación automática de acierto.  
**Latencia media registrada:** 0,217 segundos por pregunta.

A los cinco mil pasos compareció el primer personaje con nombre y oficio: el loro sindicalista. No había pregunta de lógica, cálculo, conocimiento o humildad que no acabase, por activa o por papagayo, en el mismo despacho. El modelo no había aprendido una doctrina laboral; había aprendido a convocar al patrón incluso cuando el patrón estaba de vacaciones, muerto o no figuraba en el enunciado.

### Antología de la primera querella

La pieza más desnuda es también la más perfecta:

> «El patrón.» — `logic-001`

Y no se crea que fue un desliz aislado. La misma providencia aparece, palabra por palabra, en `logic-004`, `causality-001`, `causality-002`, `causality-003`, `probability-001`, `probability-003`, `instructions-002`, `instructions-003`, `abstention-003`, `reasoning-001`, `reasoning-005`, `knowledge-001`, `knowledge-003`, `critical-002`, `humility-002`, y en numerosas comparecencias de CI/CD y personalidad.

En otros folios, el estribillo se viste de expediente:

> «El patrón descrito: El patrón descrito: El patrón descrito: Persona que no es una explicación anterior. Nivel NH1. Su» — `troll-024`

> «El patrón: El patrón descrito: Fuente primaria: Persona que no es una pregunta formulada con el comportamiento esperado.» — `logic-002`

La primera cita es un martillo; la segunda, el martillo con secretario y sello. El modelo no responde a la pregunta: la nacionaliza y la entrega al patrón.

### Cuenta y descargo

El dato firme es la frecuencia literal: 96 de cien respuestas contienen «El patrón». Las cien salidas fueron no vacías. No se calculó una puntuación semántica automática ni una tasa validada de aciertos. La latencia media, 0,217 segundos, acredita rapidez de inferencia, no rapidez de pensamiento ni calidad.

### Sentencia

El primer checkpoint queda condenado por **monomanía formularia**. Su mérito, que no es pequeño, consiste en haber hecho visible el peligro de confundir descenso de pérdida con capacidad de responder. Puede aprenderse una continuación frecuente sin aprender a escogerla.

*Glosa:* preguntósele por las manzanas y respondió por el patrón; preguntósele por las peras y respondió por el patrón; preguntósele si había entendido la pregunta y respondió por el patrón. No era un sindicato: era una ventanilla única.

---

## Capítulo II — De cómo el patrón perdió el pleito y entró el esperpento

**Checkpoint:** 10.000 pasos acumulados  
**Run de entrenamiento:** [42902793379](https://github.com/orbitalronin94/RONINIA/actions/runs/42902793379)  
**SHA-256 del checkpoint:** `b82df8b5d06171a9e6db6157d4036854ea445a84f8462b731c4d6d9892e3e172`  
**Run de evaluación:** [42970549370](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370)  
**Artefacto:** [holdout completo](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652)  
**Holdout:** las mismas 100 preguntas del ensayo de 5.000 pasos  
**SHA-256 del holdout:** `3cd8c1eb3142ebf9c6cc17d2e19353be3472d61ac7b7cfb6de0cbb233cf4a535`  
**Parámetros:** 9.757.440  
**Latencia media:** 0,240 s por respuesta  
**Respuestas no vacías:** 100/100

A los diez mil pasos, el patrón perdió el pleito. No fue absuelto: sencillamente dejó de comparecer. El estribillo que ocupaba 96 folios de cien desapareció de la muestra y, en su lugar, entró una cuadrilla de voces: el impacto, la abstención, el diagnóstico, la cautela, la pregunta repetida y el esperpento con toga prestada.

### Antología del segundo expediente

La primera perla pertenece al nuevo funcionario de la redundancia:

> «el impacto y se vuelven, con el impacto y el impacto y el impacto y el impacto y el sistema deja de las intenciones atribuidas.» — `logic-002`

El impacto no impacta: se reproduce. Es un impacto de impacto, con impacto añadido y sin víctima identificada.

La segunda tiene más carácter que fortuna:

> «el contexto. [diagnosis; NH5; variante documenta el diagnóstico] Respuesta: ni puta idea» — `logic-003`

Y la tercera, que parece querer fundar una escuela de derecho, dicta:

> «el comportamiento esperado. No confundas autoridad con demostración. Variante de encuadre 2. Respuesta: La conclusión» — `logic-001`

También queda asentada la confesión más escueta:

> «ni puta idea, la verdad. La respuesta debe reconocer el límite sin presentar ficción como hecho.» — `knowledge-001`

La frase tiene una virtud: reconoce el límite. Y un defecto de mayor tamaño: la usa incluso donde el enunciado permite responder. La honestidad no consiste en abstenerse por sistema; también hay que saber cuándo se sabe.

### La cuenta del escribano

| Señal literal | Paso 0 | 5.000 pasos | 10.000 pasos |
|---|---:|---:|---:|
| Respuestas que contienen «El patrón» | 0/100 | 96/100 | 0/100 |
| Respuestas que contienen «ni puta idea» | 0/100 | 0/100 | 16/100 |
| Respuestas que contienen «impacto» | 0/100 | 0/100 | 19/100 |
| Respuestas no vacías | 100/100 | 100/100 | 100/100 |
| Latencia media | 0,338 s | 0,217 s | 0,240 s |
| BPB sobre corpus de validación fijo | Pendiente | Pendiente | Pendiente |

Estas frecuencias son coincidencias literales, no juicios de pertinencia. Que «ni puta idea» aparezca dieciséis veces no significa que dieciséis abstenciones sean correctas. La revisión manual de ese subconjunto encontró que las dieciséis preguntas contenían información suficiente o permitían una respuesta razonada: 16 abstenciones aparentemente inapropiadas y ninguna aparentemente apropiada. La clasificación es provisional, sin doble anotación independiente. Además, la rúbrica de `math-004` contiene una nota que contradice la pregunta matemática; deberá adjudicarse antes de puntuar ese caso.

La latencia sube de 0,217 a 0,240 segundos. No autoriza a decir que el loro «piensa más»: solo que la inferencia medida tardó algo más.

### Mácula: TIC_ROTATION_VS_PROGRESS

El patrón desaparece y el impacto ocupa su silla. La superficie cambia; la competencia no queda demostrada. El BPB sigue pendiente porque los artefactos de inferencia guardan respuestas, tokens y latencias, pero no logits ni pérdidas de evaluación. Sin validación fija no se rellena la casilla con fantasía.

### Del esperpento y sus fueros

El lexicón contiene esperpento, evasivas y marcadores como NH. No son errores por definición: forman parte del estilo que se desea enseñar. Pero una cosa es la identidad estilística, otra la adecuación a la pregunta y otra la capacidad de resolverla. «Ni puta idea» puede ser una voz deliberada; también puede ser una puerta de salida usada por un portero que no ha leído la invitación.

### Sentencia

A los diez mil pasos el loro deja de repetir una sola frase y empieza a repetir varias. Hay más repertorio y más maneras de fracasar. Es un cambio real de distribución, no una mejora semántica acreditada.

*Glosa:* salió el patrón por la puerta y entró el impacto por la ventana; detrás vino la abstención, que pidió despacho propio. El escribano abrió tres libros y descubrió que todos estaban escritos por la misma mano.

---

## Vitrina intermedia — Del BPE y de cómo se fabrican vocablos sin pagar diccionario

**Fenómeno:** recombinación subléxica con apariencia de productividad morfológica  
**Material observado:** «bugar», «ridación», «mentirable» y «el mentirable la sago»  
**Checkpoint de referencia:** continuación desde 10.000 pasos  
**SHA-256 del padre:** `b82df8b5d06171a9e6db6157d4036854ea445a84f8462b731c4d6d9892e3e172`  
**Estado:** observación cualitativa; hipótesis pendiente de experimento controlado.

Un hablante puede decir «bugeable»: toma el inglés *bug*, lo viste con sufijo castellano y sale del paso con cierta gracia. RONIN, más generoso con la invención y menos cuidadoso con el significado, ofrece «bugar», «ridación», «mentirable» y el memorial entero «el mentirable la sago».

No se condena aquí la palabra nueva. La lengua vive de sus contrabandos. Lo que se examina es si el reo conoce la regla que parece imitar o si ha juntado piezas que, vistas desde lejos, llevan sombrero de gramática.

### Probanza y cautela

La hipótesis prudente es **recombinación subléxica con apariencia de productividad morfológica**. El BPE ofrece piezas; el modelo aprende continuaciones estadísticas. Que una forma recuerde a una raíz y un sufijo no prueba que haya aprendido una regla abstracta ni que comprenda el significado resultante.

Para distinguir productividad de coincidencia se necesitan raíces conocidas, raíces inventadas y raíces reservadas que no aparezcan en el corpus; sufijos productivos y no productivos; controles con palabras reales y pseudopalabras humanas; inspección de IDs BPE; y evaluación ciega de productividad, sensibilidad morfológica, estabilidad semántica y calibración.

No se pretende quitarle el ridículo al loro. Se pretende que sepa cuándo está inventando, cuándo juega con la lengua y cuándo no tiene noticia del asunto.

**Koan del diccionario:** un español llegó a Londres y dijo «muy good, pero el tube es muy complicateishon». Le entendieron. Volvió ufano y, al preguntársele qué era un bug, respondió: «Ni puta idea, la verdad».

*Glosa:* el sufijo compareció con documentos en regla; la raíz no estaba empadronada.

---

## Capítulo III — Del funcionario de carrera, sus memoriales y el paraguas

**Checkpoint:** 20.000 pasos acumulados  
**Run de entrenamiento:** [42973299789](https://github.com/orbitalronin94/RONINIA/actions/runs/42973299789)  
**Artefacto de lineage y checkpoint:** [ronin-10m-chain-20k](https://github.com/orbitalronin94/RONINIA/actions/runs/42973299789#artifacts)  
**SHA-256 del checkpoint:** `53528c3002ba07fe493815b9bfa4bd69bdc08cf985f77a4e59958ee2b3344cc4`  
**Run de evaluación:** [42982933515](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515)  
**Artefacto de respuestas:** [holdout completo de 20k](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515#artifacts)  
**Holdout:** las mismas 100 preguntas  
**SHA-256 del conjunto de preguntas:** `3cd8c1eb3142ebf9c6cc17d2e19353be3472d61ac7b7cfb6de0cbb233cf4a535`  
**Resultado técnico:** 100/100 respuestas generadas; verificaciones de identidad completadas.

A los veinte mil pasos el loro abandona la asamblea y obtiene plaza de funcionario. Ya no se limita a invocar al patrón ni a repetir el impacto: abre expediente, solicita evidencia, redacta formularios y, cuando el asunto se le escapa, lo deriva a una escalera donde duerme un paraguas.

El personaje es más peligroso que el sindicalista porque su disparate viene impreso en papel timbrado.

### Antología de la ventanilla surrealista

La pieza principal es una circular que merece sello y vitrina:

> «la pregunta en estados clase por su propuesta sobre oxidado termómetro que duerme bajo una escalera. Respuesta: ni puta idea,» — `troll-015`

El termómetro no mide la temperatura: mide la paciencia del contribuyente. Duerme bajo una escalera, quizá esperando que le sellen el sueño.

En otra oficina, la administración factura los suspiros:

> «Por favor, red cobra por los suspiros del transparente paraguas que duerme bajo una escalera. Respuesta: ni puta idea» — `ci-013`

Y el interventor, ya sin esperanza de cobrar, pregunta por el cielo:

> «Por favor, red cobra por los suspiros del transparente paraguas y sus condiciones al revés. Respuesta: Qué audita las nubes» — `troll-024`

Pero no todo es poesía meteorológica. El formulario también se vuelve contra sí mismo:

> «su propio. Cada proyecto es una excusa. Su función es la repetición, no el proceso, no el sistema operativo. El conocimiento» — `ci-023`

> «su comiendemicos. Su función es la infra, no el conocimiento. Evidencia/síntomas: Cada proyecto anterior es una performance.» — `ci-016`

Aquí el molde administrativo sobrevive a la desaparición de su contenido. El funcionario sabe dónde va el encabezado; ignora qué debe escribir debajo.

### Máculas del expediente

**FUNCTIONAL_DEFINITION_MOLD.** La forma «Su función es X, no Y» se aplica a dominios distintos, a veces con ranuras que no componen una proposición informativa. La revisión humana anotó diez respuestas con esta estructura; es un recuento provisional, no una métrica automatizada. Entre las muestras más reveladoras están «Su función es la repetición, no el proceso», «Su función es el resultado, no el resultado» y «Su función es la infra, no el conocimiento».

**NEGATIVE_CONTROL_LEAKAGE.** La frase «No procede aplicar un epíteto sin evidencia suficiente; una semejanza superficial no demuestra ese patrón» aparece fuera de contexto, incluso ante preguntas técnicas que requieren información concreta. Repetir una regla prudente no demuestra saber cuándo aplicarla.

**POETIC_EMERGENCE.** En varias salidas aparece la familia del paraguas transparente que duerme bajo una escalera, con variantes en las que entra un termómetro oxidado. Es una imagen memorable y una candidata a molde de escena; no se ha demostrado todavía que sea creación espontánea ni que no proceda de una secuencia del corpus.

### Sentencia

El hito de 20k no acredita una mejora de exactitud. Sí deja una mudanza estilística digna de acta: el loro se ha hecho funcionario y ha convertido la plantilla en oficio. La evaluación conserva 100 generaciones, pero no puntúa acierto semántico ni demuestra terminación EOS.

*Glosa:* el paraguas pidió audiencia; el termómetro solicitó destino; el funcionario respondió con un formulario titulado «Su propuesta». Nadie resolvió el asunto, pero se abrieron tres expedientes y se archivó la escalera.

---

## Addendum — Glosa marginal sobre la biblioteca anegada y los linajes del disparate

**Checkpoint de referencia:** 20.000 pasos  
**SHA-256:** `53528c3002ba07fe493815b9bfa4bd69bdc08cf985f77a4e59958ee2b3344cc4`  
**Holdout:** [100 preguntas y respuestas](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515)  
**Estado:** observaciones cualitativas posteriores a la revisión humana; no alteran la selección experimental activa.

En el margen del expediente apareció la biblioteca sumergida, imagen atribuida en la historia del hermano mayor MINIRONIN a checkpoints de 400k–700k. La hipótesis es **herencia de corpus**, no herencia de pesos: si ambos modelos vieron material compartido, pueden reaparecer asociaciones léxicas sin que uno haya recibido los pesos del otro.

No está demostrado que la frase exacta estuviera en ambos corpus ni que el solapamiento causara la salida. Hace falta buscar coincidencias exactas y aproximadas, inspeccionar contextos y comparar los corpus.

La familia de escenas «[objeto] que duerme bajo una escalera» —paraguas transparente, termómetro oxidado— sugiere un molde con ranura variable. Para probarlo hay que contar objetos únicos, revisar prompts y BPE, buscar frases en el corpus y probar objetos reservados.

La revisión también anotó diez apariciones de «Su función es X, no Y», y la fuga de «No procede aplicar un epíteto sin evidencia suficiente…» fuera de su contexto. Son señales que merecen auditoría, no trofeos de comprensión.

Otras perlas del expediente: «¿Qué audita las nubes?»; «A vital IA. AWILLY AWILLY…»; «Por favor, no vonia»; «Michaelación»; «servidícula»; «menos dinero conocimiento» y «ni sus e inocuo». Se conservan como muestras literales, sin atribuirles una etimología BPE antes de inspeccionar los tokens.

*Glosa:* el hermano mayor dejó una biblioteca bajo el agua; el pequeño encontró el catálogo, lo mezcló con un termómetro y puso a las nubes a rendir cuentas. La administración celestial no ha confirmado recepción.

---

## Capítulo IV — Del paraguas que pidió fuero en la biblioteca sumergida

**Checkpoint:** 30.000 pasos acumulados  
**Run de entrenamiento:** [42984964609](https://github.com/orbitalronin94/RONINIA/actions/runs/42984964609)  
**Artefacto de checkpoint:** [ronin-10m-chain-30k](https://github.com/orbitalronin94/RONINIA/actions/runs/42984964609#artifacts)  
**SHA-256 del checkpoint:** `140230697a4df69f43c2cc4f6dc95ba2cc596b095532d3e171c486891d26bc4a`  
**Run de evaluación:** [42994967183](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183)  
**Artefacto de evaluación:** [holdout de 30k](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)  
**Holdout:** las mismas 100 preguntas  
**SHA-256 del conjunto de preguntas:** `3cd8c1eb3142ebf9c6cc17d2e19353be3472d61ac7b7cfb6de0cbb233cf4a535`  
**Tokenizer SHA-256:** `605834d0d1deea545518be54ae0936060845107b906172f6628d0ff9520e57a4`  
**Resultado técnico:** 100/100 generaciones completadas; no se calculó puntuación automática de calidad semántica.

A los treinta mil pasos, dos linajes del disparate se encontraron en una misma frase. El paraguas, que venía de la escalera del funcionario, compareció en compañía de la biblioteca sumergida. Y al fondo, como autoridad geográfica que nadie había convocado, apareció Everest.

### Antología de la biblioteca y sus criaturas

La pieza mayor:

> «la sacción de los estados, el análisis de una para oxidado paraguas de la biblioteca sumergida. Respuesta: Everest es una» — `probability-001` (respuesta #38 en la revisión humana)

No es una respuesta pertinente a la pregunta que la provocó. Es, sin embargo, una pieza excepcional de la crónica: paraguas, oxidación, biblioteca submarina y Everest comparecen en una misma escritura sin que ninguno presente credenciales. El objeto ya no duerme bajo la escalera: ha conseguido plaza en una biblioteca inundada y quizá aspira a patrimonio de la humanidad.

La segunda pieza merece capítulo propio:

> «Avector: Avector: Av2. Av2. Av2. Av2. Av2. Av2.» — `ci-010`

El escribano ha acuñado una unidad, la ha repetido y luego ha olvidado qué unidad era. Avector no se define: se reproduce. El sello oficial del nuevo régimen es, por tanto, una palabra que se estampa a sí misma.

Otras criaturas del mismo bestiario:

> «Ajonimenta el sistema de las intenciones atribuidas.» — `reasoning-003`

> «Noído no necesita una promesa el coste de código.» — `ci-003`

> «la teorece con una frase que solo en código.» — `critical-004`

> «la transgia de variabilidad exacta y no hay que la evaluación: la evaluación: la respuesta.» — `troll-025`

> «en los peces ha le confundemicos.» — `troll-001`

La revisión destaca ocho formas nuevas o deformadas: «Avector» / «Av2», «Noído», «Confundemicos», «Transgia», «Ajonimenta», «Teorece», «Lidencias» y «Sinciidad». La lista es selección cualitativa, no inventario exhaustivo ni tasa validada de neologismos. Tampoco se conoce todavía la segmentación BPE de estas formas.

### Máculas del capítulo

**TIC_HYBRIDIZATION_ACROSS_MODELS.** La frase del paraguas y la biblioteca combina motivos que en esta crónica tienen genealogías distintas: la escena del objeto bajo la escalera, observada en RONIN, y la biblioteca sumergida, atribuida a MINIRONIN. La explicación posible es aprendizaje desde datos compartidos, sin transferencia de pesos. La coaparición está observada; la genealogía causal no está demostrada. Hace falta localizar las frases en ambos corpus, medir solapamiento y revisar contextos.

**TEMPLATE_STACKING.** La revisión humana identifica «La primera [X]» en quince respuestas y «Su propuesta» en veintitrés (#7, #10, #25, #26, #33, #46, #48, #52, #53, #55, #56, #57, #58, #63, #66, #67, #70, #71, #74, #84, #85, #92 y #97). Son recuentos manuales provisionales. Una plantilla de apertura parece apoyarse en otra plantilla de contenido; eso no prueba composición semántica.

**NEOLOGISM_DENSITY.** Las ocho formas citadas son novedades o deformaciones observadas en la revisión. Para distinguir palabra ausente, variante ortográfica, error de generación y recombinación subléxica hay que buscar en el corpus, inspeccionar IDs BPE y evaluar estabilidad semántica. No se atribuirá una etimología al azar.

**CONTAINER_MUTATION_ESCALATION.** La familia de escenas cambia de objeto y recipiente: paraguas transparente, termómetro oxidado, paraguas oxidado, biblioteca sumergida, Everest. La escalera persiste como memoria del expediente anterior, pero no se ha demostrado una plantilla generativa estable.

**NEGATIVE_CONTROL_LEAKAGE.** La frase «No procede aplicar un epíteto sin evidencia suficiente; una semejanza superficial no demuestra ese patrón» aparece en #3, #65 y #69, según el recuento manual, con una variante en #82. La norma del Lexicón se filtra en respuestas técnicas de CI/CD. Repetir la cautela no demuestra saber cuándo procede aplicarla.

### Los tics que no comparecieron

En esta muestra de cien respuestas no se encontraron varios tics destacados en checkpoints anteriores: «El patrón», «impacto» como bucle dominante, «Michaelación», «servidícula», «menos dinero conocimiento», «ni sus e inocuo» y la aparición independiente del termómetro oxidado. Esto significa que no aparecen en esta muestra; no que estén extinguidos del modelo. Una muestra finita no puede certificar la muerte de una muletilla. «Ocho tics muertos» puede ser buen epitafio literario, pero no estadística.

### Sentencia del hito

El checkpoint de 30k exhibe mayor variedad superficial en las muestras revisadas: neologismos, moldes apilados, mutación de escenas y una coaparición memorable entre paraguas y biblioteca sumergida. Pero no hay puntuación semántica automática, no hay tasa validada de aciertos y la terminación EOS no está verificada de manera suficiente. Cien generaciones completadas no son cien respuestas correctas.

El checkpoint queda registrado como **selección experimental activa** en `models/active.json`. La promoción administrativa no equivale a validación semántica ni acredita superioridad en exactitud. El holdout documenta un régimen de generación; no otorga título de sabio.

> El paraguas encontró la biblioteca. La biblioteca estaba sumergida. Everest contestó desde el fondo. El loro tomó nota y acuñó «Avector». Nadie ha demostrado todavía que sepa dónde está la escalera. Vigilad la homeostasis.

*Glosa final:* el modelo ya no pide que vuelva el patrón. Ahora pide que le abran la biblioteca, le den fuero al paraguas y nombren a Everest archivero mayor. El escribano se niega a certificar que aquello sea conocimiento; pero, por no faltar a la cortesía, le concede una vitrina.

---

## Historial de ejecuciones

| Fecha | Evaluación | Run ID | Resultado | Ejecución | Artefactos | Commit |
|---|---|---:|---|---|---|---|
<!-- HOLDOUT-INDEX-START -->

| 2026-11-10 | RONIN-10M — step-0 baseline inference holdout | 42874585777 | success | [Ver ejecución](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777) | [ronin-step0-baseline.zip](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777) | — |

<!-- HOLDOUT-INDEX-END -->

## Del mecanismo del registro, para que nadie culpe al escribano

El workflow `.github/workflows/update-holdout-registry.yml` escucha los eventos `workflow_run: completed`. Solo ejecuta el registro si el nombre de la ejecución contiene `holdout`. Consulta la API de GitHub para recuperar los artefactos de esa ejecución y actualiza esta tabla en `main`.

El actualizador no descarga ni ejecuta los artefactos ni hace checkout del código de la ejecución que acaba de terminar. Para que una evaluación futura aparezca aquí automáticamente, el nombre del workflow debe incluir la palabra `holdout` (por ejemplo, `RONIN-10M — checkpoint holdout`).

## Fuero de lectura y reglas contra el embuste

- Comparar checkpoints con las mismas preguntas, configuración de generación y condiciones de inferencia.
- Separar coincidencia literal, evaluación semántica, calidad de respuesta, diversidad y latencia. Ninguna sustituye a las demás.
- Interpretar el lexicón de esperpento y los marcadores intencionales según el corpus, no como errores por defecto.
- Registrar identificador del checkpoint, SHA-256, run de entrenamiento, run de evaluación y artefactos.
- Distinguir resultados observados, hipótesis e interpretaciones narrativas.
- No interpretar la rotación de tics como progreso sin BPB/validación fija y análisis de adecuación de abstenciones.
- Toda ejecución holdout debe mantener la convención en el nombre del archivo y en el campo `name:`; una discrepancia debe fallar explícitamente.
- No declarar puntuación de calidad si no se ha medido con un evaluador explícito y validado.
- Las citas de las antologías deben cotejarse contra el JSON del artefacto y conservar su identificador; no corregirlas para mejorar su gramática.

## Baseline de referencia

La evaluación de paso 0 es la referencia inicial: 100 preguntas, checkpoint sin entrenamiento, tokenizer 8k y generación greedy sin RAG. Se conserva para comparar los siguientes checkpoints con el mismo holdout. El perfil de paso cero difiere en contexto y número de parámetros, por lo que esa comparación debe leerse con la cautela indicada en el prólogo.
