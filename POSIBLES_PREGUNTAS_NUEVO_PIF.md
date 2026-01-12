# 🔮 POSIBLES PREGUNTAS PARA EL NUEVO PIF (Predicción)

Basado en el análisis de frecuencia de los últimos 7 años, aquí tienes las preguntas más probables para caer en tu próximo examen. ¡Domínalas!

---

## 🚨 Top Probabilidad: Protecciones y Seguridad (Siempre caen)

**1. Calculo de Intensidad de Cortocircuito (Icc) vs Poder de Corte**
*   *Pregunta:* Tienes un disyuntor de 6kA. La Icc calculada en el punto es de 10kA. ¿Es válido?
*   *Respuesta:* No. El poder de corte del disyuntor (6kA) debe ser siempre MAYOR que la Icc posible (10kA), o explotará.

**2. Selectividad Diferencial**
*   *Pregunta:* ¿Cómo aseguras que salte el diferencial del baño (30mA) y no el general de la casa (300mA) ante un fallo en el baño?
*   *Respuesta:* Usando un diferencial general de tipo "Selectivo" (S) y asegurando que su sensibilidad sea al menos 3 veces mayor (300mA vs 30mA).

**3. Zonas de Baño (La pregunta trampa)**
*   *Pregunta:* ¿Puedo poner una toma de corriente a 50cm de la bañera si tiene tapa?
*   *Respuesta:* No, sigue siendo Volumen 2 (0-60cm). Solo permitido tomas de afeitadora con transformador de separación.

---

## ⚡ Top Probabilidad: Motores y Automatismos

**4. Dimensionamiento de Motor**
*   *Pregunta:* Un motor de 10kW, 400V, cos φ 0.85, rendimiento 0.9. Calcule la corriente nominal para ajustar el relé térmico.
*   *Fórmula:* $I = P / (\sqrt{3} \cdot V \cdot \cos\varphi \cdot \eta)$.
*   *Cálculo:* $10000 / (1.732 \cdot 400 \cdot 0.85 \cdot 0.9) = 18.86 A$. Ajustar relé a 19A aprox.

**5. Lógica de Contactores**
*   *Pregunta:* Dibuja el enclavamiento eléctrico para una inversión de giro.
*   *Respuesta:* Debes dibujar un contacto NC de K2 en serie con la bobina de K1, y un contacto NC de K1 en serie con la bobina de K2.

---

## 📐 Top Probabilidad: Cálculos y Cables

**6. Caída de Tensión (El clásico)**
*   *Pregunta:* Tienes una línea de 50 metros, 1.5mm², alimentando 10A a 230V. ¿Cumple la caída de tensión < 3%?
*   *Cálculo:* $\Delta U = (2 \cdot L \cdot I) / (56 \cdot S) = (2 \cdot 50 \cdot 10) / (56 \cdot 1.5) = 11.9 V$.
*   *Límite 3%:* $230 \cdot 0.03 = 6.9 V$.
*   *Respuesta:* **NO cumple** (11.9V > 6.9V). Hay que aumentar sección.

**7. Factor de Corrección de Cables**
*   *Pregunta:* Si paso 3 circuitos juntos por un tubo aislante, ¿el cable aguanta los mismos amperios?
*   *Respuesta:* No. Debes aplicar un factor de corrección (aprox 0.70) porque se calientan mutuamente. El cable aguanta MENOS corriente.

---

## 🤖 Top Probabilidad: Tecnología Moderna (KNX/Smart)

**8. Topología KNX**
*   *Pregunta:* ¿Qué pasa si cierro el bucle en una línea de bus KNX?
*   *Respuesta:* Error de comunicación. La topología debe ser Árbol, Estrella o Línea, pero NUNCA anillo cerrado.

**9. Variador de Frecuencia**
*   *Pregunta:* ¿Cómo reduzco la velocidad de un motor asíncrono a la mitad?
*   *Respuesta:* Reduciendo la frecuencia (Hz) a la mitad mediante un variador. (Recuerda $n = 60f / p$).

**10. Diferencial Tipo B**
*   *Pregunta:* Vamos a instalar un cargador de coche eléctrico. ¿Qué diferencial necesito?
*   *Respuesta:* Tipo B (o Tipo A EV), porque el coche puede inyectar corrientes continuas puras de fallo que dejarían ciego a un diferencial normal AC.
