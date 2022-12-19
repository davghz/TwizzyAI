import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = ""

# Create a Completion object
completion = openai.Completion()

# Set the model to use
model = "text-davinci-003"

def generate_completion(prompt, max_tokens=1024, temperature=0.5, top_p=1.0, presence_penalty=0.0):
    """
    Generate a completion for a given prompt using the OpenAI API.
    
    Parameters:
    - prompt (str): The prompt to complete.
    - max_tokens (int): The maximum number of tokens (words and punctuation) to generate in the completion.
    - temperature (float): The "creativity" of the completions. A higher temperature will result in more creative and varied completions, while a lower temperature will result in more predictable completions.
    - top_p (float): The probability that the API will choose a particular completion. A higher value will result in more predictable completions, while a lower value will result in more creative completions.
    - presence_penalty (float): The probability that the API will choose a completion that does not include certain words or phrases.
    
    Returns:
    - str: The completed text.
    """
    # Send the completion request
    response = completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        presence_penalty=presence_penalty,
    )

    # Check if the request was successful
    if response:
        # Return the completed text
        return response.choices[0].text
    else:
        # Return an error message
        return "Error: " + response.json()["error"]

while True:
    # Get the prompt from the user
    prompt = input("Enter a prompt to complete (or 'q' to quit): ")

    if prompt == 'q': 
        break

    # Generate the completion
    completed_text = generate_completion(prompt)

    # Print the completed text
    print(completed_text)
