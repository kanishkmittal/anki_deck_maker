import genanki
import os
import re

# Initialize lists to hold the tuples
questions_tuple = []

# Read the file
with open('chapter2.txt', 'r') as file:
    data = file.read()

# Split into blocks based on separators
blocks = data.split('---------\n')

# Regex patterns to extract question, tag, and answer
question_pattern = r'Question:\n(.+?)\n'
tag_pattern = r'Tag: (.+?)\n'
answer_pattern = r'Answer:\n(.+?)(?=\n\n|\Z)'

# Iterate over each block and extract information
for block in blocks:
    question = re.search(question_pattern, block, re.S)
    tag = re.search(tag_pattern, block, re.S)
    answer = re.search(answer_pattern, block, re.S)
    
    if question and tag and answer:
        # Clean up the strings
        question_clean = question.group(1).strip()
        tag_clean = tag.group(1).strip()
        answer_clean = answer.group(1)  # Remove the strip() method to retain formatting

        # Append the tuple to the list
        questions_tuple.append((question_clean, tag_clean, answer_clean))


################################################################################

# Unique IDs for the model and the deck
my_model_id = 1607392319
my_deck_id = 2059400110

# Define the Anki model without the image component
my_model = genanki.Model(
  my_model_id,
  'Simple Model without Image',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '<div style="font-size: 20px; font-family: Arial;">{{Question}}</div>',
      'afmt': '{{FrontSide}}<hr id="answer"><div style="font-size: 20px; font-family: Arial;">{{Answer}}</div>',
    },
  ],
  css='.card { font-family: arial; font-size: 20px; text-align: center; color: black; background-color: white;}'
)

# Create the deck
my_deck = genanki.Deck(
  my_deck_id,
  'Chapter 2 Deck'
)

# Add cards to the deck
for question, answer, tag in questions_tuple:
    # Create a new note with the model
    answer = answer.replace(' ', '_')
    note = genanki.Note(
        model=my_model,
        fields=[question, tag],
        tags=[answer]  # Add tags this way
    )
    my_deck.add_note(note)

# Save the deck to a file
genanki.Package(my_deck).write_to_file('outpu2.apkg')

print("Deck has been created and exported as output.apkg.")
