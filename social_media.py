from utils.deepseek import call_deepseek
import json

def social_media_agent(title, content):
    system = """You are a Social Media Manager for Neo Vision Hub.
    Create engaging social media captions in English.
    Return JSON with keys: instagram, twitter, linkedin"""
    
    user = f"Create social media captions for this blog post: {title}\nBrief: {content[:200]}\n\nReturn ONLY valid JSON."
    result = call_deepseek(system, user, 600)
    
    try:
        clean = result.strip().replace("```json","").replace("```","").strip()
        return json.loads(clean)
    except:
        return {
            "instagram": f"New post alert! {title} - Check the link in bio! #AI #Tech #NeoVisionHub",
            "twitter": f"Just published: {title} Read now on Neo Vision Hub! #AI #Tech",
            "linkedin": f"Excited to share our latest article: {title}"
        }
