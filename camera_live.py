import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# video_file = open('myvideo.mp4', 'rb')
# video_bytes = video_file.read()

# st.video(video_bytes)
esp_cam_url = "http://192.168.1.101:81/stream"

with col1:
   st.image(esp_cam_url,caption='cam #1')

with col2:
   st.image(esp_cam_url,caption='cam #2')

with col3:
   st.image(esp_cam_url,caption='cam #3')
with col4:
   st.image(esp_cam_url,caption='cam #4')