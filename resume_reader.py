from pypdf import PdfReader


def read_resume(file_name):
    text=''
    if file_name.lower().endswith('.txt'):
        with open(file_name,'r') as file:
            text=file.read()
        if not text.strip():
            raise ValueError('File is empty')
    
    elif file_name.lower().endswith('.pdf'):
        try:
            reader = PdfReader(file_name)
        except Exception:
            raise ValueError('File is empty')
        for page in reader.pages:
            text+=page.extract_text() or ''
        if not text.strip():
            raise ValueError('File is empty')
    else:
        raise ValueError('Unsupported file type')
    return text
