import os.path
import sys
from pdf2image import convert_from_path
from PIL import Image
import pytesseract


# Covert PDF to a list of images
def pdf_to_text(pdf_path):
    images = convert_from_path(pdf_path)

    full_text = []

    for image in images:
        text = pytesseract.image_to_string(image)

        full_text.append(text)
    return "\n".join(full_text)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    extracted_text = pdf_to_text(pdf_path)

    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    text_file_name = f"{base_name}.txt"
    # print(extracted_text)
    with open(text_file_name, 'w', encoding='utf-8') as file:
        file.write(extracted_text)

    print(f"The extracted text has been saved to {text_file_name}")