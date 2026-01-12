# PIFQU 2017-2018,2019,2020,2021,2022,2023,2024

**40 fuentes**

Estas fuentes constituyen una guía técnica integral sobre electricidad industrial, centrada en el funcionamiento y cálculo de sistemas monofásicos y trifásicos. Los textos detallan fórmulas esenciales para determinar la potencia (activa, reactiva y aparente), la intensidad de corriente y la eficiencia en dispositivos como motores, transformadores y hornos. Además, se exploran conceptos avanzados de automatización mediante el software LOGO!, incluyendo el uso de funciones lógicas, temporizadores y esquemas de automantenimiento. El material también aborda normativas de seguridad eléctrica, métodos de conexión en estrella y triángulo, y la importancia de corregir el factor de potencia. Finalmente, se incluyen ejercicios prácticos y analogías pedagógicas para facilitar la comprensión de fenómenos como la impedancia y la caída de tensión.

---

## Martes, 23 de diciembre

### Explicación de Conexión Estrella-Triángulo
La conexión estrella y triángulo son los dos métodos fundamentales para configurar los devanados de un motor trifásico o cualquier receptor de tres fases, permitiendo adaptar el equipo a las tensiones de la red eléctrica.

**1. Conexión Estrella (Y)**
En esta configuración, un extremo de cada uno de los tres devanados (denominados U2, V2, W2) se une en un punto común, también llamado punto neutro o estrella. Los otros tres extremos libres se conectan a las fases de la red (L1, L2, L3).
*   **Relación de Tensión:** La tensión que soporta cada bobinado (tensión de fase, $U_{ph}$) es la tensión de la red ($U_L$) dividida por $\sqrt{3} \approx 1,732$. Por ejemplo, en una red de 400 V, cada bobina recibe aproximadamente 230 V.
*   **Relación de Corriente:** La corriente que circula por la línea ($I_L$) es igual a la corriente que circula por cada fase del motor ($I_{ph}$).
*   **Uso común:** Se utiliza para arrancar motores en tensiones altas o como el primer paso del arranque estrella-triángulo para reducir la intensidad de arranque.

**2. Conexión Triángulo (Δ)**
En la conexión en triángulo, el final de un devanado se conecta al principio del siguiente (U2 con V1, V2 con W1, W2 con U1), formando un bucle cerrado. Las fases de la red se conectan a los vértices de este triángulo.
*   **Relación de Tensión:** Cada bobinado soporta la tensión compuesta total de la red ($U_L = U_{ph}$). Si la red es de 400 V, cada bobina recibe los 400 V completos.
*   **Relación de Corriente:** La corriente de línea es $\sqrt{3}$ veces mayor que la corriente que circula por cada bobinado ($I_L = \sqrt{3} \cdot I_{ph}$).
*   **Uso común:** Es la conexión de trabajo normal para motores cuya tensión nominal del bobinado coincide con la tensión entre fases de la red.

**Diferencias clave y Potencia:**
*   **Potencia Total:** Si se conectan tres resistencias idénticas, la potencia absorbida en configuración triángulo es tres veces superior a la absorbida en estrella ($P_\Delta = 3 \cdot P_Y$).
*   **Compatibilidad (Placa de características):** Un motor con placa 230/400V debe conectarse en estrella si la red es de 400 V, ya que sus bobinas solo soportan un máximo de 230 V. Si se conectara en triángulo a 400 V, los bobinados recibirían demasiada tensión y se dañarían.
*   **Arranque Estrella-Triángulo:** Maniobra clásica para evitar picos excesivos de corriente. El motor inicia en estrella (consumiendo menos corriente y entregando menos par) y, tras unos segundos, cambia a triángulo para trabajar a su potencia nominal.

> **Analogía para consolidar el concepto:**
> Imagina que los bobinados del motor son como personas en una mesa compartiendo comida. En la conexión estrella, las personas comparten las raciones, por lo que cada una recibe una porción pequeña (230V); esto es ideal si las personas tienen poca capacidad. En cambio, en la conexión triángulo, cada persona tiene su propia pizza entera (400V) delante; esto solo funciona si las personas son "gigantes" y tienen capacidad para comerse la pizza completa sin enfermar.

