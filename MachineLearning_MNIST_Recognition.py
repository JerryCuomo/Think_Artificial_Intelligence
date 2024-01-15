# Source: "Think Artificial Intelligence" by Jerry Cuomo, 2024
# Purpose: Educational code examples from the book.
# Copyright © 2024 Jerry Cuomo. All rights reserved.

# Generated via prompt: Generate the simplest python program to illustrate deep learning in action

# MNIST Digit Recognition with TensorFlow
# This program utilizes the TensorFlow library to create a neural network model for recognizing handwritten digits.
# It includes steps for loading the MNIST dataset, preprocessing the data, defining and compiling the model,
# and then training and evaluating the model's performance.
# The model uses a simple architecture suitable for beginners in deep learning

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalize the images
train_images = train_images / 255.0
test_images = test_images / 255.0

# Convert labels to one-hot encoded format
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Build the model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc}")

# This program trains a neural network to recognize handwritten digits.

#    Load MNIST Dataset: Import digit images.

#    Normalize Images: Standardize brightness levels.

#    One-Hot Encode Labels: Convert to binary format.

#    Build Neural Network:
#        Flatten: Transform images.
#        Dense Layer: 128 ReLU units.
#        Dense Layer: 10 Softmax units.

#    Compile Model: Optimize, evaluate loss, measure accuracy.

#    Train Model: 5 learning cycles.

#    Evaluate: Test and report accuracy.