import tensorflow as tf
from tensorflow.keras import preprocessing 
import streamlit as st
import numpy as np
import webbrowser
from PIL import Image

url = "https://github.com/NavinBondade/Classifying-Five-Rice-Crop-Diseases-With-Deep-Learning"
data = 'https://www.kaggle.com/raddar/tuberculosis-chest-xrays-shenzhen'


st.set_page_config(page_title='Rice Crop Diseases Identification Tool', initial_sidebar_state = 'auto')
st.title("Rice Crop Diseases Identification Tool")
st.write("A machine learning powered system that tells accurately whether a rice crop is infected with Gudi Rotten, Apex Blast, Leaf Blast, Leaf Burn or Neck Blast Paddy. Check out code here [link](%s)." % url)

with open("Data.zip", "rb") as fp:
    col1, col2, col3 = st.columns(3)
    with col2:
        btn = st.download_button(
        label="Download Test Data",
        data=fp,
        file_name="Data.zip",
        mime="application/zip"
        )

 

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)        

file = st.sidebar.file_uploader("Upload Image", type=['jpeg','jpg','png'])

cat = ['Gudi Rotten', 'Apex Blast', 'Leaf Blast', 'Leaf Burn', 'Neck Blast Paddy']

def prediction(image, model):
    test_image = image.resize((150,150))
    test_image = preprocessing.image.img_to_array(test_image)
    test_image = test_image / 255.0
    test_image = np.expand_dims(test_image, axis=0)
    result=model.predict(test_image)
    result=np.argmax(result)
    Pred=cat[result]
    return Pred



if file is not None:
    img = Image.open(file)
    model = tf.keras.models.load_model("Rice_Diseases.h5")
    img_jpeg = img.convert('RGB')
    pred = prediction(img_jpeg, model)
    #score = tf.nn.softmax(prediction[0])
    st.markdown(f"<h2 style='text-align: center; color: black;'>{pred}</h2>", unsafe_allow_html=True)
    st.image(img, use_column_width=True)
    






