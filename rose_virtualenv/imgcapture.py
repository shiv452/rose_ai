import cv2
import pytesseract
import webbrowser

# Set the path to the Tesseract executable (change this to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

def capture_image():
    # Use OpenCV to capture an image from the camera
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return frame

def extract_text_from_image(image):
    # Use pytesseract to extract text from the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.strip()

def search_online(query, search_engine):
    # Perform a search on the specified search engine
    url = f"https://www.{search_engine}.com/search?q={query}"
    webbrowser.open(url)

def main():
    # Capture image from the camera
    image = capture_image()

    # Extract text from the captured image
    text = extract_text_from_image(image)

    print("User said:", text)

    # Perform searches on various platforms
    search_online(text, "google")
    search_online(text, "amazon")
    search_online(text, "flipkart")

if __name__ == "__main__":
    main()
