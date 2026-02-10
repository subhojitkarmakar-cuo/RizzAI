import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="RizzAI", page_icon="🔥")

# --- CUSTOM STYLE ---
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    h1 { color: #FF007A; text-align: center; }
    .stButton>button { background: linear-gradient(45deg, #FF007A, #8A2BE2); color: white; border-radius: 10px; width: 100%; height: 50px; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("Settings ⚙️")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Get key from: aistudio.google.com")

# --- HEADER ---
st.title("🔥 RizzAI")
st.write("World's best Rizz expert & Coach.")

# --- INPUTS ---
tab1, tab2 = st.tabs(["📝 Text", "📸 Screenshot"])

with tab1:
    chat_text = st.text_area("Paste messages here:", placeholder="Example: Hi, how are you?")

with tab2:
    uploaded_file = st.file_uploader("Upload screenshot", type=["jpg", "png", "jpeg"])

# --- GENERATE ---
if st.button("Generate Rizz ✨"):
    if not api_key:
        st.error("Please add API Key in sidebar!")
    elif not chat_text and not uploaded_file:
        st.warning("Please provide text or image.")
    else:
        try:
            genai.configure(api_key=api_key)
            # আপডেট করা মডেলের নাম যা নিশ্চিতভাবে কাজ করবে
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            
            prompt = "You are a Rizz expert. Analyze this chat and give 3 witty, romantic, or bold replies in the same language as input (Bengali/Hindi/English)."
            
            content = [prompt]
            if chat_text: content.append(chat_text)
            if uploaded_file: content.append(Image.open(uploaded_file))
            
            with st.spinner("Thinking..."):
                response = model.generate_content(content)
                st.success("Your Moves:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