---

## Sábado, 3 de enero

### Explica la fórmula para calcular resistencias
Para calcular la resistencia eléctrica (R), que se define como la oposición total que presenta un circuito al paso de la corriente, se utiliza principalmente la Ley de Ohm.

**1. La Ley de Ohm (Fórmula Básica)**
$$R = \frac{V}{I}$$
*   R: Resistencia en ohmios (Ω).
*   V: Voltaje/Tensión en voltios (V).
*   I: Corriente/Intensidad en amperios (A).

**2. Relación con la Potencia**
Dependiendo de los datos disponibles:
*   Con voltaje y potencia: $$R = \frac{V^2}{P}$$
*   Con potencia y corriente: $$R = \frac{P}{I^2}$$

**3. Resistencias en Serie y Paralelo**
*   **En Serie:** $R_{eq} = R_1 + R_2$ (Ej: 20 + 30 = 50 Ω).
*   **En Paralelo:** $R_{eq} = \frac{R_1 \cdot R_2}{R_1 + R_2}$ (Ej: 20 y 30 en paralelo = 12 Ω).

**4. Aplicación en Sistemas Trifásicos**
*   En conexión estrella equilibrada, tensión de fase $U_{ph} = \frac{U_L}{\sqrt{3}}$.
*   Resistencia por fase: $R = \frac{U_{ph}}{I_{ph}}$.

> **Analogía:**
> Imagina que la corriente eléctrica es agua fluyendo por una tubería. El voltaje es la presión que empuja el agua y la resistencia es el grosor de la tubería o cualquier obstrucción (como un filtro). Para saber qué tan "estrecha" u obstruida está la tubería (resistencia), solo necesitas observar cuánta presión aplicas (voltaje) y cuánta agua sale finalmente (corriente). Si con mucha presión sale poca agua, la resistencia es muy alta.

---

### Fórmulas para calcular potencia
**1. Fórmulas Básicas (Ley de Watt - CC)**
*   $P = V \cdot I$
*   Con resistencia: $P = I^2 \cdot R$ o $P = \frac{V^2}{R}$.

**2. Potencia en Corriente Alterna Monofásica**
*   **Potencia activa:** $P = V \cdot I \cdot \cos\varphi$

**3. Potencia en Sistemas Trifásicos** (Fundamental para industria)
*   **Potencia Activa (P):** Trabajo útil (W o kW). Fórmula: $P = \sqrt{3} \cdot U_L \cdot I_L \cdot \cos\varphi$.
*   **Potencia Aparente (S):** Potencia total entregada (VA o kVA). Fórmula: $S = \sqrt{3} \cdot U_L \cdot I_L = \sqrt{P^2 + Q^2}$.
*   **Potencia Reactiva (Q):** Campos magnéticos (VAr). Fórmula: $Q = \sqrt{S^2 - P^2}$.

**4. Potencia y Rendimiento en Motores**
*   **Conversión:** 1 HP = 0,746 kW; 1 kW = 1,341 HP.
*   **Eficiencia ($\eta$):** Si un motor recibe 100 W y tiene $\eta=0.9$, entrega 90 W efectivos.

> **Analogía:**
> Imagina una jarra de cerveza. La **potencia activa (P)** es el líquido real que bebes. La **potencia reactiva (Q)** es la espuma; ocupa espacio pero no te la bebes. La **potencia aparente (S)** es el tamaño total de la jarra necesaria para líquido + espuma. El **factor de potencia ($\cos\varphi$)** es qué tan eficientemente aprovechas el vaso: ¡menos espuma, más cerveza!

---

### El factor de Eficiencia ($\eta$) y Tipo de Conexión
El cálculo preciso de la potencia no es solo teórico, sino necesario para dimensionar protecciones y conductores.

**1. El factor de Eficiencia ($\eta$)**
Representa la capacidad de transformar energía eléctrica en mecánica.
*   Si $\eta=0,9$, de 100 W eléctricos salen 90 W mecánicos.
*   **Fórmula Corriente Motor Trifásico:** $$I = \frac{P}{\sqrt{3} \cdot V \cdot \cos\varphi \cdot \eta}$$

