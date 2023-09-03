# Neuralyzer.py
# By Jerry Cuomo, 2023, Art of AI for Business
# A utility to make biased API calls to OpenAI's GPT-3
# The program can be configured to forget (bias against) specific terms
# when generating text in response to a given prompt.
# Think "Men in Black" neuralyzer, but for text!

import openai
import tiktoken

# Initialize API credentials
openai.api_key = "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"

# Specify the GPT-3 model to be used
# Supported models include "text-davinci-003", "text-ada-001", etc.
MODEL = "text-davinci-003"  # For example, you could replace with "text-ada-001"

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
    #print("Logit bias adjustments:", logit_bias_adjustments)
    
    # Perform the API call with or without logit bias based on the terms_to_forget
    response = openai.Completion.create(
        engine=MODEL,
        prompt=prompt,
        temperature=0.2,  # Lowering temperature to make output more deterministic
        max_tokens=150,
        logit_bias=logit_bias_adjustments if terms_to_forget else {},
        frequency_penalty=0,
        presence_penalty=-0.5  # Adding a slight negative presence penalty
    )
    
    # Return the text result from the API call
    return response.choices[0].text.strip()

# Define the prompt and terms that should be forgotten (biased)
prompt = "What animal jumped over the moon?"
terms_to_forget = ["cow"]
# prompt = "List ingredients that go into cookies. List only if there's a match"
# terms_to_forget = ["butter", "buter", "lard", "butter", "palm oil", "coconut oil", "egg", "eggs", "yolks", "bacon", "sausages", "cheese", "milk", "cream", "beef", "pork", "lamb"]
# prompt = "who is Jerry Cuomo. Comment only if there's a match."
# terms_to_forget = ["Jerry", "Cuomo"]


# Make API calls and display results
# First without any bias
response_before = biasedPrompt(prompt)
print(f"Before bias alteration: {prompt}")
print(response_before)

# Then with bias
response_after = biasedPrompt(prompt, terms_to_forget)
print(f"\nAfter bias alteration: {prompt}")
print(response_after)