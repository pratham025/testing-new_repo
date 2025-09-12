import time
import pyttsx3
from datetime import datetime
import keyboard

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty(
    'rate',
    170
)

def speak_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    engine.say(f"The time is {current_time}")
    engine.runAndWait()

print("Talking Clock Started ⏰ (Press CTRL+C to stop)")

keyboard.add_hotkey("ctrl+alt+t", speak_time)

# Keep running until ESC is pressed
keyboard.wait("esc")

