import streamlit as st
import pandas as pd
import numpy as np
import chess
import chess.svg
import random
from PIL import Image
from io import BytesIO

st.title('Chess Upsets')

RAW_DATA_URL = 'games.csv'
UPSET_DATA = 'upset_dataset.csv'

# unused at the moment
df = pd.read_csv(RAW_DATA_URL)
COLUMNS = df.columns


@st.cache_data
def load_data(DATA, nrows):
    data = pd.read_csv(DATA, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data


# gets both datasets
data_load_state = st.text('Loading data...')
raw_data = load_data(RAW_DATA_URL, 20000)  # dataset has ~20000
upset_data = load_data(UPSET_DATA, 10000)
upset_data = upset_data.drop(columns=["index", "unnamed: 0"])

# displays 2 datasets
if st.checkbox('Show raw chess data'):
    st.subheader('Raw data')
    st.write(raw_data)

if st.checkbox('Show processed upsets'):
    st.subheader('Processed data - This is what we will be using')
    st.write(upset_data)


# generates a random match from the upset dataset
def get_rand_match():
    st.write(upset_data.iloc[[random.randint(0, 546)]])  # 545 elements


st.subheader("Let's look at a random match!")
st.button('Click me', on_click=get_rand_match)
st.write("Note: result is generated on the top of the screen")

# Searches a player
players_upset = pd.concat([upset_data['white_id'], upset_data['black_id']]).drop_duplicates()
st.subheader("Below are the usernames that are within the dataset. \n Specifically the 'interesting' players")
st.write(players_upset)

st.subheader("Search a match!")
user_input = st.text_input("Enter in a number ranging from 0 - 545 or a player_id:")
if user_input:
    st.subheader('Match Information')

    try:
        match_history = upset_data.iloc[[int(user_input)]]
        st.text(f"Let's see match {user_input}!")
        st.write(match_history)
        st.write(match_history["moves"])

    except:
        st.text(f"Let's see '{user_input}' match history!")
        result = upset_data.query(f'((white_id == "{user_input}") or (black_id == "{user_input}"))')
        st.write(result)
        st.write(result["moves"])

# streamlit does not process the chess board visualization, code below is irrelavent
def show_board():

    print(board)
def play_chess_game(moves):
    board = chess.Board()
    images = []

    for move in moves:
        try:
            board.push_san(move)

            # Convert chessboard to SVG and then to an image
            svg_board = chess.svg.board(board=board)
            print(svg_board)
            # Append the image to the list
            #images.append(image)
        except ValueError:
            st.error(f"Invalid move: {move}")
            break

    return images

board = chess.Board()
st.write(board)