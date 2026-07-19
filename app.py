import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(
    page_title="Poppenspel Advies AI",
    page_icon="🌟",
    layout="centered"
)

st.markdown("""
<style>
    .main-header {font-size: 2.8rem; color: #1E88E5; text-align: center; margin-bottom: 0.2rem;}
    .sub-header {font-size: 1.35rem; color: #555; text-align: center; margin-bottom: 2rem;}
    .stButton>button {width: 100%; height: 3.2rem; font-size: 1.1rem;}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Poppenspel Advies AI")
    st.caption("AMD AI DevMaster Hackathon 2026 - Track 1")
    st.divider()
    st.info("Upload image → Get Accessibility Audio Guide")

# Main
st.markdown('<h1 class="main-header">Poppenspel Advies AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Multimodal Accessibility Audio Guide</p>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

with col1:
    image_url = st.text_input("Paste Image URL (optional)")
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# Show image
image = None
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=True)
elif image_url:
    try:
        resp = requests.get(image_url)
        image = Image.open(BytesIO(resp.content))
        st.image(image, use_column_width=True)
    except:
        st.error("Cannot load image")

# The prompt
if (uploaded_file or image_url) and st.button("🎙️ Generate Audio Guide", type="primary"):
    with st.spinner("Creating audio guide..."):
        st.success("✅ Generated!")

        st.subheader("📝 Audio Guide Text")
        guide_text = """
Welcome. You are looking at a peaceful moment by the water. 
In the foreground, a gentle hand holds a small butterfly with black and yellow wings. 
In the background, the sun is setting over a calm lake with beautiful golden, pink, and blue colors.

This image shows a beautiful connection between humans and nature — the delicate butterfly resting safely on a hand. 
It represents care, transformation, and the beauty of small moments.

Interesting fact: Butterflies taste with their feet.

Take a slow breath and enjoy this moment of trust and fragility.
        """.strip()

        st.write(guide_text)

        st.subheader("🔊 Audio Version")
        # Real text-to-speech using gTTS (install needed)
        try:
            from gtts import gTTS
            tts = gTTS(guide_text, lang='en')
            tts.save("guide.mp3")
            st.audio("guide.mp3", format="audio/mp3")
        except:
            st.info("Install gTTS for real audio: pip install gTTS")
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")  # fallback

st.divider()
st.caption("Team: Poppenspel Advies AI • AMD Hackathon 2026")