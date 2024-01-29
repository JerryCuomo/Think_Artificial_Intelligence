# Source: "Think Artificial Intelligence" by Jerry Cuomo, 2024
# Purpose: Educational code examples from the book.
# Copyright © 2024 Jerry Cuomo. All rights reserved.
#
# This code was autogenterated by GPT-4, from the following prompt
# Prompt: Prompt: Use 'en_core_web_sm' to replace 'ORG' entities in 'climatebert-climate-detection.csv' with '[ANONYMIZED]', save updated data to 'anonymized_dataset.csv'.
#
# About: This script anonymizes organization names in a text dataset using spaCy's NLP model
# and then saves the modified data to a CSV file.
#
# Setup: Python installed, with 'climatebert-climate-detection.csv' in your directory. 
# Install pandas and spaCy using 'pip install pandas spacy', then download the 
# spaCy model 'python -m spacy download en_core_web_sm'

import spacy
import pandas as pd

# Load the dataset
data = pd.read_csv('datasets/climatebert-climate-detection.csv')

# Load a pre-trained NLP model
nlp = spacy.load('en_core_web_sm')  # Efficient small English model

# Anonymize organization names directly within the DataFrame
for idx, text in enumerate(data['text']):
    doc = nlp(text)
    anonymized_text = text
    for ent in doc.ents:
        if ent.label_ == 'ORG':  # Identify organization entities
            anonymized_text = anonymized_text.replace(ent.text, '[ANONYMIZED]')
    data.at[idx, 'text'] = anonymized_text  # Update the text with anonymized version

# Save the anonymized dataset without the index
data.to_csv('anonymized_dataset.csv', index=False)
