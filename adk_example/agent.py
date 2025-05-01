from google.adk.agents import LlmAgent

# --- Define Sub-Agents ---

# Trend finder agent
trend_finder_agent = LlmAgent(
    name="trend_finder_agent",
    model="gemini-2.5-pro-exp-03-25",
    description="Discovers trending hashtags for social media content.",
    instruction="""Given a topic, research and identify the most relevant trending hashtags.
                   Return 3-5 hashtags that would maximize engagement.""",
    # tools=[google_search], # Uncomment if using built-in tools
)

# Content writer agent
content_writer_agent = LlmAgent(
    name="content_writer_agent",
    model="gemini-2.5-pro-exp-03-25",
    description="Creates engaging social media posts using trending hashtags.",
    instruction="""Given a topic and trending hashtags, write a catchy, engaging social media post.
                   Keep it concise and optimized for the platform."""
)

# Visual concept agent
visual_concept_agent = LlmAgent(
    name="visual_concept_agent",
    model="gemini-2.5-pro-exp-03-25",
    description="Suggests visual concepts to accompany social media posts.",
    instruction="""Given a social media post, suggest creative visual ideas that would
                   enhance engagement and complement the written content."""
)

# --- Define Parent Agent with Hierarchy ---

social_media_agent = LlmAgent(
    name="social_media_agent",
    model="gemini-2.5-pro-exp-03-25",
    description="You are SocialMedia Genius, an AI specialized in crafting engaging social media content.",
    instruction="""When given a topic, coordinate with your sub-agents to:
                    1. Find trending hashtags (trend_finder_agent)
                    2. Write an engaging post (content_writer_agent)
                    3. Suggest visual concepts (visual_concept_agent)
                    Return the complete social media content package to the user.
                """,
    sub_agents=[
        trend_finder_agent,
        content_writer_agent,
        visual_concept_agent
    ]
)

# --- Run the Root Agent for the Runner ---
root_agent = social_media_agent
