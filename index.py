import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import pytesseract
from PIL import Image
import cv2
import numpy as np


def preprocess_image(image_path):
    """Cargar y mejorar la imagen para OCR."""
    print(f"Intentando cargar la imagen desde: {image_path}") #agregado
    image = cv2.imread(image_path)
    if image is None: #agregado
        print("Error: La imagen no se pudo cargar.") #agregado
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 11, 2)
    return gray

def extract_text(image_path):
    """Extrae texto de una imagen usando OCR."""
    processed_image = preprocess_image(image_path)
    if processed_image is None: #agregado
        return "" #agregado
    text = pytesseract.image_to_string(processed_image, lang='spa')  # Español
    return text

if __name__ == "__main__":
    image_path = "C:\\Users\\fmontes\\Documents\\bot_ordenes\\336210_0.jpg"  # Reemplazar con la ruta real de la imagen
    extracted_text = extract_text(image_path)
    print("Texto extraído:")
    print(extracted_text)