# Import necessary packages
import streamlit as st
from tensorflow import keras
from PIL import Image
import numpy as np

st.title("Computer Vision: X-ray Classifier")
st.text("Created by Vitor Abdo")


@st.cache(allow_output_mutation=True)
def teachable_machine_classification(img, weights_file):
    # Load the model
    model = keras.models.load_model(weights_file)

    test_image = image.resize((150, 150))
    test_image = np.array(test_image)
    test_image = np.expand_dims(test_image, axis=0)

    # run the inference
    prediction_percentage = model.predict(test_image)
    prediction = prediction_percentage.round()

    return prediction, prediction_percentage


uploaded_file = st.file_uploader("Choose a chest X-ray Image...", type=["png","jpg","jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded file', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label, perc = teachable_machine_classification(image, 'my_keras_model.h5')

    if label == 1:
        st.write("Its Normal, confidence level:", perc)

    else:
        st.write("Its Pneumonia, confidence level:", 1 - perc)


