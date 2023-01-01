import librosa
import librosa.display
import numpy as np
import streamlit as st
from tensorflow.python.keras.models import load_model
import random
import os
from PIL import Image
import pandas as pd
#extract mfcc from the audio
trainpath= ("./bird_pics/")

# get the training classes
keys=os.listdir(trainpath)
values=range(len(keys))

bird_image = np.array(keys)
print(bird_image)
st.set_page_config(page_title="bird classification",page_icon="bird.ico")
excel_data=pd.read_excel("bird.xlsx")
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        .css-15tx938{
            display:none;
        }
        .uploadedFileData{
            font-weight:bold;
            color:green;
        }
        .css-1q1n0ol{
            visibility:hidden;
        }
        </style>
        """
stylesheet = """
        <style>
        *{
            color:black;
            font-family:Arial, Helvetica, sans-serif;
        }
        .block-container, .css-12oz5g7{
            max-width:90%;
            
        }
        .css-1v3fvcr {
            background-color: #fff;
            
        }
  
        .css-18ni7ap{
            background-color: #fff;

        }
        .css-15tx938{
            display:none;
        }
        .css-eczf16{
            display:none;
        }
        .css-8u98yl{
            width:100%;
            max-width:700px;
            margin:0 auto;
        }
        .css-1kyxreq{
            
            max-width:1000px;
        }
        .css-po3vlj{
            border:1px solid black;
            background:transparent;
            width:100%
            max-width:700px;
        }
        .css-po3vlj:focus{
            background:transparent;
            color:back;
            border:1px solid black;
            box-shadow:none;
        }
        .css-1cpxqw2{
            background:transparent;
            color:back;
            border:1px solid black;
        }
        .css-1cpxqw2:hover{
            background:black;
            color:white;
            border:1px solid white;
        }
        .uploadedFileData{
            font-weight:bold;
            color:green;
        }
        .css-1q1n0ol{
            visibility:hidden;
        }

        .row{
            display:flex;
            flex-direction:row;

        }
        .col-left,.col-right{
            display:flex;
            flex-direction:column;
        }
        .stAudio{
            position:absolute;
            z-index:1;
            bottom:60px;
            left:-2px;
            padding:5px;
            max-width:505px;
        }
        </style>
        """

about="<h1>Know any Unknown Birds</h1> "

st.markdown(about,unsafe_allow_html=True)
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.markdown(stylesheet, unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a file")
about_the_project="<div class='abp'><p>You can detect bird's voice by using this web app ......</p></div>"
st.markdown(about_the_project,unsafe_allow_html=True)
if uploaded_file is not None:
    after_upload_Stylesheet="""
    <style>
    .abp{
        display:none;
    }
    </style>
    
    """
    st.markdown(after_upload_Stylesheet,unsafe_allow_html=True)
    ran_number=random.randint(1,1000)
    #print(ran_number)
    #print(uploaded_file)
    audio_name='audio'+str(ran_number)+'.wav'
    with open(audio_name, mode='bx') as f:
        f.write(uploaded_file.getvalue())

    audio, sample_rate = librosa.load(audio_name,duration=5) 
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
    mfccs_scaled_features=mfccs_scaled_features.reshape(1,-1)
    m1=mfccs_scaled_features.reshape(1,-1)
    md=load_model("audio_classification.hdf5")
    s=md.predict_classes(m1)
    #type(s)
    classes=['grey-cheeked warbler' ,'grey-sided laughingthrush', 'grey-winged blackbird' ,'himalayan cuckoo' ,'indian spot-billed duck','mountain scops owl', 'mountain tailorbird', 'pale blue flycatcher','scaly laughingthrush']
    #print(classes[s[0]])
    
    container=f"<div class='row'><div class='col-left'>"
  
    predicted_bird=f"</div><div class='col-right'><h1 class='heading'>{classes[s[0]]}</h1><h3 class='snam'>Scientific Name:{excel_data['scname'][s[0]]}</h3></div></div>"
    st.markdown(container,unsafe_allow_html=True)
    st.markdown(predicted_bird,unsafe_allow_html=True)
    about_bird=f"<p class='about'>{excel_data['About'][s[0]]}</p>"
    st.text("\t")
    image=Image.open("bird_pics/"+bird_image[s[0]])

    
    col1, col2 = st.columns(2)
    with col1:
        audio_file = open(audio_name, 'rb')
        audio_bytes = audio_file.read()
        st.image(image,caption=classes[s[0]],width=500)
        st.audio(audio_bytes, format='audio/wav')
        
    with col2:
       
        st.markdown(about_bird,unsafe_allow_html=True)
    
    
