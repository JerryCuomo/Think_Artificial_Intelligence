# Source: "Think Artificial Intelligence" by Jerry Cuomo, 2024
# Purpose: Educational code examples from the book.
# Copyright © 2024 Jerry Cuomo. All rights reserved.
#
# Prompt: Create a Python script to generate synthetic health records using Faker for personal details 
# and statistical methods for health-related data.
#
# This script generates a synthetic health record dataset and saves it to a CSV file. It uses the Faker library 
# to generate personal information and statistical methods for health-related data.
#
# Setup: Python installed with Faker. Install using 'pip install Faker'.

import pandas as pd
from faker import Faker
import numpy as np
import random

faker = Faker()

def generate_health_record(num_records):
    records = []

    for _ in range(num_records):
        record = {
            'Patient Name': faker.name(),
            'Date of Birth': faker.date_of_birth(),
            'Address': faker.address(),
            'Blood Type': random.choice(['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']),
            'Heart Rate (bpm)': np.random.normal(70, 10),
            'Blood Pressure': f"{np.random.randint(90, 140)}/{np.random.randint(60, 90)}",
            'Allergies': faker.word(ext_word_list=['None', 'Penicillin', 'Nuts', 'Latex', 'Pollen']),
            'Medication': faker.word(ext_word_list=['None', 'Aspirin', 'Insulin', 'Metformin', 'Lisinopril'])
        }
        records.append(record)

    return pd.DataFrame(records)

# Generate 100 synthetic health records
synthetic_data = generate_health_record(100)

# Save the generated data to a CSV file
output_file = 'synthetic_health_records.csv'
synthetic_data.to_csv(output_file, index=False)
print(f"Data saved to {output_file}")