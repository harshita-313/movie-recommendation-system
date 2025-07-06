import streamlit as st
import pickle
import pandas as pd

# Load preprocessed data and similarity matrix
movies = pickle.load(open('movies.pkl', 'rb'))   # should contain the dataframe with 'title'
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    return [movies.iloc[i[0]].title for i in movie_list]

# Streamlit app
st.title('Movie Recommender System')

selected_movie = st.selectbox('Select a movie:', movies['title'].values)

if st.button('Show Recommendations'):
    recommendations = recommend(selected_movie)
    st.write("### Recommended Movies:")
    for title in recommendations:
        st.write(title)
