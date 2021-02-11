import pytesseract


def OCR(data):
    results = pytesseract.pytesseract.image_to_string(
        pytesseract.pytesseract.Image.open(data))
    # for line in results.split('\n'):
    #     print(line)

    return results
