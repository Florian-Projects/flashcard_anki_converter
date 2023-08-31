# Analog Flashcard to Anki deck converter

## Description

This is a collection of scripts I wrote to convert some analog flashcards I bought
to an anki deck So I can use spaced repetition in order to prepare for my final exam.

## How to use

1. Intall python (I have used 3.11, some earlier version should still work though)
2. Install the requirements ```pip install -r requirements.txt```
3. Add your pdfs to ```answers``` and ```questions``` directories
4. Run ```python image_extractor```. This will extract the scanned images from the pdf files.
5. Run ```python image_to_text```. This will extract the text from the images
6. Run ```python generate_anki```. This will generate the anki deck from the text files

## Folder Explanation

### ```answers``` and ```questions```

These folder should contain pdf files of the scanned flash cards.
The pdf files should be in a specific order. So you can later map the extracted question the
extracted answers.

### ```answers_img``` and ```questions_img```

These folder contain the extracted images as .png file.
The files are numbered from 0...n and the all other scripts assume that ```answers_img/0.png```
corresponds to ```questions_img/0.png``` and so on.

### ```answers_txt``` and ```questions_txt```

These folders contain the OCR parsed text from the img files
