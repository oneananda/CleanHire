# 🔊 Audio Pattern Observer (APO) — CleanHire MVP

**Audio Pattern Observer** is a lightweight, non-invasive module for CleanHire that passively monitors and logs real-time audio patterns. It’s designed to run silently in the background, providing foundational insights into voice activity and environmental audio without interacting with any user applications.

---

## 📦 Features

- ✅ Passive audio monitoring (input/output)
- 🎤 Voice activity detection (via WebRTC VAD)
- 📈 Volume level tracking (RMS/peak)
- 🕒 Timestamped event logging (silent / speaking)
- 📝 Local export (JSON/CSV)
- 💻 CLI toggle for start/stop

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- `pip` package manager

### Installation

```bash
git clone https://github.com/cleanhire.git
cd audio-pattern-observer
pip install -r requirements.txt
````

### Run the Observer

```bash
python observer.py
```

Optional flags:

```bash
python observer.py --output logs/session1.json --duration 300
```

---

## 🧪 Sample Output

```json
[
  {
    "timestamp": "2025-06-15T14:32:10Z",
    "state": "speaking",
    "volume": 0.72
  },
  {
    "timestamp": "2025-06-15T14:32:15Z",
    "state": "silent",
    "volume": 0.05
  }
]
```

---

## 🛠️ Tech Stack

* **Language:** Python
* **Audio I/O:** `pyaudio`, `sounddevice`
* **Voice Activity Detection:** `webrtcvad`
* **Logging:** Standard I/O, JSON/CSV

---

## 🧩 CleanHire Integration

This module is a foundational component of CleanHire's environment analysis layer. Future integration points will allow CleanHire to:

* Correlate voice activity with interview timelines
* Flag potential engagement gaps or disruptions
* Score environmental clarity (background noise)

---

## 📂 Project Structure

```
audio-pattern-observer/
│
├── observer.py               # Main audio monitoring script
├── vad_utils.py              # Voice activity detection helpers
├── logger.py                 # Logging and data output
├── requirements.txt
└── README.md
```

---

## 📄 License

MIT License © 2025 CleanHire

```

---
