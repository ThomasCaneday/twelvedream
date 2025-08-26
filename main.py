import cv2

desktop_camera = 0
iphone_camera = 1
camera = cv2.VideoCapture(iphone_camera)

if not camera.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        # Capture a single frame
        ret, frame = camera.read()
        if not ret:
            print("Error: Could not read frame from camera.")
            break
        
        cv2.imshow("Press 's' to capture, 'q' to quit", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            cv2.imwrite('captured_image.jpg', frame)
            print("Image captured and saved as 'captured_image.jpg'")
            break
        elif key == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()

from PIL import Image
import pytesseract

# Open the captured image
image = Image.open('captured_image.jpg')

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text:")
print(text)
print("-------------------- End of Extracted Text --------------------")


import os
from dotenv import load_dotenv
from openai import OpenAI

# load variables from .env into environment
load_dotenv()

# get the API key
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-4o-mini",
    input=f"You are a narrative designer. Your task is to take a passage of text from a book and distill it into a single clear story beat. A story beat is a short, vivid summary of the core event, action, or emotional turning point that moves the story forward. Guidelines: Focus only on the key moment (not all details), Keep it short: 1-3 sentences, Make it visual and evocative, so it can be imagined as a scene for an image or short video, Emphasize action, emotion, and setting over exposition. Here is the passage: {text} Now, provide the story beat:"
)

print(response.output_text)
beat = response.output_text

import base64, time

os.makedirs("generated", exist_ok=True)
img = client.images.generate(model="gpt-image-1", prompt=beat, size="1024x1024")
png = base64.b64decode(img.data[0].b64_json)
path = f"generated/beat_{int(time.time())}.png"
with open(path, "wb") as f: f.write(png)