from utils.deepseek import call_deepseek

def editor_agent(post, seo, image_url):
    system = """You are a professional Editor for Neo Vision Hub blog.
    You review and improve blog posts.
    Return the improved post as a JSON with keys: title, content, excerpt, meta_title, meta_description, tags, image_url"""
    
    user = f"""Review and improve this blog post:
Title: {post['title']}
Content: {post['content'][:500]}...
SEO Meta Title: {seo.get('meta_title','')}
SEO Meta Desc: {seo.get('meta_description','')}
Tags: {seo.get('tags',[])}

Return ONLY valid JSON with keys: title, content, excerpt, meta_title, meta_description, tags, image_url
Set image_url to: {image_url}"""
    
    result = call_deepseek(system, user, 2000)
    try:
        import json
        clean = result.strip().replace("```json","").replace("```","").strip()
        final = json.loads(clean)
        final["image_url"] = image_url
        final["content"] = post["content"]
        return final
    except:
        post["image_url"] = image_url
        post["meta_title"] = seo.get("meta_title", post["title"])
        post["meta_description"] = seo.get("meta_description", post["excerpt"])
        post["tags"] = seo.get("tags", [])
        return post
