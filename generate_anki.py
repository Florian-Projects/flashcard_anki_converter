import os
import genanki


def generate_deck():
    # Define a Model for the Anki cards
    my_model = genanki.Model(
        1607392319,  # This is a random model ID
        'Simple Model',
        fields=[
            {'name': 'Title'},
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '<b>{{Title}}</b><br>{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])

    # Path to the questions and answers folders
    questions_path = "questions_txt"
    answers_path = "answers_txt"

    # Ensure both folders exist
    if not os.path.exists(questions_path) or not os.path.exists(answers_path):
        raise ValueError("Both 'questions' and 'answers' folders must exist.")

    # Get list of files in the questions folder
    question_files = os.listdir(questions_path)

    # Create a deck
    my_deck = genanki.Deck(2059400110, "Generated Deck")  # This is a random deck ID

    # Iterate over each file in the questions folder
    for q_file in question_files:
        if not q_file.endswith(".txt"):
            continue
        # Construct the path to the corresponding answer file
        a_file_path = os.path.join(answers_path, q_file)

        # Check if the corresponding answer file exists
        if not os.path.exists(a_file_path):
            print(f"Warning: No answer found for {q_file}. Skipping.")
            continue

        # Read the content of the question and answer files
        with open(os.path.join(questions_path, q_file), 'r') as qf, open(a_file_path, 'r') as af:
            title = os.path.splitext(q_file)[0]
            question_content = qf.read().strip().replace("\n", "<br>")
            answer_content = af.read().strip().replace("\n", "<br>")

        # Create a new Anki note with the content
        my_note = genanki.Note(
            model=my_model,
            fields=[title, question_content, answer_content]
        )

        # Add the note to the deck
        my_deck.add_note(my_note)

    # Generate the Anki package (.apkg file)
    genanki.Package(my_deck).write_to_file('output_deck.apkg')

    print("Deck has been generated as 'output_deck.apkg'.")


if __name__ == "__main__":
    generate_deck()
