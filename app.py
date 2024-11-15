import streamlit as st
import pandas as pd
import plotly.express as px

#load in data
df = pd.read_csv('tiktok_data.csv')

#Setting the sidebar
#st.set_page_config(layout='wide')
st.sidebar.markdown("<img src= 'https://w7.pngwing.com/pngs/959/454/png-transparent-tiktok-logo-thumbnail.png' width = 50/><h1 style = 'display:inline-block'>Welcome to the Tik Tok Dashboard</h1>", unsafe_allow_html=True )
st.sidebar.markdown("This dashboard contains many different statistics and analysis performed on a Tik Tok Dataset")
st.sidebar.markdown("<p> Each page has different graphs that can be interacted with via: <ul><li>Clicking on the graph</li><li>Clicking and dragging on the graph</li><li>Using the UI buttons on top of the graph</li></ol></p>", unsafe_allow_html = True)
st.sidebar.markdown("Pages can be changed via the drop down menu named 'Menu'")

page = st.selectbox("Menu:", ["Homepage","Sound Analytics","Contact Us"])
if page == "Homepage":

    st.html("<h3> All About the Data </h3><p> This dataset was created by Erik van de Ven. It contains 1,000 different values for trending Tik Toks from 2020. Each cell gives information on the creator, audio used, view count, share count, and comment count. </p>")

    fig = px.histogram(df, x='text', y='playCount')
    st.plotly_chart(fig, use_container_width=True)


    col1, col2,col3 = st.columns(3)
    st.html("<br> </br>")
    st.html("<br> </br>")
    #use this id to find the file on desktop
    most_popular = df[df['playCount'] == df['playCount'].max()]
    id = most_popular['id']
    #uploading the file for the most popular video
    col1.subheader('Most Popular Video')
    video_file = open("6894081763379924229.mp4", 'rb')
    video_bytes = video_file.read()
    col1.video(video_bytes)

    #Creation of description for the most popular video
    col1.write(f"Creator Name: {most_popular['authorMeta_name'].values[0]}")
    col1.write(f"Description: {most_popular['text'].values[0]} ")
    col1.write(f"Play Count: {most_popular['playCount'].values[0]} ")

    #creation of description for the most popular sound
    most_popular_song = df[df['playCount'] == df.groupby('musicMeta_musicName')['playCount'].transform('max')]
    col3.subheader('The Most Popular Song')
    col3.image("images.jpg", caption="Pop Smoke - Elements", width = 250)
    col3.write(f"Audio Title: {most_popular_song['musicMeta_musicName'].values[0]}")
    col3.write(f"Audio Creator: {most_popular_song['musicMeta_musicAuthor'].values[0]}")
    col3.write(f"Audio Play Count: {most_popular_song['playCount'].values[0]}")


    #Creation of description for the most popular creator
    most_popular_tiktoker = df[df['playCount'] == df.groupby('authorMeta_name')['playCount'].transform('max')]
    col2.subheader('Most Popular Creator')
    col2.write(f"Creator Name: {most_popular_tiktoker['authorMeta_name'].values[0]}")
    col2.write(f"Video Count: {most_popular_tiktoker['playCount'].values[0]}")
    col2.write(f"Verified? {most_popular_tiktoker['authorMeta_verified'].values[0]}")
elif page == "Sound Analytics":
    audio = st.text_input('Search for a specific audio', value = "")

    #Button
    if st.button('Get data'):
    #run after button is pressed
        st.write(audio)
        filtered_df = df[df['musicMeta_musicName'].str.contains(audio,case= False, na= False)]
        if filtered_df.empty:
            st.write("There is no data for this audio")
        else:
            st.write(filtered_df)
        df

    #Visuals
        fig = px.histogram(filtered_df, x='musicMeta_musicName', y= 'playCount')
        st.plotly_chart(fig, use_container_width= True)

        left_col, right_col = st.columns(2)
        scatter1 = px.scatter(filtered_df, x = 'commentCount', y= 'shareCount')
        left_col.plotly_chart(scatter1, use_container_width=True)
        
        scatter2 = px.scatter(filtered_df, x = 'shareCount', y= 'playCount')
        right_col.plotly_chart(scatter2, use_container_width=True)
    
elif page == "Contact Us":
    st.write("Hello")
        
