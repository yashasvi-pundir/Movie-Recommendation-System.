import pickle
import streamlit as st
import requests

st.header("Movies Recommendation System Using Machine Learning.")
movies=pickle.load(open('movies_list.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

movie_list=movies['title'].values
selected_movie=st.selectbox('Type or select a movie for recommendation',
             movie_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    recommended_movies_name=[]
    recommended_movies_poster=[]
    movies_list= sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    for i in movies_list:
        movie_id=movies.iloc[i[0]]['movie_id']
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name
    
        
def fetch_poster(movie_id):
    url="http://www.omdbapi.com/?i={movie_id}&apikey=18bb380".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data["Poster"]
    full_path="imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1._SX320.jpg"+poster_path
    return full_path
    
        
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters= recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    
