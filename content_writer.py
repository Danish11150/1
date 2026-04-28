from utils.deepseek import call_deepseek
import json

def content_writer_agent(trend):
    system = """You are a professional blog Content Writer for Neo Vision Hub.
    You write SEO-optimized, engaging blog posts in English.
    Always return a JSON object with keys: title, content, excerpt
    The content should be 600-800 words with proper HTML formatting (h2, h3, p tags).
    Do not include markdown, only HTML tags inside content."""
    
    user = f"Write a complete blog post about this trending topic: {trend}\n\nReturn ONLY valid JSON with keys: title, content, excerpt"
    result = call_deepseek(system, user, 2000)
    
    try:
        clean = result.strip().replace("```json","").replace("```","").strip()
        return json.loads(clean)
    except:
        return {
            "title": "Latest Trends in Technology 2025",
            "content": f"<p>{result}</p>",
            "excerpt": result[:200]
        }
