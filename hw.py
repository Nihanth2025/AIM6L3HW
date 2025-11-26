import random
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 0.9)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_samples():
    return [
        "Hello! I am your computer!",
        "Python is a great programming language!",
        "This is AI speaking to you!",
        "Welcome to the world of AI!",
        "Never give up on your dreams!",
        "AI is transforming the world!",
        "Speak your thoughts into code!"
    ]

def main():
    print("🎤 VOICE MASTER+")
    speak("Hello! Type something for me to say!")

    while True:
        user_input = input("\n💻 You: ").strip().lower()

        if user_input == "exit":
            speak("Goodbye!")
            break

        elif user_input == "sample":
            phrase = random.choice(get_samples())
            print(f"💬 {phrase}")
            speak(phrase)

        elif user_input == "speed up":
            rate = min(300, engine.getProperty("rate") + 50)
            engine.setProperty("rate", rate)
            speak(f"Speed increased to {rate} rate.")

        elif user_input == "speed down":
            rate = max(50, engine.getProperty("rate") - 50)
            engine.setProperty("rate", rate)
            speak(f"Speed decreased to {rate} rate.")

        elif user_input == "increase volume":
            vol = min(1.0, engine.getProperty("volume") + 0.1)
            engine.setProperty("volume", vol)
            speak(f"Volume increased to {vol:.1f}.")

        elif user_input == "decrease volume":
            vol = max(0.0, engine.getProperty("volume") - 0.1)
            engine.setProperty("volume", vol)
            speak(f"Volume decreased to {vol:.1f}.")

        elif user_input == "tell a joke":
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
                "Why don't skeletons fight each other? They don't have the guts!"
            ]
            joke = random.choice(jokes)
            print(f"😂 {joke}")
            speak(joke)

        elif user_input == "help":
            commands = ["sample", "speed up", "speed down", "increase volume",
                        "decrease volume", "tell a joke", "exit"]
            print("📜 Available commands:", ", ".join(commands))
            speak("Here are the available commands.")

        elif user_input:
            speak(user_input)

        else:
            print("❓ Type 'sample' for a random phrase or 'exit' to quit.")
            speak("I didn't understand that. Please try again.")

if __name__ == "__main__":
    main()