**2. Influencia del Tipo de Conexión**
*   **Estrella (Y):** Menos tensión ($U_{ph} = U_L / \sqrt{3}$), menor corriente de arranque.
*   **Triángulo ($\Delta$):** Tensión plena ($U_{ph} = U_L$), 3 veces más potencia que en estrella.

> **Analogía:**
> La eficiencia ($\eta$) es como el metabolismo de un atleta. Si es 80%, necesita comer 1000 calorías para producir 800 calorías de movimiento. El tipo de conexión es la marcha del coche: **Estrella** es primera (arranque suave, ahorro), **Triángulo** es velocidad de crucero (fuerza máxima, mayor consumo).

---

### Cómo se calcula la eficiencia
La eficiencia eléctrica ($\eta$) mide la relación entre la salida útil y la entrada total.
$$ \eta = \frac{P_{util}}{P_{suministrada}} $$
*   $P_{util}$ (Salida): Potencia en el eje del motor.
*   $P_{suministrada}$ (Entrada): Potencia absorbida de la red.
*   Resultado en % (Ej: 0.9 = 90%).

**Para calcular corriente:**
Si la eficiencia es baja, el motor consume más corriente para el mismo trabajo.
$$ I = \frac{P}{\sqrt{3} \cdot V \cdot \cos\varphi \cdot \eta} $$

> **Analogía:**
> La eficiencia es como un exprimidor de naranjas. Potencia suministrada = total de naranjas. Potencia útil = zumo obtenido. Si el exprimidor es malo (baja eficiencia), desperdicias mucha pulpa y necesitas más naranjas para llenar un vaso.

---

### Fórmulas para calcular corriente y sus usos
**1. Fórmulas Fundamentales**
*   **Ley de Ohm:** $I = V/R$ (Circuitos resistivos).
*   **Ley de Watt:** $I = P/V$ (Electrodomésticos simples).

**2. Corriente en Motores**
*   **Monofásico:** $I = P / (V \cdot \eta \cdot \cos\varphi)$
*   **Trifásico:** $I = P / (\sqrt{3} \cdot V \cdot \eta \cdot \cos\varphi)$

**3. Corriente en Transformadores**
*   **Trifásico:** $I = kVA / (\sqrt{3} \cdot kV)$

**4. Relación según Conexión**
*   **Estrella:** $I_{linea} = I_{fase}$
*   **Triángulo:** $I_{linea} = \sqrt{3} \cdot I_{fase}$

**Usos:** Dimensionamiento de conductores, selección de protecciones, seguridad y detección de fallas.

> **Analogía:**
> La corriente es el caudal de agua. El voltaje es la presión. Las fórmulas son el manual del fontanero para saber qué tan gruesa debe ser la manguera (cable) para que no estalle.

---

### Cálculo de consumo eléctrico
Consumo = Potencia $\times$ Tiempo.
**1. Sistemas Monofásicos:** $P = V \cdot I \cdot \cos\varphi$.
**2. Sistemas Trifásicos:** $P = \sqrt{3} \cdot V_L \cdot I_L \cdot \cos\varphi$.
**3. Factores clave:** Eficiencia ($\eta$) y Valor Eficaz (True RMS) para mediciones reales.
**4. Conversiones:** 1 HP = 0,746 kW.

> **Analogía:**
> El consumo es el gasto de agua. Potencia es qué tan abierto está el grifo (caudal) y Tiempo es cuánto dura abierto. El factor de potencia es como sarro en la tubería (ineficiencia).

---

### Cálculos para costes de consumo eléctrico
Para facturar, se usa la potencia activa absorbida de la red ($P_{red}$).
**1. Potencia total de red:** $P_{red} = P_{util} / \eta$. (¡Importante!)
**2. Fórmula Coste:**
$$ \text{Coste} = P_{red} \text{ (kW)} \cdot \text{Tiempo (h)} \cdot \text{Precio kWh} $$

