from openai import OpenAI
import PyPDF2
import json
client = OpenAI()


# Process PDF and extract text
with open("prompt.pdf", "rb") as pdf_file:
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.pages[0]
    page_content = page.extractText()

# Pass through moderation module
response = client.moderations.create(
    model="omni-moderation-latest",
    input=[
        {"type": "text", "text": page_content},
    ],
)

moderation = json.load(response)
if response.results.flagged != False:
        result = client.responses.create(
        model="gpt-5-nano",
        input= page_content
    )
#else:
#      return 
# { "allowed": false, "flag": "<category>" }
print(response.output_text)


