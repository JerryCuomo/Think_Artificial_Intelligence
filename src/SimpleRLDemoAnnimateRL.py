# Source: "Think Artificial Intelligence" by Jerry Cuomo, 2024
# Purpose: To introduce beginners to reinforcement learning concepts through practical examples.
# Copyright © 2024 Jerry Cuomo. All rights reserved.
#
# This code was autogenerated by GPT-4, from the following prompt:
# Prompt: Create a simple reinforcement learning program using the Lunar Lander environment from Gymnasium to demonstrate basic RL concepts to undergraduates.
#
# About: This script introduces the Lunar Lander environment from Gymnasium as a practical example to teach basic reinforcement learning concepts. It demonstrates initializing the environment, running episodes with random actions, and tracking the total reward to gauge performance. The example emphasizes the importance of observation, action selection, and reward feedback loop in reinforcement learning.
#
# Setup: Python installed, with Gymnasium installed in your environment. 
# Install Gymnasium using 'pip install gymnasium'. Ensure you have a suitable environment for rendering if you wish to visualize the simulation.

import gymnasium as gym

def main():
    # Initialize the Lunar Lander environment with render_mode specified
    env = gym.make("LunarLander-v2", render_mode="human")
    
    # Reset the environment at the start of each episode
    observation, info = env.reset(seed=42)
    
    # Initialize a list to keep track of total rewards for each episode
    episode_rewards = []

    # Run for a certain number of episodes, e.g., 10
    for episode in range(10):
        total_reward = 0  # To keep track of the total reward per episode
        while True:
            # Render the environment to visualize (optional, depending on your setup)
            # env.render()  # Not needed if render_mode="human" is set during env.make()
            
            # Agent selects an action randomly (this is where a policy would be implemented)
            action = env.action_space.sample()
            
            # Environment executes the action and returns new state and reward
            observation, reward, terminated, truncated, info = env.step(action)
            
            total_reward += reward  # Update the total reward
            
            # Check if the episode is done (either terminated or truncated)
            if terminated or truncated:
                observation, info = env.reset()  # Reset the environment for the next episode
                break  # Exit the loop and move to the next episode
        
        episode_rewards.append(total_reward)  # Store the total reward for this episode
        print(f"Episode {episode + 1}: Total Reward = {total_reward}")

    env.close()  # Close the environment when done

    # Calculate and print the average reward after all episodes are done
    average_reward = sum(episode_rewards) / len(episode_rewards)
    print(f"Average reward over {len(episode_rewards)} episodes: {average_reward}")

if __name__ == "__main__":
    main()
