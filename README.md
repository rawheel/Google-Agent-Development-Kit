# Google ADK Example

A hierarchical agent system built with Google's Agent Development Kit (ADK) for creating engaging social media content.

## Overview

This project uses Google's ADK to create a multi-agent system that generates social media content. The system consists of:

1. A parent agent that coordinates the entire process
2. Three specialized sub-agents:
   - **Trend Finder Agent**: Discovers trending hashtags for maximum engagement
   - **Content Writer Agent**: Creates engaging posts using trending hashtags
   - **Visual Concept Agent**: Suggests visual ideas to accompany the posts

## Project Structure

```
Google-Agent-Development-Kit/
├── adk_example/
│   ├── __init__.py     # Module initialization
│   ├── agent.py        # Agent definitions
│   └── venv/           # Virtual environment
└── README.md           # This file
```

## Requirements

- Python 3.8+
- Google ADK (`google-adk`)
- Google API credentials configured

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/rawheel/Google-Agent-Development-Kit
   cd Google-Agent-Development-Kit
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure Google API credentials following the [official documentation](https://developers.google.com/identity/protocols/oauth2).

## Usage

Run the agent using the ADK CLI:

```
adk run adk_example
```

This will start the agent service, which you can then interact with through the ADK interface.

Example prompt:
```
Create a social media post about artificial intelligence
```

## Agent Architecture

The system uses a hierarchical approach:

- **Parent Agent (`social_media_agent`)**: Coordinates the workflow and delegates tasks
- **Sub-agents**:
  - `trend_finder_agent`: Researches and identifies trending hashtags
  - `content_writer_agent`: Creates engaging social media posts
  - `visual_concept_agent`: Suggests visual ideas for the content

Run the agent using the ADK UI:
```
adk web
```

## Customization

You can customize each agent's behavior by modifying the instructions in `agent.py`. Additional tools like search capabilities can be enabled by uncommenting the appropriate lines.

## Learn More

For more information about Google's Agent Development Kit (ADK) and how to build AI agents, check out my article:
[Meet Google's Agent Development Kit (ADK)🤯: Build Real AI Agents, Not Just Chatbots](https://dev.to/rawheel/meet-googles-agent-development-kit-adk-build-real-ai-agents-not-just-chatbots-44g)
