import streamlit as st
import os
import pygame

pygame.mixer.init()

mp3_files = [file for file in os.listdir("mp3_files") if file.endswith(".mp3")]
images = [file for file in os.listdir("Images") if file.endswith((".jpg"))]

song_to_album_art = {}
for song in mp3_files:
    song_name = os.path.splitext(song)[0]
    for album_art in images:
        if song_name in album_art:
            song_to_album_art[song] = album_art



with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def main():
    st.title("Music Player")
    st.header("Playing Now")


    st.sidebar.title("Play List")
    current_song_index = st.session_state.get("current_song_index", 0)
    song_selection = st.sidebar.radio("Select Song", mp3_files, index=current_song_index)
    st.sidebar.title(" ")
    st.sidebar.success(f"Now playing: {song_selection}")

    current_song = mp3_files[current_song_index]
    album_art_image = song_to_album_art.get(current_song, "default.gif")
    album_art_path = f"album_art/{album_art_image}"
    st.image(album_art_path, use_column_width=True)
    
    st.audio("mp3_files/" + song_selection, format="audio/mp3", start_time=0)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⏮️") and current_song_index > 0:
            current_song_index -= 1

        if st.button("stop"):
            current_song_index = 0

        if st.button("⏭️") and current_song_index < len(mp3_files) - 1:
            current_song_index += 1
    
        st.session_state.current_song_index = current_song_index

if __name__ == "__main__":
    main()

