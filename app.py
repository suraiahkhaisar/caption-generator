import streamlit as st
from PIL import Image
st.title("hello page")
st.write("upload a image")
upload_file=st.file_uploader("choose your file....",type=["jpg","jpeg","png"])
if upload_file is not None:
  st.success("successfully uploaded")
  image=Image.open(upload_file)
  st.image(image,caption="uploaded image")
  
