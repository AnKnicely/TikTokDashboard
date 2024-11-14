
import pandas as pd
import json

file_path = "trending.json"

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

df = pd.json_normalize(data['collector'], sep = '_',
                       record_path= None,
                       meta = ['id','text','createTime'],
                       meta_prefix= 'post_',
                       record_prefix='music_',
                       errors='ignore')

df = pd.json_normalize(df.to_dict(orient='records'), sep = '_')
def clean_data (df):
    simplified_df = df[
    ['id','text','playCount','shareCount','commentCount','authorMeta_name','authorMeta_nickName','authorMeta_verified',
     'musicMeta_musicName', 'musicMeta_musicAuthor','musicMeta_musicOriginal','videoMeta_duration']
    ]
    return simplified_df

simplified_df = clean_data(df) 
simplified_df.head()
simplified_df.to_csv('tiktok_data.csv', index = False)