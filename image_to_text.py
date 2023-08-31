import os
from PIL import Image
from pytesseract import image_to_string


def extract_text_from_image(image_name, question_dir, answer_dir):
    question_img = Image.open(f"{question_dir}/{image_name}")
    answer_img = Image.open(f"{answer_dir}/{image_name}")

    question = image_to_string(question_img, lang="deu")
    answer = image_to_string(answer_img, lang="deu")

    with open(f"./questions_txt/{image_name.replace('.png', '.txt')}", "w") as file:
        file.write(question)
    with open(f"./answers_txt/{image_name.replace('.png', '.txt')}", "w") as file:
        file.write(answer)


def main():
    question_img_dir = "./questions_img"
    answers_img_dir = "./answers_img"
    os.makedirs("questions_txt", exist_ok=True)
    os.makedirs("answers_txt", exist_ok=True)
    file_names = os.listdir(question_img_dir)

    for image_name in file_names:
        if not image_name.endswith(".png"):
            continue

        extract_text_from_image(image_name, question_img_dir, answers_img_dir)


if __name__ == "__main__":
    main()
