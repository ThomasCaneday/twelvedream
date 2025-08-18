import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open camera.")
else:
    # Capture a single frame
    ret, frame = camera.read()
    if ret:
        # Save the captured frame as an image file
        cv2.imwrite('captured_image.jpg', frame)
        print("Image captured and saved as 'captured_image.jpg'")
    else:
        print("Error: Could not capture frame from the camera.")
    
camera.release()
cv2.destroyAllWindows()