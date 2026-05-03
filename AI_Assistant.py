import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import wikipedia
import wolframalpha
import pyjokes
import sys
import re

# ================= CONFIG =================
WOLFRAM_APP_ID = "9VHY4G4P2Q"
wikipedia.set_lang("en")

VS_CODE_PATH = os.path.join(
    os.environ['LOCALAPPDATA'],
    "Programs",
    "Microsoft VS Code",
    "Code.exe"
)

# ================= ASSISTANT =================
class JarvisAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 180)

        self.recognizer = sr.Recognizer()
        self.client = wolframalpha.Client(WOLFRAM_APP_ID)

    # ================= SPEAK =================
    def speak(self, text):
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    # ================= LISTEN =================
    def listen(self):
        with sr.Microphone() as source:
            print("\nListening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=6)
            except:
                return "none"

        try:
            print("Recognizing...")
            query = self.recognizer.recognize_google(audio, language='en-US')
            print(f"You: {query}")
            return query.lower()
        except:
            return "none"

    # ================= MAIN =================
    def run(self):
        self.speak("All systems initialized. I am ready.")

        while True:
            query = self.listen()

            if query == "none":
                continue

            # ===== BASIC COMMANDS =====
            if 'time' in query:
                time_now = datetime.datetime.now().strftime("%I:%M %p")
                self.speak(f"The time is {time_now}")

            elif 'open youtube' in query:
                self.speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")

            elif 'open code' in query or 'vs code' in query:
                if os.path.exists(VS_CODE_PATH):
                    self.speak("Opening Visual Studio Code")
                    os.startfile(VS_CODE_PATH)
                else:
                    self.speak("VS Code not found")

            elif 'joke' in query:
                self.speak(pyjokes.get_joke())

            elif 'exit' in query or 'quit' in query:
                self.speak("Goodbye")
                sys.exit()

            # ===== SMART AI =====
            else:
                query_clean = query.strip().lower()

                # 🔹 Fix short names
                if query_clean == "srk":
                    query_clean = "Shah Rukh Khan"

                # 🔹 Casual replies
                if "how are you" in query_clean:
                    self.speak("I'm doing great ⚡ How can I help you?")
                    continue

                if "your name" in query_clean:
                    self.speak("I am Jarvis, your assistant.")
                    continue

                if query_clean in ["ok", "okay", "thanks", "thank you", "got it"]:
                    self.speak("Alright 👍")
                    continue

                # 🔥 1️⃣ MATH FIX
                if re.search(r"[0-9]+\s*[\+\-\*/]\s*[0-9]+", query_clean):
                    try:
                        result = eval(query_clean)
                        self.speak(f"The answer is {result}")
                        continue
                    except:
                        pass

                # 🔥 2️⃣ WOLFRAM (smart answers)
                try:
                    res = self.client.query(query_clean)
                    answer = next(res.results).text

                    # avoid wrong answers like songs
                    if "song" not in answer.lower():
                        self.speak(answer)
                        continue
                except:
                    pass

                # 🔹 3️⃣ Wikipedia
                try:
                    result = wikipedia.summary(query_clean, sentences=2)
                    self.speak(result)
                    continue
                except:
                    pass

                # 🔹 4️⃣ FINAL fallback
                self.speak("I couldn’t find a direct answer. Searching Google.")
                webbrowser.open(f"https://www.google.com/search?q={query_clean}")


# ================= RUN =================
if __name__ == "__main__":
    bot = JarvisAssistant()
    bot.run()