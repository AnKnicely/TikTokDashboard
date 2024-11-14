import streamlit as st
import pandas as pd

#load in data
df = pd.read_csv('tiktok_data.csv')
#This is the dashboard homepage

most_popular = df[df['playCount'] == df['playCount'].max()]
id = most_popular['id']
#use this id to find the file on desktop

st.title('The most Popular video is:')
video_file = open("6894081763379924229.mp4", 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

creator =  most_popular['authorMeta_name']
desc = most_popular['text']
st.write(creator)
st.write(desc)
st.write(most_popular['playCount'])

#TO DO: Find the most popular video and find the most popular song
#most popular tiktoker

col1, col2 = st.columns(2)
most_popular_song = df[df['playCount'] == df.groupby('musicMeta_musicName')['playCount'].transform('max')]
col1.subheader('The Most Popular Song')
col1.write(f"Audio Title: {most_popular_song['musicMeta_musicName'].values[0]}")
col1.write(f"Audio Play Count: {most_popular_song['playCount'].values[0]}")


print(most_popular_song)
most_popular_tiktoker = df[df['playCount'] == df.groupby('authorMeta_name')['playCount'].transform('max')]

most_popular_song = df[df['playCount'] == df.groupby('musicMeta_musicName')['playCount'].transform('max')]
#col1.subheader('The Most Popular Song')
#col1.write(f"Audio Title: {most_popular_song['musicMeta_musicName'].values[0]}")
#col1.write(f"Audio Play Count: {most_popular_song['playCount'].values[0]}")

print('help')
print(most_popular_song)
most_popular_tiktoker = df[df['playCount'] == df.groupby('authorMeta_name')['playCount'].transform('max')]
