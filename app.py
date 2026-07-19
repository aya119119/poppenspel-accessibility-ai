import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="Poppenspel Advies AI", page_icon="🌟", layout="wide")

st.markdown("""
<style>
    .main-header {font-size: 3rem; color: #1E88E5; text-align: center; margin: 0;}
    .sub-header {font-size: 1.4rem; color: #444; text-align: center; margin-bottom: 2rem;}
    .feature-card {background: #f8f9fa; padding: 1.5rem; border-radius: 12px; border: 1px solid #e0e0e0;}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://raw.githubusercontent.com/sahirmaharaj/exifa/main/img/Exifa.gif", width=80)
    st.title("Poppenspel Advies AI")
    st.caption("AMD AI DevMaster Hackathon 2026 • Track 1: Multimodal AI")
    st.divider()
    st.success("Accessibility + Creativity + Education")

# Main Header
st.markdown('<h1 class="main-header">Poppenspel Advies AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">See the world through words • Create stories • Learn & Explore</p>', unsafe_allow_html=True)

# Tabs for different modes
tab1, tab2, tab3, tab4 = st.tabs(["🎙️ Audio Guide", "📖 Story Creator", "🏛️ Historical Guide", "🎨 Creative Studio"])

with tab1:  # Accessibility Audio Guide
    st.subheader("Accessibility Audio Guide")
    st.write("Upload any image and get a clear spoken description — perfect for visually impaired users.")
    
    col1, col2 = st.columns([3,1])
    with col1:
        uploaded_file = st.file_uploader("Upload Image", type=["jpg","jpeg","png"], key="audio")
        image_url = st.text_input("Or paste image URL", key="url_audio")
    
    if uploaded_file or image_url:
        if uploaded_file:
            image = Image.open(uploaded_file)
        else:
            image = Image.open(BytesIO(requests.get(image_url).content))
        st.image(image, use_column_width=True)
        
        if st.button("Generate Audio Guide", type="primary", use_container_width=True):
            with st.spinner("Creating detailed audio guide..."):
                st.success("✅ Generated!")
                description = """
Welcome. You are looking at a beautiful scene. [Your model will generate real description here]
This image shows... (detailed description)
Interesting fact: ...
Take a moment to appreciate this view.
                """
                st.write(description)
                st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")  # replace later with real TTS

with tab2:  # Story Creator
    st.subheader("Children's Story Creator")
    st.write("Turn any image into an engaging narrated children's story.")
    # Similar structure...

with tab3:  # Historical Guide (as requested by teammate)
    st.subheader("🏛️ Historical & Museum Audio Guide")
    st.write("Perfect for historical pictures, monuments, paintings, or tourist sites.")
    st.info("This mode adds rich historical context and facts — great for museum visitors and students.")
    # Same upload + button logic

with tab4:  # Creative Studio
    st.subheader("Creative Studio")
    st.write("Style Transfer • Image to Cartoon • Short Video")
    st.button("Apply Children's Book Style", use_container_width=True)
    st.button("Generate Short Animated Video", use_container_width=True)

st.divider()
st.caption("Team: Poppenspel Advies AI • Built for AMD Radeon GPUs & ROCm")