**Versión Examen Luxemburgo (ILNAS-EN 60364):**
$$ \text{Coste} = \left( \frac{\sqrt{3} \cdot U_L \cdot I_L \cdot \cos\varphi}{1000} \right) \cdot t(h) \cdot \text{Precio} $$
Ó desde potencia eje: Coste = $(P_n / \eta) \cdot t \cdot \text{Precio}$.

> **Analogía:**
> Pagar la cuenta en un restaurante con cocina ineficiente ($\eta$). Pagas por toda la comida que compró el chef ($P_{red}$), no solo la que te comiste ($P_{util}$), porque el desperdicio del chef (pérdidas) corre por tu cuenta.

---

### Fórmulas y conceptos de Frecuencia y Sinusoide
**1. La Sinusoide:** Onda de CA. Inicia en 0, sube a pico (+), baja a 0, baja a pico (-), vuelve a 0.
**2. Amplitudes:**
*   **Valor Pico ($V_p$):** Máximo valor de la cresta. $V_p = V_{RMS} \cdot \sqrt{2}$.
*   **Valor RMS ($V_{RMS}$):** Valor eficaz (lo que mide el multímetro). $V_{RMS} = V_p / \sqrt{2}$.
**3. Frecuencia ($f$):** Ciclos por segundo (Hz).
**4. Velocidad Síncrona ($n$):**
$$ n = \frac{60 \cdot f}{p} \quad \Rightarrow \quad f = \frac{n \cdot p}{60} $$
*   **60:** Factor de conversión seg/min.
*   **$p$:** Pares de polos (Polos totales / 2).

> **Analogía Frecuencia:**
> Latidos del corazón de un deportista. 60 Hz = 60 latidos por segundo.
> **Analogía 60:** El segundero del reloj que traduce latidos/segundo a vueltas/minuto.

---

### Lunes, 5 de enero

### Cálculo de Caída de Tensión (3%)
Normativa Luxemburgo.
**1. Valor admisible:** $\Delta U = 3\% \cdot V_{nominal}$. (Ej: $3\% \cdot 230V = 6.9V$).
**2. Fórmulas reales:**
*   **Monofásico:** $\Delta U = \frac{2 \cdot L \cdot I \cdot \cos\varphi}{\gamma \cdot S}$
*   **Trifásico:** $\Delta U = \frac{\sqrt{3} \cdot L \cdot I \cdot \cos\varphi}{\gamma \cdot S}$
**3. Sección necesaria ($S$):** Despejar S si $\Delta U > 3\%$. $S = \frac{\dots}{\Delta U_{max} \cdot \gamma}$.

> **Analogía:**
> Transportar agua con una manguera muy larga. La fricción roba presión (caída de tensión). Si al final no sale con fuerza (superas el 3%), necesitas una manguera (cable) más ancha.

### Reglas de Coordinación ($I_b, I_n, I_z$)
Seguridad fundamental (ILNAS-EN 60364).
Regla: $$ I_b \le I_n \le I_z $$
1.  **$I_b$ (Empleo):** Corriente real de carga.
2.  **$I_n$ (Nominal protección):** Valor del disyuntor.
3.  **$I_z$ (Capacidad cable):** Límite máximo del cable antes de quemarse.
Explicación: La protección ($I_n$) debe saltar antes de que el cable se queme ($I_z$), pero no debe saltar con el uso normal ($I_b$).

> **Analogía:**
> Llenar una piscina con manguera.
> $I_b$: Caudal necesario.
> $I_z$: Presión máxima antes de que la manguera explote.
> $I_n$: Válvula de seguridad. La válvula debe dejar pasar lo necesario ($I_b$) pero cerrar antes de la explosión ($I_z$).

### Esquemas de Potencia y Mando (Paso a Paso)
**1. Potencia (Fuerza):**
*   Líneas L1, L2, L3 $\to$ Protección (-Q) $\to$ Contactor (-K1) $\to$ Relé Térmico (-F4) $\to$ Motor (-MA1).
*   Bornes clave: Contactor (1-2, 3-4, 5-6).

