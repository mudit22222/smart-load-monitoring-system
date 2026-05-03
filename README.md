# ⚡ Smart Electrical Load Monitoring System

## 🚀 Overview
This project is an IoT-based system designed to monitor real-time electrical load using an ESP32 microcontroller. It measures voltage and current, calculates power consumption, and transmits the data to a backend server for storage and visualization.

The system is built using a rapid prototyping approach (breadboard-based hardware setup) to validate design concepts efficiently.

---

## ⚡ Features
- Real-time voltage and current monitoring  
- Power calculation (P = V × I)  
- Wireless data transmission using WiFi  
- Backend data logging using SQL  
- Interactive dashboard for visualization  
- Scalable architecture for industrial applications  

---

## 🏗️ System Architecture

ESP32 → Sensors → WiFi → Flask Backend → SQL Database → Dashboard

---

## 🔌 Hardware Components
- ESP32 Microcontroller  
- Current Sensor (CT Sensor / ACS712)  
- Voltage Divider Circuit (for voltage sensing)  
- Breadboard-based prototyping setup  
- Connecting wires & power supply  

---

## 🧠 Software Stack
- Embedded C (ESP32 firmware)  
- Python (Flask backend)  
- SQLite (database)  
- Streamlit (dashboard visualization)  

---

## ⚡ Power Calculation

Power (Watts) = Voltage (V) × Current (A)

The system performs real-time power estimation to monitor electrical load behavior and detect anomalies.

---

## 📊 Dashboard
The dashboard provides:
- Real-time voltage, current, and power trends  
- Historical data visualization  
- Tabular representation of recent readings  

---

## 🎯 Applications
- Industrial load monitoring  
- Energy consumption analysis  
- Smart electrical systems  
- Predictive maintenance systems  
- Site commissioning validation  

---

## ▶️ How to Run

### 1. ESP32 Firmware
- Upload the code to ESP32 using Arduino IDE  
- Configure WiFi credentials  

### 2. Backend Server
```bash
pip install -r requirements.txt
python app.py
