import streamlit as st
import random
import os


# Sample Data (Expand these based on sources)
camera_movements = ["Slow zoom", "First-person perspective", "Aerial shot", "Tracking shot"]
lighting_styles = ["Silhouette", "Firelight", "Neon-lit", "Sunlight filtering through leaves"]
moods = ["Magical", "Ethereal", "Mysterious", "Joyful"]
characters = ["Shaman woman", "Group of women", "Lone figure", "Jaguar"]
settings = ["Ancient forest", "Emerald lagoon", "Cave of healing", "Desert landscape"]
details = ["Crystals", "Incense smoke", "Petroglyphs", "Medicinal plants"]

# Streamlit App Title
st.title("Prompt Generator for Creative Visuals")

# Sidebar Inputs
st.sidebar.header("Prompt Elements")
selected_camera = st.sidebar.selectbox("Choose a camera movement:", camera_movements)
selected_lighting = st.sidebar.selectbox("Choose a lighting style:", lighting_styles)
selected_mood = st.sidebar.selectbox("Choose a mood:", moods)
selected_character = st.sidebar.selectbox("Choose a character:", characters)
selected_setting = st.sidebar.selectbox("Choose a setting:", settings)
selected_details = st.sidebar.multiselect("Choose details (optional):", details)

# Generate Prompt Logic
prompt = f"Create a visually stunning scene with a {selected_mood} atmosphere.\n"
prompt += f"Camera: {selected_camera}\n"
prompt += f"Lighting: {selected_lighting}\n"
prompt += f"Character: {selected_character}\n"
prompt += f"Setting: {selected_setting}\n"

if selected_details:
    prompt += "Details: " + ", ".join(selected_details)

# Display Generated Prompt
st.header("Generated Prompt:")
st.write(prompt)

# Explanation and Connection to Sources
st.sidebar.header("Explanation:")
st.sidebar.write("""
- **Prompt Structure:** The prompt is generated using structured elements: camera movement, lighting, mood, character, setting, and details, based on keywords inspired by your sources.
- **Keywords:** Sample keywords are chosen to align with the visuals and styles mentioned in the sources.
- **Visual Elements:** The prompt elements align with common imagery from the sources, such as smoke, crystals, and natural settings.
- **Streamlit UI:** This tool uses Streamlit to create an interactive interface for easy input and prompt generation.
""")

# Instructions for Running the Code
st.sidebar.header("Running the Code:")
st.sidebar.write("""
1. Ensure Python and Streamlit are installed. Use `pip install streamlit` if necessary.
2. Save this code as a Python file (e.g., `prompt_generator.py`).
3. Run the script using the terminal with `streamlit run prompt_generator.py`.
4. The app will open in your web browser.
""")

# Important Considerations
st.sidebar.header("Important Considerations:")
st.sidebar.write("""
- **Source Data:** Expand the sample data lists with keywords and concepts from your sources to make the prompt generator more robust.
- **Prompt Refinement:** Generating effective prompts may require iterative refinement. Experiment with different variations.
- **Target AI Model:** Adapt the prompts based on the specific requirements and capabilities of the AI model you're using.
""")
