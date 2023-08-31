import os
import io
import PyPDF2
from PIL import Image

image_counter = 0


def extract_images_from_pdf(pdf_path, output_folder, counter=0, reverse_counting=False):
    with open(pdf_path, "rb") as file:
        # Create a PDF reader object
        pdf = PyPDF2.PdfReader(file)

        # Loop through all the pages in the PDF
        for page_num, page in enumerate(pdf.pages):
            # Check if the page contains any images
            if '/XObject' in page['/Resources']:
                xObject = page['/Resources']['/XObject'].get_object()

                for obj in xObject:
                    if xObject[obj]['/Subtype'] == '/Image':
                        try:
                            data = xObject[obj]._data
                            image = Image.open(io.BytesIO(data))
                            image.save(f"{output_folder}/{counter}.png")
                            if not reverse_counting:
                                counter += 1
                            else:
                                counter -= 1
                        except Exception as e:
                            print(f"Error extracting image on page {page_num + 1}, object {obj}: {e}")

        return counter


def main():
    questions_pdf_dir = "./questions"
    answers_pdf_dir = "./answers"
    question_img_dir = "./questions_img"
    answers_img_dir = "./answers_img"

    # I needed the counter because the order of cards was reversed.
    # Therefore I needed to reverse the counter in between. My answer pdf are also in incorrect order
    # if your pdfs are correct than you can just keep increasing the counter and then set it to 0 when extracting
    # the answer and pass reverse_counting = False to the extraction function
    counter = 0

    for filename in os.listdir(questions_pdf_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(questions_pdf_dir, filename)

            os.makedirs(question_img_dir, exist_ok=True)
            counter = extract_images_from_pdf(pdf_path, question_img_dir, counter)

    # specific for my case
    reverse_counter = 154
    for filename in os.listdir(answers_pdf_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(answers_pdf_dir, filename)

            os.makedirs(answers_img_dir, exist_ok=True)
            extract_images_from_pdf(pdf_path, answers_img_dir, reverse_counter, True)
            reverse_counter = counter - 1


if __name__ == "__main__":
    main()