**2. Mando (Control):**
*   Fase $\to$ Relé Térmico NC (95-96, seguridad) $\to$ Pulsador Parada NC (1-2) $\to$ Pulsador Marcha NO (3-4) $\to$ Bobina (A1-A2).
*   **Enclavamiento/Auto-mantenimiento:** Paralelo al pulsador de marcha con contacto auxiliar NO (13-14) del contactor.

> **Analogía:**
> **Potencia:** El caballero y su espada (fuerza bruta). **Mando:** El cerebro que ordena atacar. **Relé Térmico:** El sudor; si hay mucho, el cerebro ordena parar (95-96 abre).

### LECTURA DE TABLA DE RESULTADOS (Examen)
*   **$\Delta V > 3\%$:** Cable muy fino o muy largo. Peligro de mal funcionamiento.
*   **Corrientes:** Verificar $I_b \le I_n \le I_z$. Si $I_{medida}$ es desigual entre fases $\to$ Desequilibrio.
*   **True RMS:** Necesario si hay variadores, si no, la lectura es falsa.

> **Analogía:**
> La tabla es el panel de control. $\Delta V$ es pérdida de presión. Corriente es caudal. Si la tabla dice que pierdes mucha presión, necesitas tubo más grueso.

### KNX: Actuadores vs Sensores
*   **Actuadores (Salidas):** Ejecutan (Relés, Dimmers). Van en cuadro DIN.
*   **Sensores (Entradas):** Detectan (Pulsadores, Detectores). Van en pared/techo.
*   **Direcciones:**
    *   **Física:** DNI del aparato (dónde está, ej: 1.1.5).
    *   **De Grupo:** Idioma/Función (qué hace, ej: "Encender Sala", 0/0/1). Vincula sensor con actuador.
*   **Cableado:** Bus par trenzado (verde) en paralelo, estrella o árbol.

> **Analogía:**
> **Sensores:** Tus ojos/tacto. **Bus:** Nervios. **Actuadores:** Músculos. **Dir. Física:** Tu nombre. **Dir. Grupo:** Una orden común ("¡Salten!") que entienden varios músculos a la vez.

### Lógica Cableada y Conectores
*   **AND (Serie):** Todo debe cumplirse. (Interruptor Y Botón).
*   **OR (Paralelo):** Basta uno. (Botón O Sensor).
*   **Enclavamiento (Interlocking):** Vital para inversión de giro. Contacto NC de K2 en bobina K1. K1 y K2 nunca juntos (Cortocircuito).
*   **Auto-mantenimiento:** Contacto 13-14 en paralelo al marcha. Memoria.

> **Analogía:**
> **AND:** Portero estricto (Invitación Y Etiqueta). **OR:** Portero relajado (Invitación O Amigo del dueño).

---

## RESUMEN GENERAL (Todo lo que debes saber)
**Fórmulas Clave:**
1.  **Ohm:** $V=I \cdot R$
2.  **Potencia Trifásica:** $P = \sqrt{3} \cdot U \cdot I \cdot \cos\varphi$
3.  **Frecuencia:** $f = (n \cdot p) / 60$
4.  **Caída Tensión:** $\Delta U = (k \cdot L \cdot I)/S$
5.  **Coordinación:** $I_b \le I_n \le I_z$

**Ejercicios Típicos Examen:**
1.  **Cálculo de Secciones:** Dado un $\Delta U$ máx, hallar mm².
2.  **Motor:** Hallar corriente nominal y de arranque (Estrella vs Triángulo).
3.  **Costes:** Calcular factura considerando eficiencia ($\eta$).
4.  **Lógica:** Dibujar esquema de mando inversión de giro o automatismo simple.
5.  **Seguridad:** 5 Reglas de Oro y grados IP.

**Instalación Estrella-Triángulo:**
*   Arrancar suave (Estrella, K1+K3).
*   Temporizador cambia a potencia (Triángulo, K1+K2).
*   **NUNCA K2 y K3 juntos (BUM).**

**Motor Monofásico (Steinmetz):**
*   Lleva condensador para crear "tercera fase" falsa. Pierde 30% potencia.

---
*Este documento resume 40 fuentes de conocimiento eléctrico industrial para la preparación de exámenes oficiales en Luxemburgo.*
