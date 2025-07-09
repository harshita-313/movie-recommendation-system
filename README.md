# 🎬 Movie Recommendation System

This is a simple movie recommendation system built using Python. It suggests movies that are similar to the one you select, based on the movie’s story, cast, director, genres, and keywords.

📖 Project Summary
This project starts by loading movie and credit data from the TMDB dataset. It then extracts useful information like the top 5 actors, director, genres, keywords, and movie overviews. After cleaning and combining all this information into one column called tags, the text is processed using NLP techniques like stemming and vectorization. A similarity matrix is created using cosine similarity, which helps compare how alike two movies are based on their content. The final system uses this matrix to recommend the top 10 most similar movies when a user selects or types in a movie name. All this logic is shown in the notebook, and there's also a Streamlit app file for a simple user interface to try it out.

## 📌 What It Does

- You choose a movie
- The system finds 10 similar movies
- It uses text analysis and compares movies using their content

---

## 📂 Files Included

| File Name | Purpose |
|-----------|---------|
| `movie_recommendation-system.ipynb` | The main Jupyter Notebook where everything is built step by step |
| `app-movie-recommendation.py` | A simple Streamlit app to get movie recommendations |
| `movies.pkl` | A saved file that contains movie titles |
| `similarity.pkl` | A saved file that helps compare movies (⚠️ too big for GitHub, download separately) |
| `tmdb_5000_movies.csv` & `tmdb_5000_credits.csv` | Movie data taken from Kaggle (link below) |

---

## 📥 Dataset Source

This project uses the **TMDB 5000 Movie Dataset** from Kaggle:  
🔗 [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

## 🚀 How To Run This Project

### 📌 Step 1: Download the Files
- Download all the files from this GitHub repo
- Also download the `similarity.pkl` file from Google Drive (because it's too big for GitHub):

👉 [Download similarity.pkl from Google Drive](https://drive.google.com/file/d/1wgiqmL60EGNI7Gman1RNlHfFi6iUrNZR/view?usp=sharing) 
Place it in the same folder as your notebook and app script.

---

### 🛠 Step 2: Install the Required Libraries
Open your terminal and run:
pip install pandas numpy scikit-learn nltk streamlit

📗 Step 3: Run the Jupyter Notebook
Open movie_recommendation-system.ipynb in Jupyter Notebook to see the full working and how recommendations are built.

▶️ Step 4: Run the Streamlit App (Optional)
If you want to run the app version:

streamlit run app-movie-recommendation.py

This will open a small web app on your browser.

🎯 Example Output
If you type or select "Avatar":

✅ Aliens vs Predator: Requiem  
✅ Independence Day  
✅ Jupiter Ascending  

