import openai
from dotenv import load_dotenv
import os

# Load your OpenAI API key from the .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_text(prompt):
    """
    Generates text using OpenAI's ChatCompletion API.

    Args:
        prompt (str): The input prompt for the AI.

    Returns:
        str: The AI-generated response.
    """
    try:
        # Make a request to the OpenAI ChatCompletion endpoint
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        # Return the generated content
        return response["choices"][0]["message"]["content"].strip()

    except Exception as e:
        # Handle exceptions and return the error message
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Example prompt
    prompt = "What is quantum computing in simple terms?"
    
    # Call the function and display the result
    result = generate_text(prompt)
    print("Generated Text:")
    print(result)
print(openai.api_key)
