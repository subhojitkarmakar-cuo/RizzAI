import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="RizzAI | Relationship Coach", page_icon="🔥", layout="centered")

# --- CUSTOM THEME (Neon Pink & Purple) ---
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }
    h1 {
        color: #FF007A;
        text-shadow: 2px 2px #8A2BE2;
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF007A, #8A2BE2);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0px 0px 15px #FF007A;
        transform: scale(1.02);
    }
    .rizz-card {
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #8A2BE2;
        background-color: #1A1A2E;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: API SETUP ---
with st.sidebar:
    st.title("Settings ⚙️")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Get your key from [Google AI Studio](https://aistudio.google.com/)")
    st.markdown("---")
    st.markdown("### Supported Languages")
    st.write("English, Hindi, Bengali, Marathi, Punjabi, and more!")

# --- APP HEADER ---
st.title("🔥 RizzAI")
st.markdown("<p style='text-align: center; color: #BBB;'>The world's best relationship coach & Rizz expert.</p>", unsafe_allow_html=True)

# --- CORE LOGIC ---
def get_rizz_response(api_key, text_input, image_input=None):
    genai.configure(api_key=api_key)
    # Using gemini-1.5-flash for speed and multimodal capabilities
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    system_role = (
        "You are the world's best relationship coach and Rizz expert. Your task is to analyze "
        "chat screenshots or text messages provided by the user. Understand the emotional context, "
        "tone, and subtext. Detect the language of the input (Bengali, Hindi, English, etc.) "
        "and generate the replies in that SAME language and script automatically. "
        "Provide exactly 3 distinct reply options: \n"
        "1. 'The Smooth Rizz' (Witty & Charismatic)\n"
        "2. 'Deep Connection' (Emotional & Romantic)\n"
        "3. 'The Savage/Alpha' (Bold & Confident).\n"
        "Keep it natural, modern, and high-quality. No robotic explanations."
    )

    content = [system_role]
    if text_input:
        content.append(f"User Message: {text_input}")
    if image_input:
        img = Image.open(image_input)
        content.append(img)

    response = model.generate_content(content)
    return response.text

# --- UI INPUTS ---
col1, col2 = st.tabs(["📝 Text Input", "📸 Upload Screenshot"])

with col1:
    chat_text = st.text_area("Paste the last few messages here:", placeholder="e.g., 'Seen at 10 PM? That's cold.'")

with col2:
    uploaded_file = st.file_uploader("Upload a chat screenshot", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.image(uploaded_file, caption="Screenshot Loaded", use_container_width=True)

# --- ACTION ---
if st.button("Generate Rizz ✨"):
    if not api_key:
        st.error("Please add your API Key in the sidebar!")
    elif not chat_text and not uploaded_file:
        st.warning("Please provide either a message or a screenshot.")
    else:
        with st.spinner("Analyzing vibes..."):
            try:
                result = get_rizz_response(api_key, chat_text, uploaded_file)
                st.subheader("Your Next Moves:")
                st.markdown(f'<div class="rizz-card">{result}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"An error occurred: {e}")

# --- FOOTER ---
st.markdown("---")
st.caption("RizzAI v1.0 | Made for the bold.")
