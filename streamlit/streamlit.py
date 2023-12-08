import streamlit as st
import pandas as pd
import numpy as np

st.title('Chess Upsets')

RAW_DATA_URL = 'games.csv'
UPSET_DATA = 'upset_dataset.csv'
df = pd.read_csv(RAW_DATA_URL)
COLUMNS = df.columns


@st.cache_data
def load_data(DATA,nrows):
    data = pd.read_csv(DATA, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data


data_load_state = st.text('Loading data...')
raw_data = load_data(RAW_DATA_URL, 10000)   #dataset has ~20000

upset_data = load_data(UPSET_DATA, 10000)

if st.checkbox('Show raw chess data'):
    st.subheader('Raw data')
    st.write(raw_data)

if st.checkbox('Show processed upsets'):
    st.subheader('Processed data')
    st.write(upset_data)

players = pd.concat([raw_data['white_id'], raw_data['black_id']]).value_counts(ascending=True).tail(20)

st.subheader("Below are the usernames that are within the dataset. \n Specifically the 'interesting' players")
st.write((pd.concat([upset_data['white_id'], upset_data['black_id']]).drop_duplicates()))

st.subheader("Search a Player!")
user_input = st.text_input("Enter in a number ranging from 0 - 9,999 or a player_id to look for a match:")
if user_input:
        st.subheader('Match Information')
        st.text(f"You entered: {user_input}. Let's see the matche(s)!")
        try:
            match_history = raw_data.iloc[[int(user_input)]]
            st.write(match_history)

            st.write(match_history["moves"])
        except:
            result = raw_data.query(f'(white_id == "{user_input}" or black_id == "{user_input}")')
            st.write(result)
            st.write(result["moves"])

