# Source: "Think Artificial Intelligence" by Jerry Cuomo, 2024
# Purpose: Educational code examples from the book.
# Copyright © 2024 Jerry Cuomo. All rights reserved.
#
# This code was autogenerated by GPT-4, from the following prompt:
# Prompt: Regenerate the setup and definitions for AI lifecycle stages and corresponding personas.
#
# About: This script visualizes the AI lifecycle stages and their corresponding personas 
# using a directed graph. It employs Python's NetworkX and Matplotlib libraries for graph generation and visualization.
#
# Setup: Python installed with NetworkX and Matplotlib. Install using 'pip install networkx matplotlib'.

import matplotlib.pyplot as plt
import networkx as nx

# Define AI Lifecycle stages and personas
lifecycle_stages = ["Data Preparation", "Model Development", "Prompt Engineering", "Model Deployment", "Application Integration", "Ethical Compliance"]
personas = ["Data Engineer", "Data Scientist", "Prompt Engineer", "AIOps Engineer", "Application Developer", "AI Ethics Officer"]

# Mapping stages to personas
lifecycle_pos = {stage: (i, 1) for i, stage in enumerate(lifecycle_stages)}
persona_pos = {persona: (i, 0) for i, persona in enumerate(personas)}

# Define colors for each stage and persona
lifecycle_colors = ['darkred', 'darkblue', 'darkgreen', 'darkorange', 'darkviolet', 'darkturquoise']
persona_colors = ['lightcoral', 'lightblue', 'lightgreen', 'peachpuff', 'plum', 'paleturquoise']

# Prepare the graph
G_combined = nx.DiGraph()

# Add nodes for lifecycle stages and personas
for stage in lifecycle_stages:
    G_combined.add_node(stage)

for persona in personas:
    G_combined.add_node(persona)

    # Connect each stage to its corresponding persona
    G_combined.add_edge(stage, persona)

# Define the node size and font size
node_size = 4000
font_size = 12

# Define the combined positions
combined_pos = {**lifecycle_pos, **persona_pos}

# Redrawing the graph with the generated definitions
nx.draw(G_combined, combined_pos, with_labels=True, node_color=lifecycle_colors + persona_colors, 
        node_size=node_size, font_size=font_size, node_shape='s', arrowsize=20)

plt.title("AI Lifecycle and Associated Personas", fontsize=15)
plt.show()
