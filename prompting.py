import prompting as st
import random
import os

# Sample Data (Expand these based on sources)
camera_movements = [
    "Slow zoom (A gradual zoom in to focus the subject)", 
    "First-person perspective (Shot from character's viewpoint)", 
    "Aerial shot (High-altitude view of the scene)", 
    "Tracking shot (Camera follows the action)",
    "Extreme wide shot (Emphasizes scale and environment)"
]

lighting_styles = [
    "Silhouette (Subject in shadow, light from behind)", 
    "Firelight (Scene illuminated by fire)", 
    "Neon-lit (Colorful, glowing lights typical of urban settings)",
    "Sunlight filtering through leaves (Natural and soft lighting)",
    "Diffused lighting (Soft, even light with minimal shadows)"
]

moods = [
    "Magical (Dreamy, surreal)", 
    "Ethereal (Delicate, otherworldly)", 
    "Mysterious (Dark, enigmatic)", 
    "Joyful (Bright, happy)"
]

characters = ["Shaman woman", "Group of women", "Lone figure", "Jaguar"]

settings = ["Ancient forest", "Emerald lagoon", "Cave of healing", "Desert landscape"]
details = ["Crystals", "Incense smoke", "Petroglyphs", "Medicinal plants"]

# Function for handling custom options and removing explanations for prompt
def custom_option(options, label):
    custom = st.sidebar.text_input(f"Custom {label}:")
    if custom:
        display_options = options + [f"Custom: {custom}"]
    else:
        display_options = options
    selected = st.sidebar.selectbox(f"Choose a {label}:", display_options)
    if selected.startswith("Custom:"):
        return custom
    return selected.split(' (')[0]  # Removes explanation in parentheses

# Streamlit App Title
st.title("Prompt Generator for Alpha Gen-3")

# Sidebar Inputs with Custom Options
st.sidebar.header("Prompt Elements")
selected_camera = custom_option(camera_movements, "camera movement")
selected_lighting = custom_option(lighting_styles, "lighting style")
selected_mood = custom_option(moods, "mood")
selected_character = custom_option(characters, "character")
selected_setting = custom_option(settings, "setting")
selected_details = st.sidebar.multiselect("Choose details (optional):", details)

# Idea input
idea = st.sidebar.text_area("Enter your idea:")

# Show explanations of selected options before the prompt
explanations = {
    "camera movement": selected_camera,
    "lighting style": selected_lighting,
    "mood": selected_mood,
    "character": selected_character,
    "setting": selected_setting
}

st.header("Selected Elements with Explanations:")
for key, value in explanations.items():
    st.write(f"**{key.capitalize()}:** {value}")

# Generate Prompt Logic
prompt = f"Create a visually stunning scene with a {selected_mood} atmosphere.\n"
prompt += f"Camera: {selected_camera}\n"
prompt += f"Lighting: {selected_lighting}\n"
prompt += f"Character: {selected_character}\n"
prompt += f"Setting: {selected_setting}\n"

if selected_details:
    prompt += "Details: " + ", ".join(selected_details) + "\n"

if idea:
    prompt += f"Idea: {idea}\n"

# Display Generated Prompt
st.header("Generated Prompt:")
st.write(prompt)

# Links, Examples, and Instructions
st.sidebar.header("Links & Tutorials:")
st.sidebar.write("""
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Cinematography Techniques](https://www.studiobinder.com/blog/cinematography-techniques/)
- [Lighting Styles Guide](https://www.masterclass.com/articles/lighting-in-film)
""")

st.sidebar.header("Examples & GIFs:")
st.sidebar.write("""
- [Camera Movement GIFs](https://www.giphy.com)
- [Lighting Techniques in Film](https://www.youtube.com/watch?v=fQXB9oFmbHs)
""")

st.sidebar.header("Running the Code:")
st.sidebar.write("""
1. Ensure Python and Streamlit are installed. Use `pip install streamlit` if necessary.
2. Save this code as a Python file (e.g., `prompt_generator.py`).
3. Run the script using the terminal with `streamlit run prompt_generator.py`.
4. The app will open in your web browser.
""")

st.sidebar.header("Important Considerations:")
st.sidebar.write("""
- **Source Data:** Expand the sample data lists with keywords and concepts from your sources to make the prompt generator more robust.
- **Prompt Refinement:** Generating effective prompts may require iterative refinement. Experiment with different variations.
- **Target AI Model:** Adapt the prompts based on the specific requirements and capabilities of the AI model you're using.
""")
