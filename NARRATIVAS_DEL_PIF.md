# 📖 NARRATIVAS DEL PIF: La Aventura del Instalador

Bienvenidos, jóvenes aprendices de la Chispa. Hoy no vamos a "cablear un examen", hoy vamos a dar vida a una Cabina. Imaginad que la cabina es un cuerpo humano y vosotros sois los cirujanos que le van a dar venas, nervios y corazón.

---

## 🏗️ Acto 1: El Esqueleto y las Venas (Infraestructura)

Antes de tocar un solo cable, necesitamos carreteras.
Imagina tu cabina hueca. Tienes que instalar **Canales (Canaletas)**.
*   **La Analogía:** Son como las arterias principales. Si son pequeñas, los cables se asfixian (y se calientan). Si están torcidas, la energía fluye "fea".
*   **La Misión:** Fija las canaletas rectas, usando el nivel. Son las autopistas por donde viajarán nuestros electrones. Recuerda: ¡La estética es la primera regla de un buen electricista!

---

## 💡 Acto 2: Los Ojos de la Cabina (Iluminación Mixta)

Aquí vamos a crear un circuito de luz inteligente, pero sin chips. Queremos que la luz se encienda si tú quieres (Interruptor) O si alguien entra (Sensor).

**Los Jugadores:**
1.  **Va et Vient (Vaivén):** Son dos interruptores que hablan entre sí. Como dos porteros en un pasillo largo; cualquiera puede abrir la puerta.
2.  **El Detector de Movimiento:** El ojo que todo lo ve.

**La Conexión (El "Challenge"):**
> *"Conectado con va y vient y detector de movimiento al mismo tiempo"*

Aquí está el truco narrativo:
Imagina que la Bombilla es el Rey. El Rey quiere luz.
*   Los **Va y Vient** son sus consejeros manuales. Si tú das la orden, la luz se enciende.
*   El **Detector** es su guardaespaldas. Si ve un intruso, enciende la luz.
*   **El Cableado:** Normalmente, el detector se conecta en PARALELO al retorno de los interruptores (o controla el circuito independientemente). Si CUALQUIERA de los dos (Interruptores O Detector) deja pasar corriente, ¡Hágase la luz!
    *   *Nota técnica:* Fase al detector y a los interruptores comunes. El retorno (vuelta) de ambos va a la lámpara.

---

## 🤖 Acto 3: El Cerebro Digital (KNX)

Ahora nos ponemos modernos. Olvida los cables gruesos de fuerza para controlar.
Vamos a instalar una **Luz Controlada por KNX**.

*   **El Músculo (Actuador):** Está escondido en el cuadro. Es un relé, pero con cerebro. Él corta y abre la corriente de la bombilla (230V).
*   **El Nervio (Cable Verde):** Un cable fino, verde, que recorre la cabina. Por aquí NO pasa electricidad para quemar, solo INFORMACIÓN.
*   **La Orden:** Cuando pulsas el botón KNX en la pared, envías un "Telegrama" (un SMS) por el cable verde que dice: *"Oye Actuador 1, actívate"*. Y clac, se hace la luz.
*   **Analogía:** Antes (convencional) tenías que ir tú a encender la bombilla. Ahora (KNX), le mandas un WhatsApp a tu mayordomo (Actuador) para que lo haga.

---

## 🔔 Acto 4: La Voz (El Timbre)

Un timbre es ruidoso, pero delicado. Funciona a baja tensión (normalmente 8V o 12V), pero nuestra red es de 230V.
*   **El Mago (Transformador):** Este pequeño aparato vive en el cuadro. Toma los 230V peligrosos (un león) y los convierte en 12V inofensivos (un gatito).
*   **El Circuito:** Fase y Neutro entran al Mago (Primario). Salen dos hilos finos (Secundario) hacia el pulsador de la puerta y el timbre. ¡Nunca mezcles al león con el gatito en el mismo tubo sin separación!

---

## 🦾 Acto 5: La Bestia (El Motor)

Aquí necesitamos fuerza bruta. Vamos a sacar una línea hacia un **Cuadro Secundario**.
Allí vive La Bestia: Un Motor Eléctrico.

**Las dos caras de la Bestia:**
1.  **Circuito de Potencia (Fuerza):** Tres cables gruesos (L1, L2, L3) que alimentan los músculos del motor. Pasan por fusibles, contactor y relé térmico.
2.  **Circuito de Mando (Control):** Cables finos. Es el cerebro que le dice al contactor "¡Cierra!". Aquí están tus botones de marcha/paro.

**El Control de Potencia:**
Usaremos un sistema para que no arranque de golpe (quizás Estrella-Triángulo o un Variador). Imagina que despiertas a un gigante; si lo haces de golpe, rompe la cama. Si lo despiertas suave, se levanta tranquilo.

---

## 🫀 Acto 6: El Corazón (Cuadro Central y Protecciones)

Todo llega aquí. Al **Cuadro Eléctrico Central**.
Aquí viven los guardianes.

**Los Guardianes:**
1.  **El General (Interruptor de Corte):** El jefe supremo. Si baja la palanca, todo muere. Seguridad total.
2.  **El Juez (Diferencial):**
    *   Su trabajo es ver si la corriente se escapa (si alguien se está electrocutando).
    *   **LA REGLA DE ORO DE ESTA CABINA:** El Juez es estricto con los Enchufes (Circuitos de Tomas). Porque ahí conectas cosas metálicas que tocas.
    *   **LA EXCEPCIÓN (Tu Misión):** Los circuitos de ILUMINACIÓN son ágiles y vuelan alto. El cliente (el examen) ha dicho: *"Los circuitos de iluminación NO pasan por el diferencial"*.
    *   *¿Por qué?* (Narrativa): Para que si una tostadora defectuosa hace saltar el diferencial, ¡no te quedes a oscuras en la cabina! La luz debe permanecer siempre encendida para ver la salida. (Ojo: Esto es una regla específica de este escenario, en casa normalmente protegemos todo).

**El Mapa del Tesoro (Distribución):**
*   Barras de Fase y Neutro arriba.
*   **Fila 1:** Disyuntores de Luz (Directos, sin pasar por el Juez Diferencial).
*   **Fila 2:** Diferencial 30mA $\to$ Disyuntores de Tomas (Protegidos por el Juez).

---

## 🌟 Resumen de la Misión

Vas a construir un cuerpo vivo:
1.  **Venas** duras (canales).
2.  **Ojos** atentos (Vaivén + Detector).
3.  **Reflejos** digitales (KNX).
4.  **Voz** suave (Timbre).
5.  **Músculos** fuertes (Motor en su propia jaula secundaria).
6.  **Corazón** inteligente (Cuadro Central) que sabe separar la Luz (supervivencia) de la Fuerza (trabajo), protegiendo lo que tocas y manteniendo encendido lo que ves.

¡A trabajar, chispas! ⚡
