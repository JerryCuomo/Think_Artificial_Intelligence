# Source: "Think Artificial Intelligence" by Jerry Cuomo, 2024
# Purpose: Educational code examples from the book.
# Copyright © 2024 Jerry Cuomo. All rights reserved.
#
# This code was autogenerated by GPT-4, from the following prompt:
# Prompt: Use BERT for sequence classification to analyze sentiment in climate-related text data from 'datasets/climatebert-climate-sentiment.csv'. The script should load and prepare the data, tokenize it for BERT, split it into training and evaluation subsets, initialize and configure the Trainer, and finally, evaluate the model's performance on test prompts both before and after training.
#
# About: This script demonstrates how to use BERT (Bidirectional Encoder Representations from Transformers) for sequence classification on a custom climate sentiment dataset. It involves loading the dataset, preparing and tokenizing the data for BERT, selecting training and evaluation subsets, configuring and initializing the Trainer, and evaluating the model's performance. The script uses Hugging Face's Transformers and Datasets libraries for model implementation and data manipulation.
#
# Setup: Python installed, with 'datasets/climatebert-climate-sentiment.csv' in your directory. 
# Install Transformers and Datasets libraries using 'pip install transformers datasets'.

from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments, pipeline
from datasets import load_dataset

# Load dataset and prepare for training
def load_and_prepare_data(file_path):
    # Load and tokenize custom climate dataset
    dataset = load_dataset('csv', data_files={'train': file_path})
    tokenized_datasets = dataset.map(tokenize_dataset, batched=True)
    return tokenized_datasets

# Tokenize text data for BERT
def tokenize_dataset(examples):
    # Returns tokenized examples with padding and truncation
    return tokenizer(examples['text'], padding="max_length", truncation=True, max_length=512)

# Select training and evaluation subsets
def select_subsets(tokenized_datasets, subset_size_ratio=0.8):
    # Splits dataset into training and evaluation sets
    subset_size = min(1000, len(tokenized_datasets['train']))
    train_size = int(subset_size * subset_size_ratio)
    small_train_dataset = tokenized_datasets['train'].shuffle(seed=42).select(range(train_size))
    small_eval_dataset = tokenized_datasets['train'].shuffle(seed=42).select(range(train_size, subset_size))
    return small_train_dataset, small_eval_dataset

# Initialize and return the Trainer
def initialize_trainer(train_dataset, eval_dataset):
    # Configures trainer with model and training arguments
    training_args = TrainingArguments(
        output_dir="../results",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=5,
        weight_decay=0.01,
        evaluation_strategy="epoch",
    )
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
    )
    return trainer

# Evaluate model performance on test prompts
def test_model_performance(sentiment_pipeline, prompts):
    # Prints predictions for each prompt
    for prompt in prompts:
        print(f"Prompt: {prompt}\nPrediction: {sentiment_pipeline(prompt)}\n")

# Initialize tokenizer and model for BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)

# Main flow
if __name__ == "__main__":
    dataset_path = '../datasets/climatebert-climate-sentiment.csv'
    tokenized_datasets = load_and_prepare_data(dataset_path)
    small_train_dataset, small_eval_dataset = select_subsets(tokenized_datasets)

    trainer = initialize_trainer(small_train_dataset, small_eval_dataset)
    print("Before Training:")
    sentiment_pipeline_before = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    
    test_prompts = [
        "The company has achieved a 20% reduction in water usage over the past year through improved conservation efforts.",
        "Recent audits revealed non-compliance with environmental regulations in several of our manufacturing facilities.",
        "Our new product line uses recycled materials, contributing to a circular economy and reducing waste.",
        "Emissions have increased due to expanded operations.",
        "The company is currently evaluating the environmental impact of its operations to better align with sustainability goals."
    ]
    
    test_model_performance(sentiment_pipeline_before, test_prompts)
    
    # Train the model
    trainer.train()

    print("After Training:")
    sentiment_pipeline_after = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    test_model_performance(sentiment_pipeline_after, test_prompts)
