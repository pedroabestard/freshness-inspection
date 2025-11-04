import streamlit as st
from model_helper import predict_image

st.title("Freshness Inspection")

uploaded_file = st.file_uploader("Upload the file", type=["jpg", "png", "jpeg"])


def get_nice_label(coded_label):
    if label.startswith('F_'):
        nice_label = 'Fresh ' + coded_label[2:]
    elif label.startswith('S_'):
        nice_label = 'Spoiled  ' + coded_label[2:]
    else:
        nice_label = coded_label  # Return the label as is if it doesn't start with F_ or S_

    return nice_label

if uploaded_file:
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        label, conf = predict_image(image_path)
        confidence = round(conf*100,1)
        st.info(f"Predicted Class: {get_nice_label(label)} with {confidence}% confidence.")
        st.image(uploaded_file, caption="Uploaded image", width='stretch')
