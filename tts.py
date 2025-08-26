import os
import time
from dotenv import load_dotenv
from openai import OpenAI

# load variables from .env into environment
load_dotenv()

# get the API key
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
os.makedirs("audio_output", exist_ok=True)
speech_file_path = f"audio_output/speech_{int(time.time())}.mp3"
text="“Once we get Gertie secured,” shouted Savachia, “we'll get below deck and wait it out!” He glanced at Emma, who looked ready to hurl at any second. Green-faced and grim, she kept pulling Gertie’s line in anyway. “The sail’s down!” Alex announced. Pimawa looked through the rain at the sail, securely bundled against the bottom of the mast. He smiled at Alex. “Excellent job! We'll make a sailor of you yet!” Alex’s eyes widened, but not in pride—in fear. “Behind you!” he yelled. Pimawa spun. Out from the foaming depths shot a large, semitransparent turquoise tentacle. It landed with a thud, wrapping itself around the railing and trapping Pimawa’s arm. Pimawa pushed against the rail and tried pulling his paw free. ."

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="coral",
    # input="Today is a wonderful day to build something people love!",
    input=text,
    instructions="Speak in a cheerful and positive tone.",
) as response:
    response.stream_to_file(speech_file_path)
print(f"Audio content written to file '{speech_file_path}'")