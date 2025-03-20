from PyPDF2 import PdfReader
from gtts import gTTS

user = "YOUR DESKTOP USERNAME"

pdf_file = f'C:\\Users\\{user}\\Desktop\\tts_test.pdf'    #link to pdf


reader = PdfReader(pdf_file)
page = reader.pages[0]
extracted_text = page.extract_text()


tts = gTTS(extracted_text)
tts.save('C:\\Users\\dzemo\\Desktop\\tts_test.mp3')

