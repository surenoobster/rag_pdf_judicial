import os
import google.generativeai as genai

# Get the Google API key from environment variables
google_api_key = os.getenv("GOOGLE_API_KEY")

# Print the API key for debugging purposes
print(f"GOOGLE_API_KEY: {google_api_key}")

# Check if the API key is loaded correctly
if google_api_key:
    # Configure the Generative AI client with the API key
    genai.configure(api_key=google_api_key)
else:
    print("GOOGLE_API_KEY not found. Make sure it's set in the .bashrc file.")
