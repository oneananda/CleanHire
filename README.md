# CleanHire

**CleanHire** helps interviewers detect and prevent candidate malpractice during live technical interviews. It uses behavioral tracking, clipboard monitoring, typing analysis, and AI-powered code originality checks to ensure a fair hiring process.

---

## 🚀 Features (MVP)

- 🎯 **Real-Time Monitoring**
  - Typing pattern analysis (speed, burst, pause)
  - Copy/paste detection
  - Tab switching & window blur detection (via Chrome Extension)

- 🧠 **AI Code Originality Analysis**
  - Detects suspicious or plagiarized code using AI
  - Compares with known solutions and coding patterns

- 🎤 **Voice Behavior Tracking**
  - Mic mute/unmute analysis (optional)
  - Silence patterns post-question

- 📊 **Session Risk Report**
  - Generates post-interview summary
  - Malpractice risk score (Low / Medium / High)
  - Logs suspicious events for reviewer audit

---

## 🧩 Architecture

```bash
cleanhire/
├── backend/        # API, AI models, code analysis
├── frontend/       # React-based dashboard for interviewers
├── extensions/     # Chrome extension for client-side monitoring
├── plugins/        # (Optional) Integrations with Zoom, HackerRank, etc.
├── docs/           # Setup, API references, architecture notes
````

---

## 🛠️ Tech Stack

* **Frontend**: React + Tailwind CSS
* **Backend**: FastAPI (Python) / Node.js (optional)
* **Database**: PostgreSQL / MongoDB
* **AI/NLP**: OpenAI / HuggingFace models
* **Browser Monitoring**: JavaScript (Chrome Extension)
* **Authentication**: OAuth2 (Google, GitHub)

---

## 📦 Installation (Local Dev)

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/cleanhire.git
   cd cleanhire
   ```

2. **Set up the backend**

   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

3. **Run the frontend**

   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. **Install Chrome Extension (Dev Mode)**

   * Go to `chrome://extensions/`
   * Enable Developer Mode
   * Load `extensions/chrome/` as an unpacked extension

---

## 📄 Roadmap

* ✅ MVP: Session logging, AI code checker, risk scoring
* 🔜 Video/audio fingerprinting for voice-based interviews
* 🔜 SaaS version for integration into interview platforms
* 🔜 Interview replay with flagged segments

---


