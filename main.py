import io
import streamlit as st
from huggingface_hub import InferenceClient
import config

st.set_page_config(page_title="AI Avatar Creator", page_icon="🎨", layout="centered")

OPTIONS = {
    "avatar type": ["boy hero", "girl hero", "wizard", "robot explorer", "space warrior", "animal adventurer"],
    "hairstyle": ["short spiky hair", "curly hair", "long straight hair", "ponytail", "glowing hair", "helmet"],
    "outfit": ["superhero suit", "magical robe", "space armor", "casual hoodie", "battle costume", "royal outfit"],
    "expression": ["happy", "confident", "excited", "brave", "mysterious", "playful"],
    "background": ["forest", "space station", "magic castle", "city skyline", "rainbow world", "cloud kingdom"],
    "art style": ["cartoon style", "anime style", "3D game style", "fantasy illustration", "comic style"],
}

client = InferenceClient(api_key=config.HF_API_KEY)
st.session_state.setdefault("generated_image", None)

st.title("ZingQuark Avatar Creator 🎨")
st.write("Create your own avatar with advanced AI🤖")
st.markdown("Choose your avatar details or write your own custom prompr then click **Generate Avatar**.")
st.subheader("⚙ Create your Avatar")

mode = st.selectbox("Choose prompt mode", ["Use Avatar Builder", "Write Custom Prompt"])

if mode == "Use Avatar Builder":
    values = {k: st.selectbox(f"Choose {k}",v) for k, v in OPTIONS.items()}
    extra = st.text_input("Add one extra detail (optional)", placeholder="Example: glowing red eyes").strip()
    prompt = (
        f"A kid-friendly {values['avatar type']},"
        f"with {values['hairstyle'],}"
        f"wearing {values['outfit'],}"
        f"with a {values['expression']} expression,"
        f"in a {values['background']} background,"
        f"{values['art style']}, colourful, highly detailed digital art pfp"
    )    
    final_prompt = f"{prompt}, {extra}" if extra else prompt
else:
    final_prompt = st.text_area(
        "Write your own prompt!",
        placeholder="Example: Pikachu with glasses",
        height=150,
    ).strip()
with st.expander("👁 See the AI prompt"):
    st.write(final_prompt or "Your prompt should be here...")
if st.button("😎 Generate your Avatar or logo"):
    if not config.HF_API_KEY:
        st.error("Server issue please inform ZingQuark team at zingquark102@gmail.com")
    elif not final_prompt:
        st.warning("Please create or enter a prompt first!!")   
    else:
        with st.spinner("Creating your avatar✨"): 
            try:
                st.session_state.generated_image = client.text_to_image(
                    prompt=final_prompt,
                    model=config.HF_IMAGE_MODEL,
                )    
                st.success("Your avatar is done and ready!")
            except Exception as e:
                st.error(f"Your avatar doesn't feel right. Unable to generate. {e}")
if st.session_state.generated_image:
    st.image(st.session_state.generated_image, caption="Your AI Avatar")
    buffer = io.BytesIO()
    st.session_state.generated_image.save(buffer, format="PNG")         
    st.download_button(
        "✔ Download by clicking this button."
        data=buffer.getvalue()
        file_name="ZINGQUARKAVATAR1.png"
        mime="image/png"
    )       
            
# -------------------------------
# Next Steps:
# 1. Add UI elements (title, description, and instructions)
# 2. Create prompt mode selection (Avatar Builder / Custom Prompt)
# 3. Build avatar input fields using OPTIONS
# 4. Generate final prompt based on user input
# 5. Show prompt preview (optional)
# 6. Add button to generate avatar using Hugging Face model
# 7. Display generated image
# 8. Add download button for the image
# -------------------------------