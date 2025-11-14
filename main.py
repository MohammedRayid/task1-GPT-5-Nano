from openai import OpenAI
import PyPDF2
client = OpenAI()

with open("Cats.pdf", "rb") as pdf_file:
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.pages[0]
    page_content = page.extractText()


response = client.moderations.create(
    model="omni-moderation-latest",
    input=[
        {"type": "text", "text": page_content},
    ],
)

print(response)
