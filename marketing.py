from utils.deepseek import call_deepseek

def marketing_agent(title):
    system = """You are a Marketing Agent for Neo Vision Hub blog.
    You create promotion strategies in Roman Urdu for the owner.
    Give practical, actionable marketing tips."""
    
    user = f"Is blog post ko promote karne ke liye 3 best strategies batao (Roman Urdu mein): {title}"
    return call_deepseek(system, user, 400)
