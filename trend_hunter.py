from utils.deepseek import call_deepseek

def trend_hunter_agent():
    system = """You are a Trend Hunter for Neo Vision Hub blog. 
    You find the most trending topics in AI, Technology, Trading, or Gaming.
    Always return ONE trending topic with a brief explanation in English."""
    
    user = "Find the most trending topic right now in AI, Tech, Trading or Gaming that would get high traffic. Return the topic and why it's trending."
    return call_deepseek(system, user, 300)
