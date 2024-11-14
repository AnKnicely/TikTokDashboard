import streamlit as st
import pandas as pd
import plotly.express as px

#importing the dataset
file_path = 'tiktok_data.csv'
df = pd.read_csv(file_path, index_col=False)

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

    #Vizuals
    fig = px.histogram(filtered_df, x='musicMeta_musicName', y= 'playCount')
    st.plotly_chart(fig, use_container_width= True)

    left_col, right_col = st.columns(2)
    

