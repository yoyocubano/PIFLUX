# 📖 PIF NARRATIVES: The Installer's Adventure

Welcome, young Sparks apprentices. Today we are not going to "wire an exam", today we are going to give life to a Cabin. Imagine that the cabin is a human body and you are the surgeons who will give it veins, nerves, and a heart.

---

## 🏗️ Act 1: The Skeleton and the Veins (Infrastructure)

Before touching a single cable, we need roads.
Imagine your hollow cabin. You have to install **Ducts (Canaletas)**.
*   **The Analogy:** They are like the main arteries. If they are small, the cables suffocate (and heat up). If they are crooked, the energy flows "ugly".
*   **The Mission:** Fix the ducts straight, using the level. These are the highways where our electrons will travel. Remember: Aesthetics is the first rule of a good electrician!

---

## 💡 Act 2: The Eyes of the Cabin (Mixed Lighting)

Here we are going to create a smart light circuit, but without chips. We want the light to turn on if you want it (Switch) OR if someone enters (Sensor).

**The Players:**
1.  **Va et Vient (Two-way Switch):** Two switches talking to each other. Like two doormen in a long hallway; either can open the door.
2.  **The Motion Detector:** The all-seeing eye.

**The Connection (The "Challenge"):**
> *"Connected with two-way switch and motion detector at the same time"*

Here is the narrative trick:
Imagine the Light Bulb is the King. The King wants light.
*   The **Two-way Switches** are his manual advisors. If you give the order, the light turns on.
*   The **Detector** is his bodyguard. If it sees an intruder, it turns on the light.
*   **The Wiring:** Normally, the detector is connected in PARALLEL to the return of the switches (or controls the circuit independently). If EITHER of the two (Switches OR Detector) lets current pass, Let there be light!
    *   *Technical note:* Phase to the detector and common switches. The return of both goes to the lamp.

---

## 🤖 Act 3: The Digital Brain (KNX)

Now we get modern. Forget the thick power cables for control.
We are going to install a **Light Controlled by KNX**.

*   **The Muscle (Actuator):** It hides in the distribution board. It's a relay, but with a brain. It cuts and opens the current for the bulb (230V).
*   **The Nerve (Green Cable):** A thin, green cable running through the cabin. NO electricity flows here to burn, only INFORMATION.
*   **The Order:** When you press the KNX button on the wall, you send a "Telegram" (an SMS) through the green cable that says: *"Hey Actuator 1, activate"*. And click, there is light.
*   **Analogy:** Before (conventional) you had to go and turn on the bulb yourself. Now (KNX), you send a WhatsApp to your butler (Actuator) to do it.

---

## 🔔 Act 4: The Voice (The Bell)

A doorbell is noisy, but delicate. It works at low voltage (usually 8V or 12V), but our network is 230V.
*   **The Wizard (Transformer):** This little device lives in the board. It takes the dangerous 230V (a lion) and converts them into harmless 12V (a kitten).
*   **The Circuit:** Phase and Neutral enter the Wizard (Primary). Two thin wires exit (Secondary) towards the door button and the bell. Never mix the lion with the kitten in the same tube without separation!

---

## 🦾 Act 5: The Beast (The Motor)

Here we need brute force. We are going to run a line to a **Secondary Board**.
There lives The Beast: An Electric Motor.

**The two faces of the Beast:**
1.  **Power Circuit (Force):** Three thick cables (L1, L2, L3) feeding the motor's muscles. They pass through fuses, contactor, and thermal relay.
2.  **Control Circuit (Command):** Thin cables. It's the brain telling the contactor "Close!". Here are your start/stop buttons.

**Power Control:**
We will use a system so it doesn't start abruptly (maybe Star-Delta or a Variable Frequency Drive). Imagine waking a giant; if you do it suddenly, he breaks the bed. If you wake him gently, he gets up calmly.

---

## 🫀 Act 6: The Heart (Central Board and Protections)

Everything arrives here. To the **Central Electric Board**.
Here live the guardians.

**The Guardians:**
1.  **The General (Main Switch):** The supreme boss. If he pulls the lever, everything dies. Total safety.
2.  **The Judge (RCD - Residual Current Device):**
    *   His job is to see if current is escaping (if someone is getting electrocuted).
    *   **GOLDEN RULE OF THIS CABIN:** The Judge is strict with Sockets. Because that's where you plug in metallic things you touch.
    *   **THE EXCEPTION (Your Mission):** LIGHTING circuits are agile and fly high. The client (the exam) has said: *"Lighting circuits DO NOT pass through the differential"*.
    *   *Why?* (Narrative): So that if a defective toaster trips the differential, you aren't left in the dark in the cabin! The light must always remain on to see the exit. (Note: This is a specific rule of this scenario, at home we usually protect everything).

**The Treasure Map (Distribution):**
*   Phase and Neutral bars on top.
*   **Row 1:** Light Breakers (Direct, without passing through the Judge Differential).
*   **Row 2:** 30mA Differential $\to$ Socket Breakers (Protected by the Judge).

---

## 🌟 Mission Summary

You are going to build a living body:
1.  **Veins** hard (ducts).
2.  **Eyes** alert (Two-way + Detector).
3.  **Reflexes** digital (KNX).
4.  **Voice** soft (Bell).
5.  **Muscles** strong (Motor in its own secondary cage).
6.  **Heart** smart (Central Board) that knows how to separate Light (survival) from Force (work), protecting what you touch and keeping on what you see.

Get to work, sparks! ⚡
