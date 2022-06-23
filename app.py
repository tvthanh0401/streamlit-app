import streamlit as st
import pandas as pd
import time
col1, col2 = st.columns([4, 2])

tracks = []
with open('./video_output.txt', 'r') as track_file:
    for line in track_file:
        track_time, track_desc = line.split(';')
        tracks_time = int(track_time)
        tracks.append((tracks_time, track_desc))
st.markdown("""
<style>
.css-1r6slb0 {
    overflow-x:scroll;
    height: 600px;
}
</style>
""",unsafe_allow_html=True)
with col1:
    st.header('Video output')
    output_video = st.empty()
    output_video.video('./video_output.webm')

with col2:
    st.header('List of event')
    with st.container():
        for track in tracks:
            if st.button(f'00:00:{str(track[0]).zfill(2)} {track[1]}'):
                output_video.text('Please wait')
                time.sleep(0.5)
                output_video.video('./video_output.webm', start_time=track[0])
