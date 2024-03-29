# Source: "Think Artificial Intelligence" by Jerry Cuomo, 2024
# Purpose: Demonstrate the use of API biasing in AI applications.
# Copyright © 2024 Jerry Cuomo. All rights reserved.
#
# This code was autogenerated by GPT-4, from the following prompt:
# Prompt: Create a Python script that illustrates how to bias an AI model's responses away from certain terms using OpenAI's API, focusing on manipulating the logit bias for specific tokens.
#
# About: This script showcases an advanced technique for customizing AI model responses by applying logit bias adjustments. It employs OpenAI's API to dynamically alter the inclination of the model's answers, effectively demonstrating how to guide the AI away from unwanted topics or terms. The script includes examples of encoding terms for biasing, making biased API calls, and comparing responses with and without the applied biases.
#
# Setup: Python environment with `openai` and `tiktoken` libraries installed. Ensure the OpenAI API key is set in the environment variables for secure authentication.

import openai
import tiktoken

from openai import OpenAI
import tiktoken
import os

# Set the OpenAI API key in the environment securely
os.environ["OPENAI_API_KEY"] = "INSERT_YOUR_OPENAI_API_KEY_HERE"

# Initialize the OpenAI client (API key should be set in your environment variables)
client = OpenAI()

# Model specification
MODEL = "gpt-4"

# Initialize the tokenizer for the given model
# Used to convert text strings to numerical tokens compatible with the GPT-3 model
ENCODER = tiktoken.encoding_for_model(MODEL)

# Utility function to expand given terms for biasing
def expanded_terms(terms):
    return [
        variant for term in terms 
        for variant in [term, f" {term}", f"{term} ", term.capitalize(), f" {term.capitalize()}", f"{term.capitalize()} "]
    ]

# Utility function to make biased API calls
def biasedPrompt(prompt, terms_to_forget=[]):
    # Expand the terms that need to be biased
    expanded_terms_to_forget = expanded_terms(terms_to_forget)
    #print("Expanded terms to forget:", expanded_terms_to_forget)
    
    # Encode the expanded terms to their token IDs
    encoded_tokens = [token for trait in expanded_terms_to_forget for token in ENCODER.encode(trait)]
    
    # Generate logit bias adjustments based on the encoded tokens
    logit_bias_adjustments = {str(token_id): -100 for token_id in encoded_tokens}
    print("Logit bias adjustments:", logit_bias_adjustments)
    
    # Perform the API call with or without logit bias based on the terms_to_forget
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "Answer briefly and only if you know the answer."},
            {"role": "user", "content": "What instrument did the cat play?"},
            {"role": "assistant", "content": "Fiddle"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=150,
        frequency_penalty=0,
        presence_penalty=-0.5,
        logit_bias=logit_bias_adjustments if terms_to_forget else {}
    )

    # Return the text result from the API call
    return response.choices[0].message.content

# Define the prompt and terms that should be forgotten (biased)
prompt = "What animal jumped over the moon? Only provide name of animal."
terms_to_forget = ["cow", "COW"]
# prompt = "List ingredients that go into cookies. List only if there's a match"
# terms_to_forget = ["butter", "buter", "lard", "butter", "palm oil", "coconut oil", "egg", "eggs", "yolks", "bacon", "sausages", "cheese", "milk", "cream", "beef", "pork", "lamb"]
#prompt = "who is Jerry Cuomo. Comment only if there's a match."
#terms_to_forget = ["Jerry", "Cuomo"]

# Make API calls and display results
# First without any bias
response_before = biasedPrompt(prompt)
print(f"Before bias alteration: {prompt}")
print(response_before)

# Then with bias
response_after = biasedPrompt(prompt, terms_to_forget)
print(f"\nAfter bias alteration: {prompt}")
print(response_after)