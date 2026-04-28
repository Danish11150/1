from utils.deepseek import call_deepseek
import json

def seo_expert_agent(title, content):
    system = """You are an SEO Expert for Neo Vision Hub blog.
    You optimize blog posts for Google rankings.
    Return a JSON object with: meta_title, meta_description, keywords (list of 5), tags (list of 5)"""
    
    user = f"Optimize SEO for this blog post.\nTitle: {title}\nContent preview: {content[:300]}\n\nReturn ONLY valid JSON."
    result = call_deepseek(system, user, 500)
    
    try:
        clean = result.strip().replace("```json","").replace("```","").strip()
        return json.loads(clean)
    except:
        return {
            "meta_title": title,
            "meta_description": content[:160],
            "keywords": ["technology", "AI", "news", "2025", "trending"],
            "tags": ["AI", "Tech", "News", "Trending", "2025"]
        }
