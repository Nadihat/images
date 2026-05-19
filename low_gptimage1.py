#!/usr/bin/env python3
import sys
import base64
from openai import OpenAI

# Check if both the prompt and filename arguments were provided
if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} \"<prompt>\" <filename.png>")
    sys.exit(1)

# Assign the arguments to variables
prompt_text = sys.argv[1]
output_filename = sys.argv[2]

client = OpenAI()

print("Generating image with DALL-E 3...")
print(f"Prompt: '{prompt_text}'")
print(f"Saving to: '{output_filename}'\n")

# Call the standard Image API for DALL-E 2
response = client.images.generate(
    model="gpt-image-1",
    prompt=prompt_text,
    n=1,
    size="1024x1024",
    quality="low"
)

# Extract the base64 string from the DALL-E 2 response object
image_base64 = response.data[0].b64_json
    
if image_base64:
    # Save the base64 data to the requested file
    with open(output_filename, "wb") as f:
        f.write(base64.b64decode(image_base64))
    print(f"Success! Saved to {output_filename}")
else:
    print("Error: No image data was returned.")
