import PyPDF2

def extract_text(filepath):

    text = ""

    with open(filepath, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content

    return text