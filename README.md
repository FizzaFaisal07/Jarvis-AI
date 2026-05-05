# 🤖 Jarvis Voice Assistant (Python)

A smart AI-powered voice assistant built using Python that can listen, understand, and respond to user commands. It can perform tasks like opening applications, telling time, answering questions, solving math problems, and more.

---

## 🚀 Features

* 🎤 Voice recognition using microphone
* 🔊 Text-to-speech responses
* 🌐 Open websites (YouTube, Google, etc.)
* 🧠 AI-powered answers using WolframAlpha
* 📚 Wikipedia summaries
* 😂 Random joke generator
* ⏰ Tells current time
* 💻 Opens Visual Studio Code
* 🧮 Solves basic math expressions
* 🔍 Fallback Google search

---

## 🛠️ Technologies Used

* Python
* SpeechRecognition
* pyttsx3
* WolframAlpha API
* Wikipedia API
* PyJokes

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/FizzaFaisal07/Jarvis-AI.git
cd Jarvis-AI
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install SpeechRecognition pyttsx3 wikipedia wolframalpha pyjokes pyaudio
```

---

## 🔑 Setup

### WolframAlpha API Key

1. Go to https://developer.wolframalpha.com/
2. Create an account
3. Get your App ID
4. Replace in code:

```python
WOLFRAM_APP_ID = "YOUR_APP_ID"
```

---

## ▶️ Run the Assistant

```bash
python AI_Assistant.py
```

---

## 🎙️ Example Commands

* "What is the time"
* "Open YouTube"
* "Open VS Code"
* "Tell me a joke"
* "2 + 5"
* "Who is Elon Musk"
* "How are you"
* "Exit"

---

## ⚠️ Requirements

* Python 3.7+
* Microphone
* Internet connection

---

## 🧠 How It Works

1. Listens using microphone
2. Converts speech to text
3. Processes commands
4. Uses:

   * Regex → Math
   * WolframAlpha → Smart answers
   * Wikipedia → Summaries
   * Google → Fallback
5. Responds using voice

---

## 📌 Notes

* If microphone is not working → check permissions
* If `pyaudio` fails:

```bash
pip install pipwin
pipwin install pyaudio
```

* Update VS Code path if needed:

```python
VS_CODE_PATH = "your_path_here"
```

---

## 💡 Future Improvements

* GUI (Tkinter / React)
* Chat history
* Wake word detection ("Hey Jarvis")
* WhatsApp / Email integration
* Smart home automation

---

## 👨‍💻 Author

**Fizza Faisal**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
