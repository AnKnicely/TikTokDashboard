import streamlit as st
import pandas as pd

#load in data
df = pd.read_csv('tiktok_data.csv')
#This is the dashboard homepage

most_popular = df[df['playCount'] == df['playCount'].max()]
id = most_popular['id']
#use this id to find the file on desktop

st.title('Welcome to the Tik Tok Dashboard')
st.write('below.....')

col1, col2,col3 = st.columns(3)

col1.subheader('Most Popular Video')
video_file = open("6894081763379924229.mp4", 'rb')
video_bytes = video_file.read()
col1.video(video_bytes)

creator =  most_popular['authorMeta_name']
desc = most_popular['text']
col1.write(f"Creator Name: {most_popular['authorMeta_name'].values[0]}")
col1.write(f"Description: {most_popular['text'].values[0]} ")
col1.write(f"Play Count: {most_popular['playCount'].values[0]} ")


most_popular_song = df[df['playCount'] == df.groupby('musicMeta_musicName')['playCount'].transform('max')]
col3.subheader('The Most Popular Song')
col3.write(f"Audio Title: {most_popular_song['musicMeta_musicName'].values[0]}")
col3.write(f"Audio Creator: {most_popular_song['musicMeta_musicAuthor'].values[0]}")
col3.write(f"Audio Play Count: {most_popular_song['playCount'].values[0]}")



most_popular_tiktoker = df[df['playCount'] == df.groupby('authorMeta_name')['playCount'].transform('max')]
col2.subheader('Most Popular Creator')
col2.write(f"Creator Name: {most_popular_tiktoker['authorMeta_name'].values[0]}")
col2.write(f"Views: {most_popular_tiktoker['playCount'].values[0]}")
col2.write(f"Verified? {most_popular_tiktoker['authorMeta_verified'].values[0]}")
