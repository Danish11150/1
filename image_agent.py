import requests
import urllib.parse

def image_agent(title):
    # Pollinations.ai - completely free, no API key needed
    prompt = f"professional blog header image for article about {title}, modern, clean, digital art style"
    encoded = urllib.parse.quote(prompt)
    image_url = f"https://image.pollinations.ai/prompt/{encoded}?width=1200&height=630&nologo=true"
    return image_url
