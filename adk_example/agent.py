from google.adk.agents import LlmAgent

# --- Define Sub-Agents ---

# Scriptwriter agent (could use a tool like google_search for trends)
scriptwriter_agent = LlmAgent(
    name="scriptwriter_agent",
    model="gemini-2.5-pro-exp-03-25",
    description="Writes engaging scripts for YouTube Shorts based on current trends.",
    instruction="""Given a topic, research current trends and write a concise, engaging script for a YouTube Short. Use the google_search tool if needed to find up-to-date information.""",
    # tools=[google_search], # Uncomment if using built-in tools
)

# Visualizer agent
visualizer_agent = LlmAgent(
    name="visualizer_agent",
    model="gemini-2.5-pro-exp-03-25",
    description="Creates visual descriptions to accompany YouTube Shorts scripts.",
    instruction="""Given a script, suggest creative visual scenes or imagery that would enhance the Short."""
)

# Formatter agent
formatter_agent = LlmAgent(
    name="formatter_agent",
    model="gemini-2.5-pro-exp-03-25",
    description="Formats scripts and visuals into a polished Markdown output.",
    instruction="""Combine the script and visuals into a clear, well-structured Markdown format for easy review."""
)

# --- Define Parent Agent with Hierarchy ---

youtube_shorts_agent = LlmAgent(
    name="youtube_shorts_agent",
    model="gemini-2.5-pro-exp-03-25",
    description="You are ShortForm Genius, an AI specialized in crafting engaging YouTube Shorts content.",
    instruction="""When given a topic, coordinate with your sub-agents to:
                    1. Generate a script (scriptwriter_agent)
                    2. Create visual ideas (visualizer_agent)
                    3. Format everything nicely (formatter_agent)
                    Return the final Markdown for the user.
                """,
    sub_agents=[
        scriptwriter_agent,
        visualizer_agent,
        formatter_agent
    ]
)

# --- Run the Root Agent for the Runner ---
root_agent = youtube_shorts_agent

