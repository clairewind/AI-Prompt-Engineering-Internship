import openai

# Set your OpenAI API key
api_key = "apikey"
openai.api_key = api_key

# Define a function to interact with the AI model
def prompt_generation(prompt, model="text-davinci-003", max_tokens=100):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )
    return response['choices'][0]['message']['content']

# Example prompts for zero-shot, few-shot, and chain-of-thought techniques
zero_shot_prompt = "Explain quantum entanglement."
few_shot_prompt = "Explain quantum entanglement using these terms: 'superposition', 'spooky action at a distance', and 'quantum states'."
chain_of_thought_prompts = [
    "What is quantum entanglement?",
    "How does quantum entanglement relate to the concept of superposition?",
    "Can you explain how 'spooky action at a distance' plays a role in quantum entanglement?"
]

# Function to generate responses using different prompt types
def generate_responses(prompt_type):
    if prompt_type == "zero_shot":
        return prompt_generation(zero_shot_prompt)
    elif prompt_type == "few_shot":
        return prompt_generation(few_shot_prompt)
    elif prompt_type == "chain_of_thought":
        full_response = ""
        for prompt in chain_of_thought_prompts:
            full_response += prompt_generation(prompt) + " "
        return full_response

# Test the prompt generation functions
print("Zero-Shot Prompt Response:")
print(generate_responses("zero_shot"))
print("\nFew-Shot Prompt Response:")
print(generate_responses("few_shot"))
print("\nChain-of-Thought Prompt Response:")
print(generate_responses("chain_of_thought"))
