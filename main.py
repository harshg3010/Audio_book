import pyttsx3
import PyPDF2

# Open the PDF file
book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)  # Updated class for PyPDF2 ≥ 2.0
pages = len(pdfReader.pages)        # Get total number of pages
print(f"Total Pages: {pages}")

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Optional: Set voice rate and voice type
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 150)  # Default is usually ~200

voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)  # voices[0] = male, voices[1] = female (may vary by system)

# Read and speak from page 7 to end
for num in range(0, pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    if text:  # Only speak if there's extractable text
        print(f"Reading page {num + 1}...")
        speaker.say(text)
        speaker.runAndWait()

# Close the PDF file
book.close()
