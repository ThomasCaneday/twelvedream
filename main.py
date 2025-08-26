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