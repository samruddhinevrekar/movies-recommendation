# # # # # import streamlit as st
# # # # # import pandas as pd
# # # # # import sqlite3

# # # # # # Function to establish database connection
# # # # # def get_connection():
# # # # #     conn = sqlite3.connect('tutorial.db')
# # # # #     return conn

# # # # # # Function to get similar movies based on scores
# # # # # def get_similar_movies(movie_name, rating):
# # # # #     similar_ratings = corrMatrix[movie_name] * (rating - 2.5)
# # # # #     similar_ratings = similar_ratings.sort_values(ascending=False)
# # # # #     return similar_ratings

# # # # # # Reading all parquet data files
# # # # # #movie_df = pd.read_parquet(path= "movies.parquet", engine='auto')
# # # # # corrMatrix = pd.read_parquet(path="corrmatrix.parquet", engine="auto")
# # # # # merged = pd.read_parquet(path="movie_rating.parquet", engine="auto")

# # # # # # Title of the app
# # # # # st.title("Movie Recommendation System")

# # # # # # Enter user id
# # # # # st.header("Enter User ID:")
# # # # # userid = st.number_input(label="User ID", step=1)
# # # # # userid = int(userid)

# # # # # # Check if the user ID is present in the movie_ratings table
# # # # # with get_connection() as conn:
# # # # #     c = conn.cursor()
# # # # #     c.execute("SELECT * FROM movie_ratings WHERE userid = ?", (userid,))
# # # # #     existing_user = c.fetchone()
# # # # #     if existing_user:
# # # # #         st.write("Existing user.")
# # # # #     else:
# # # # #         st.write("New user.")

# # # # # # Functions to perform
# # # # # st.header("Function to perform")
# # # # # selected_move = st.selectbox("Select a Move", options=[None, "Get Suggestions", "Update Ratings", "Delete user", "Add Movie"])


# # # # # #get movie suggestions
# # # # # if selected_move == "Get Suggestions":
# # # # #     # Movie rating section
# # # # #     st.header("Rate Movie:")

# # # # #     with get_connection() as conn:
# # # # #         c = conn.cursor()
# # # # #         c.execute("SELECT DISTINCT title FROM movie_ratings")
# # # # #         movie_titles = [row[0] for row in c.fetchall()]

# # # # #     selected_movie = st.selectbox("Select a Movie",movie_titles)
# # # # #     rating = st.slider("Rate this movie (1-5)", 1, 5)

# # # # #     if st.button("Submit and get Recommendations"):
# # # # #         with get_connection() as conn:
# # # # #             c = conn.cursor()
# # # # #             c.execute("INSERT INTO movie_ratings (userid, title, rating) VALUES (?, ?, ?)", 
# # # # #                       (userid, selected_movie, rating))
# # # # #             conn.commit()
# # # # #             temp_df = get_similar_movies(selected_movie, rating)
# # # # #             st.write(temp_df.head())
# # # # #             st.success(f"Your rating for '{selected_movie}' has been submitted.")

# # # # # elif selected_move == "Update Ratings":
# # # # #     st.header("Search Movie:")

# # # # #     with get_connection() as conn:
# # # # #         c = conn.cursor()
# # # # #         c.execute("SELECT DISTINCT title FROM movie_ratings")
# # # # #         movie_titles = [row[0] for row in c.fetchall()]

# # # # #     selected_movie = st.selectbox("Select a Movie", movie_titles)
# # # # #     rating = st.slider("Rate this movie (1-5)", 1, 5)
# # # # #     if st.button("Update Rating"):
# # # # #         with get_connection() as conn:
# # # # #             c = conn.cursor()
# # # # #             c.execute("SELECT * FROM movie_ratings WHERE userid = ? AND title = ?", (userid, selected_movie))
# # # # #             existing_rating = c.fetchone()
# # # # #             if existing_rating:
# # # # #                 # Updating rating
# # # # #                 c.execute("UPDATE movie_ratings SET rating = ? WHERE userid = ? AND title = ?",
# # # # #                           (rating, userid, selected_movie))
# # # # #                 conn.commit()
# # # # #                 st.success(f"Your rating for '{selected_movie}' has been updated.")
# # # # #             else:
# # # # #                 # Inserting the new rating
# # # # #                 c.execute("INSERT INTO movie_ratings (userid, title, rating) VALUES (?, ?, ?)",
# # # # #                           (userid, selected_movie, rating))
# # # # #                 conn.commit()
# # # # #                 st.success(f"Your rating for '{selected_movie}' has been submitted.")

# # # # # elif selected_move == "Delete user":
# # # # #     if st.button("Delete User"):
# # # # #         # Deleting the user from the database
# # # # #         with get_connection() as conn:
# # # # #             c = conn.cursor()
# # # # #             c.execute("DELETE FROM movie_ratings WHERE userid = ?", (userid,))
# # # # #             conn.commit()
# # # # #             st.success(f"User with ID {userid} has been deleted.")

# # # # # elif selected_move == "Add Movie":
# # # # #     st.header("Add Movie:")
# # # # #     movie_id = st.number_input(label="Enter Movie ID", step=1)
# # # # #     movie_title = st.text_input(label="Enter Movie Title")

# # # # #     if st.button("Add Movie"):
# # # # #         # Insert the movie into the database
# # # # #         with get_connection() as conn:
# # # # #             c = conn.cursor()
# # # # #             c.execute("INSERT INTO movie_ratings (movieid, title) VALUES (?, ?)",
# # # # #                       (movie_id, movie_title))
# # # # #             conn.commit()
# # # # #             st.success(f"Movie with ID {movie_id} has been added to the database.")

# # # # # #if st.button("Update Cosine Similarity Matrix"):
    
# # # # # #    st.write("popo")
# # # # # #    corrMatrix = pd.DataFrame(cosine_similarity(sparse_df), index=user_ratings.columns, columns=user_ratings.columns)


# # # # # c.close()

# # # # import streamlit as st
# # # # import pandas as pd
# # # # import sqlite3
# # # # import streamlit as st

# # # # # Function to establish database connection
# # # # def get_connection():
# # # #     conn = sqlite3.connect('tutorial.db')
# # # #     return conn

# # # # # Function to get similar movies based on scores
# # # # def get_similar_movies(movie_name, rating):
# # # #     similar_ratings = corrMatrix[movie_name] * (rating - 2.5)
# # # #     similar_ratings = similar_ratings.sort_values(ascending=False)
# # # #     return similar_ratings

# # # # # Reading all parquet data files
# # # # # movie_df = pd.read_parquet(path= "movies.parquet", engine='auto')
# # # # corrMatrix = pd.read_parquet(path="corrmatrix.parquet", engine="auto")
# # # # merged = pd.read_parquet(path="movie_rating.parquet", engine="auto")

# # # # # Title of the app
# # # # st.title("Movie Recommendation System")

# # # # # Enter user id
# # # # st.sidebar.header("Enter User ID:")
# # # # userid = st.sidebar.number_input(label="User ID", step=1)
# # # # userid = int(userid)

# # # # # Check if the user ID is present in the movie_ratings table
# # # # with get_connection() as conn:
# # # #     c = conn.cursor()
# # # #     c.execute("SELECT * FROM movie_ratings WHERE userid = ?", (userid,))
# # # #     existing_user = c.fetchone()
# # # #     if existing_user:
# # # #         st.write("Existing user.")
# # # #     else:
# # # #         st.write("New user.")

# # # # # Functions to perform
# # # # st.sidebar.header("Function to perform")
# # # # selected_move = st.sidebar.selectbox("Select a Move", options=[None, "Get Suggestions", "Update Ratings", "Delete user", "Add Movie"])

# # # # # get movie suggestions
# # # # if selected_move == "Get Suggestions":
# # # #     # Movie rating section
# # # #     st.header("Rate Movie:")

# # # #     with get_connection() as conn:
# # # #         c = conn.cursor()
# # # #         c.execute("SELECT DISTINCT title FROM movie_ratings")
# # # #         movie_titles = [row[0] for row in c.fetchall()]

# # # #     selected_movie = st.selectbox("Select a Movie", movie_titles)
# # # #     rating = st.slider("Rate this movie (1-5)", 1, 5)

# # # #     if st.button("Submit and get Recommendations"):
# # # #         with get_connection() as conn:
# # # #             c = conn.cursor()
# # # #             c.execute("INSERT INTO movie_ratings (userid, title, rating) VALUES (?, ?, ?)", 
# # # #                       (userid, selected_movie, rating))
# # # #             conn.commit()
# # # #             temp_df = get_similar_movies(selected_movie, rating)
# # # #             st.write(temp_df.head())
# # # #             st.success(f"Your rating for '{selected_movie}' has been submitted.")

# # # # elif selected_move == "Update Ratings":
# # # #     st.header("Search Movie:")

# # # #     with get_connection() as conn:
# # # #         c = conn.cursor()
# # # #         c.execute("SELECT DISTINCT title FROM movie_ratings")
# # # #         movie_titles = [row[0] for row in c.fetchall()]

# # # #     selected_movie = st.selectbox("Select a Movie", movie_titles)
# # # #     rating = st.slider("Rate this movie (1-5)", 1, 5)
# # # #     if st.button("Update Rating"):
# # # #         with get_connection() as conn:
# # # #             c = conn.cursor()
# # # #             c.execute("SELECT * FROM movie_ratings WHERE userid = ? AND title = ?", (userid, selected_movie))
# # # #             existing_rating = c.fetchone()
# # # #             if existing_rating:
# # # #                 # Updating rating
# # # #                 c.execute("UPDATE movie_ratings SET rating = ? WHERE userid = ? AND title = ?",
# # # #                           (rating, userid, selected_movie))
# # # #                 conn.commit()
# # # #                 st.success(f"Your rating for '{selected_movie}' has been updated.")
# # # #             else:
# # # #                 # Inserting the new rating
# # # #                 c.execute("INSERT INTO movie_ratings (userid, title, rating) VALUES (?, ?, ?)",
# # # #                           (userid, selected_movie, rating))
# # # #                 conn.commit()
# # # #                 st.success(f"Your rating for '{selected_movie}' has been submitted.")

# # # # elif selected_move == "Delete user":
# # # #     if st.button("Delete User"):
# # # #         # Deleting the user from the database
# # # #         with get_connection() as conn:
# # # #             c = conn.cursor()
# # # #             c.execute("DELETE FROM movie_ratings WHERE userid = ?", (userid,))
# # # #             conn.commit()
# # # #             st.success(f"User with ID {userid} has been deleted.")

# # # # elif selected_move == "Add Movie":
# # # #     st.header("Add Movie:")
# # # #     movie_id = st.number_input(label="Enter Movie ID", step=1)
# # # #     movie_title = st.text_input(label="Enter Movie Title")

# # # #     if st.button("Add Movie"):
# # # #         # Insert the movie into the database
# # # #         with get_connection() as conn:
# # # #             c = conn.cursor()
# # # #             c.execute("INSERT INTO movie_ratings (movieid, title) VALUES (?, ?)",
# # # #                       (movie_id, movie_title))
# # # #             conn.commit()
# # # #             st.success(f"Movie with ID {movie_id} has been added to the database.")

# # # # c.close()


# # # import streamlit as st
# # # import pandas as pd
# # # import sqlite3

# # # # Function to establish database connection
# # # def get_connection():
# # #     conn = sqlite3.connect('tutorial.db')
# # #     return conn

# # # # Function to get similar movies based on scores
# # # def get_similar_movies(movie_name, rating):
# # #     similar_ratings = corrMatrix[movie_name] * (rating - 2.5)
# # #     similar_ratings = similar_ratings.sort_values(ascending=False)
# # #     return similar_ratings

# # # # Reading all parquet data files
# # # # movie_df = pd.read_parquet(path= "movies.parquet", engine='auto')
# # # corrMatrix = pd.read_parquet(path="corrmatrix.parquet", engine="auto")
# # # merged = pd.read_parquet(path="movie_rating.parquet", engine="auto")

# # # # Title of the app
# # # st.title("Movie Recommendation System")

# # # # Enter user id
# # # st.sidebar.header("Enter User ID:")
# # # userid = st.sidebar.number_input(label="User ID", step=1)
# # # userid = int(userid)

# # # # Check if the user ID is present in the movie_ratings table
# # # with get_connection() as conn:
# # #     c = conn.cursor()
# # #     c.execute("SELECT * FROM movie_ratings WHERE userid = ?", (userid,))
# # #     existing_user = c.fetchone()
# # #     if existing_user:
# # #         st.write("Existing user.")
# # #     else:
# # #         st.write("New user.")

# # # # Functions to perform
# # # st.sidebar.header("Function to perform")
# # # selected_move = st.sidebar.selectbox("Select a Move", options=[None, "Get Suggestions", "Update Ratings", "Delete user", "Add Movie"])

# # # # get movie suggestions
# # # if selected_move == "Get Suggestions":
# # #     # Movie rating section
# # #     st.header("Rate Movie:")

# # #     with get_connection() as conn:
# # #         c = conn.cursor()
# # #         c.execute("SELECT DISTINCT title FROM movie_ratings")
# # #         movie_titles = [row[0] for row in c.fetchall()]

# # #     selected_movie = st.selectbox("Select a Movie", movie_titles)
# # #     rating = st.slider("Rate this movie (1-5)", 1, 5)

# # #     if st.button("Submit and get Recommendations"):
# # #         with get_connection() as conn:
# # #             c = conn.cursor()
# # #             c.execute("INSERT INTO movie_ratings (userid, title, rating) VALUES (?, ?, ?)", 
# # #                       (userid, selected_movie, rating))
# # #             conn.commit()
# # #             temp_df = get_similar_movies(selected_movie, rating)
# # #             st.write(temp_df.head())
# # #             st.success(f"Your rating for '{selected_movie}' has been submitted.")

# # # elif selected_move == "Update Ratings":
# # #     st.header("Search Movie:")

# # #     with get_connection() as conn:
# # #         c = conn.cursor()
# # #         c.execute("SELECT DISTINCT title FROM movie_ratings")
# # #         movie_titles = [row[0] for row in c.fetchall()]

# # #     selected_movie = st.selectbox("Select a Movie", movie_titles)
# # #     rating = st.slider("Rate this movie (1-5)", 1, 5)
# # #     if st.button("Update Rating"):
# # #         with get_connection() as conn:
# # #             c = conn.cursor()
# # #             c.execute("SELECT * FROM movie_ratings WHERE userid = ? AND title = ?", (userid, selected_movie))
# # #             existing_rating = c.fetchone()
# # #             if existing_rating:
# # #                 # Updating rating
# # #                 c.execute("UPDATE movie_ratings SET rating = ? WHERE userid = ? AND title = ?",
# # #                           (rating, userid, selected_movie))
# # #                 conn.commit()
# # #                 st.success(f"Your rating for '{selected_movie}' has been updated.")
# # #             else:
# # #                 # Inserting the new rating
# # #                 c.execute("INSERT INTO movie_ratings (userid, title, rating) VALUES (?, ?, ?)",
# # #                           (userid, selected_movie, rating))
# # #                 conn.commit()
# # #                 st.success(f"Your rating for '{selected_movie}' has been submitted.")

# # # elif selected_move == "Delete user":
# # #     if st.button("Delete User"):
# # #         # Deleting the user from the database
# # #         with get_connection() as conn:
# # #             c = conn.cursor()
# # #             c.execute("DELETE FROM movie_ratings WHERE userid = ?", (userid,))
# # #             conn.commit()
# # #             st.success(f"User with ID {userid} has been deleted.")

# # # elif selected_move == "Add Movie":
# # #     st.header("Add Movie:")
# # #     with st.form(key='add_movie_form'):
# # #         movie_id = st.number_input(label="Enter Movie ID", step=1)
# # #         movie_title = st.text_input(label="Enter Movie Title")
# # #         submit_button = st.form_submit_button(label='Add Movie')

# # #         if submit_button:
# # #             # Insert the movie into the database
# # #             with get_connection() as conn:
# # #                 c = conn.cursor()
# # #                 c.execute("INSERT INTO movie_ratings (movieid, title) VALUES (?, ?)",
# # #                           (movie_id, movie_title))
# # #                 conn.commit()
# # #                 st.success(f"Movie with ID {movie_id} has been added to the database.")

# # # c.close()

# # import streamlit as st
# # import pandas as pd
# # import sqlite3

# # # Function to establish database connection
# # def get_connection():
# #     conn = sqlite3.connect('tutorial.db')
# #     return conn

# # # Function to get similar movies based on scores
# # def get_similar_movies(movie_name, rating):
# #     similar_ratings = corrMatrix[movie_name] * (rating - 2.5)
# #     similar_ratings = similar_ratings.sort_values(ascending=False)
# #     return similar_ratings

# # # Reading all parquet data files
# # # movie_df = pd.read_parquet(path= "movies.parquet", engine='auto')
# # corrMatrix = pd.read_parquet(path="corrmatrix.parquet", engine="auto")
# # merged = pd.read_parquet(path="movie_rating.parquet", engine="auto")

# # # Title of the app
# # st.title("Movie Recommendation System")

# # # Sidebar - Enter user id
# # with st.sidebar:
# #     st.header("Enter User ID:")
# #     userid = st.number_input(label="User ID", step=1)
# #     userid = int(userid)

# #     # Check if the user ID is present in the movie_ratings table
# #     with get_connection() as conn:
# #         c = conn.cursor()
# #         c.execute("SELECT * FROM movie_ratings WHERE userid = ?", (userid,))
# #         existing_user = c.fetchone()
# #         if existing_user:
# #             st.write("Existing user.")
# #         else:
# #             st.write("New user.")

# # # Sidebar - Functions to perform
# # with st.sidebar:
# #     st.header("Function to perform")
# #     selected_move = st.selectbox("Select a Move", options=[None, "Get Suggestions", "Update Ratings", "Delete user", "Add Movie"])

# # # Main content area
# # if selected_move == "Get Suggestions":
# #     # Movie rating section
# #     st.header("Rate Movie:")

# #     with get_connection() as conn:
# #         c = conn.cursor()
# #         c.execute("SELECT DISTINCT title FROM movie_ratings")
# #         movie_titles = [row[0] for row in c.fetchall()]

# #     selected_movie = st.selectbox("Select a Movie", movie_titles)
# #     rating = st.slider("Rate this movie (1-5)", 1, 5)

# #     if st.button("Submit and get Recommendations"):
# #         with get_connection() as conn:
# #             c = conn.cursor()
# #             c.execute("INSERT INTO movie_ratings (userid, title, rating) VALUES (?, ?, ?)", 
# #                       (userid, selected_movie, rating))
# #             conn.commit()
# #             temp_df = get_similar_movies(selected_movie, rating)
# #             st.write(temp_df.head())
# #             st.success(f"Your rating for '{selected_movie}' has been submitted.")

# # elif selected_move == "Update Ratings":
# #     st.header("Search Movie:")

# #     with get_connection() as conn:
# #         c = conn.cursor()
# #         c.execute("SELECT DISTINCT title FROM movie_ratings")
# #         movie_titles = [row[0] for row in c.fetchall()]

# #     selected_movie = st.selectbox("Select a Movie", movie_titles)
# #     rating = st.slider("Rate this movie (1-5)", 1, 5)
# #     if st.button("Update Rating"):
# #         with get_connection() as conn:
# #             c = conn.cursor()
# #             c.execute("SELECT * FROM movie_ratings WHERE userid = ? AND title = ?", (userid, selected_movie))
# #             existing_rating = c.fetchone()
# #             if existing_rating:
# #                 # Updating rating
# #                 c.execute("UPDATE movie_ratings SET rating = ? WHERE userid = ? AND title = ?",
# #                           (rating, userid, selected_movie))
# #                 conn.commit()
# #                 st.success(f"Your rating for '{selected_movie}' has been updated.")
# #             else:
# #                 # Inserting the new rating
# #                 c.execute("INSERT INTO movie_ratings (userid, title, rating) VALUES (?, ?, ?)",
# #                           (userid, selected_movie, rating))
# #                 conn.commit()
# #                 st.success(f"Your rating for '{selected_movie}' has been submitted.")

# # elif selected_move == "Delete user":
# #     if st.button("Delete User"):
# #         # Deleting the user from the database
# #         with get_connection() as conn:
# #             c = conn.cursor()
# #             c.execute("DELETE FROM movie_ratings WHERE userid = ?", (userid,))
# #             conn.commit()
# #             st.success(f"User with ID {userid} has been deleted.")

# # elif selected_move == "Add Movie":
# #     st.header("Add Movie:")
# #     with st.form(key='add_movie_form'):
# #         movie_id = st.number_input(label="Enter Movie ID", step=1)
# #         movie_title = st.text_input(label="Enter Movie Title")
# #         submit_button = st.form_submit_button(label='Add Movie')

# #         if submit_button:
# #             # Insert the movie into the database
# #             with get_connection() as conn:
# #                 c = conn.cursor()
# #                 c.execute("INSERT INTO movie_ratings (movieid, title) VALUES (?, ?)",
# #                           (movie_id, movie_title))
# #                 conn.commit()
# #                 st.success(f"Movie with ID {movie_id} has been added to the database.")


# # import streamlit as st
# # import pandas as pd
# # import sqlite3

# # # Function to establish database connection
# # def get_connection():
# #     conn = sqlite3.connect('tutorial.db')
# #     return conn

# # # Function to get similar movies based on scores
# # def get_similar_movies(movie_name, rating):
# #     similar_ratings = corrMatrix[movie_name] * (rating - 2.5)
# #     similar_ratings = similar_ratings.sort_values(ascending=False)
# #     return similar_ratings

# # # Reading all parquet data files
# # # movie_df = pd.read_parquet(path= "movies.parquet", engine='auto')
# # corrMatrix = pd.read_parquet(path="corrmatrix.parquet", engine="auto")
# # merged = pd.read_parquet(path="movie_rating.parquet", engine="auto")

# # # Title of the app
# # st.title("Movie Recommendation System")

# # # Enter user id
# # st.sidebar.header("Enter User ID:")
# # userid = st.sidebar.number_input(label="User ID", step=1)
# # userid = int(userid)

# # # Check if the user ID is present in the movie_ratings table
# # with get_connection() as conn:
# #     c = conn.cursor()
# #     c.execute("SELECT * FROM movie_ratings WHERE userid = ?", (userid,))
# #     existing_user = c.fetchone()
# #     if existing_user:
# #         st.write("Existing user.")
# #     else:
# #         st.write("New user.")

# # # Functions to perform
# # st.sidebar.header("Activities")
# # selected_move = st.sidebar.selectbox("Select a Move", options=[None, "Get Suggestions", "Update Ratings", "Delete user", "Add Movie", "View Ratings"])

# # # get movie suggestions
# # if selected_move == "Get Suggestions":
# #     # Movie rating section
# #     st.header("Rate Movie:")

# #     with get_connection() as conn:
# #         c = conn.cursor()
# #         c.execute("SELECT DISTINCT title FROM movie_ratings")
# #         movie_titles = [row[0] for row in c.fetchall()]

# #     selected_movie = st.selectbox("Select a Movie", movie_titles)
# #     rating = st.slider("Rate this movie (1-5)", 1, 5)

# #     if st.button("Submit and get Recommendations"):
# #         with get_connection() as conn:
# #             c = conn.cursor()
# #             c.execute("INSERT INTO movie_ratings (userid, title, rating) VALUES (?, ?, ?)", 
# #                       (userid, selected_movie, rating))
# #             conn.commit()
# #             temp_df = get_similar_movies(selected_movie, rating)
# #             st.write(temp_df.head())
# #             st.success(f"Your rating for '{selected_movie}' has been submitted.")

# # elif selected_move == "Update Ratings":
# #     st.header("Search Movie:")

# #     with get_connection() as conn:
# #         c = conn.cursor()
# #         c.execute("SELECT DISTINCT title FROM movie_ratings")
# #         movie_titles = [row[0] for row in c.fetchall()]

# #     selected_movie = st.selectbox("Select a Movie", movie_titles)
# #     rating = st.slider("Rate this movie (1-5)", 1, 5)
# #     if st.button("Update Rating"):
# #         with get_connection() as conn:
# #             c = conn.cursor()
# #             c.execute("SELECT * FROM movie_ratings WHERE userid = ? AND title = ?", (userid, selected_movie))
# #             existing_rating = c.fetchone()
# #             if existing_rating:
# #                 # Updating rating
# #                 c.execute("UPDATE movie_ratings SET rating = ? WHERE userid = ? AND title = ?",
# #                           (rating, userid, selected_movie))
# #                 conn.commit()
# #                 st.success(f"Your rating for '{selected_movie}' has been updated.")
# #             else:
# #                 # Inserting the new rating
# #                 c.execute("INSERT INTO movie_ratings (userid, title, rating) VALUES (?, ?, ?)",
# #                           (userid, selected_movie, rating))
# #                 conn.commit()
# #                 st.success(f"Your rating for '{selected_movie}' has been submitted.")

# # elif selected_move == "Delete user":
# #     if st.button("Delete User"):
# #         # Deleting the user from the database
# #         with get_connection() as conn:
# #             c = conn.cursor()
# #             c.execute("DELETE FROM movie_ratings WHERE userid = ?", (userid,))
# #             conn.commit()
# #             st.success(f"User with ID {userid} has been deleted.")

# # elif selected_move == "Add Movie":
# #     st.header("Add Movie:")
# #     with st.form(key='add_movie_form'):
# #         movie_id = st.number_input(label="Enter Movie ID", step=1)
# #         movie_title = st.text_input(label="Enter Movie Title")
# #         submit_button = st.form_submit_button(label='Add Movie')

# #         if submit_button:
# #             # Insert the movie into the database
# #             with get_connection() as conn:
# #                 c = conn.cursor()
# #                 c.execute("INSERT INTO movie_ratings (movieid, title) VALUES (?, ?)",
# #                           (movie_id, movie_title))
# #                 conn.commit()
# #                 st.success(f"Movie with ID {movie_id} has been added to the database.")

# # elif selected_move == "View Ratings":
# #     st.header("View Your Ratings:")
# #     with get_connection() as conn:
# #         c = conn.cursor()
# #         c.execute("SELECT title, rating FROM movie_ratings WHERE userid = ?", (userid,))
# #         user_ratings = c.fetchall()
# #         if user_ratings:
# #             st.write("Your Ratings:")
# #             for movie, rating in user_ratings:
# #                 st.write(f"- {movie}: {rating}")
# #         else:
# #             st.write("You haven't rated any movies yet.")

# # c.close()


# import streamlit as st
# import pandas as pd
# import sqlite3

# # Function to establish database connection
# def get_connection():
#     conn = sqlite3.connect('tutorial.db')
#     return conn

# # Function to get similar movies based on scores
# def get_similar_movies(movie_name, rating):
#     similar_ratings = corrMatrix[movie_name] * (rating - 2.5)
#     similar_ratings = similar_ratings.sort_values(ascending=False)
#     return similar_ratings

# # Reading all parquet data files
# # movie_df = pd.read_parquet(path= "movies.parquet", engine='auto')
# corrMatrix = pd.read_parquet(path="corrmatrix.parquet", engine="auto")
# merged = pd.read_parquet(path="movie_rating.parquet", engine="auto")

# # Title of the app
# st.title("Movie Recommendation System")

# # Enter user id
# st.sidebar.header("Enter User ID:")
# userid = st.sidebar.number_input(label="User ID", step=1)
# userid = int(userid)

# # Check if the user ID is present in the movie_ratings table
# with get_connection() as conn:
#     c = conn.cursor()
#     c.execute("SELECT * FROM movie_ratings WHERE userid = ?", (userid,))
#     existing_user = c.fetchone()
#     if existing_user:
#         st.write("Existing user.")
#     else:
#         st.write("New user.")

# # Functions to perform
# st.sidebar.header("Function to perform")
# selected_move = st.sidebar.selectbox("Select a Move", options=[None, "Get Suggestions", "Update Ratings", "Delete user", "Add Movie", "View Ratings", "Top Rated Movies", "Most Popular Movies"])

# # get movie suggestions
# if selected_move == "Get Suggestions":
#     # Movie rating section
#     st.header("Rate Movie:")

#     with get_connection() as conn:
#         c = conn.cursor()
#         c.execute("SELECT DISTINCT title FROM movie_ratings")
#         movie_titles = [row[0] for row in c.fetchall()]

#     selected_movie = st.selectbox("Select a Movie", movie_titles)
#     rating = st.slider("Rate this movie (1-5)", 1, 5)

#     if st.button("Submit and get Recommendations"):
#         with get_connection() as conn:
#             c = conn.cursor()
#             c.execute("INSERT INTO movie_ratings (userid, title, rating) VALUES (?, ?, ?)", 
#                       (userid, selected_movie, rating))
#             conn.commit()
#             temp_df = get_similar_movies(selected_movie, rating)
#             st.write(temp_df.head())
#             st.success(f"Your rating for '{selected_movie}' has been submitted.")

# elif selected_move == "Update Ratings":
#     st.header("Search Movie:")

#     with get_connection() as conn:
#         c = conn.cursor()
#         c.execute("SELECT DISTINCT title FROM movie_ratings")
#         movie_titles = [row[0] for row in c.fetchall()]

#     selected_movie = st.selectbox("Select a Movie", movie_titles)
#     rating = st.slider("Rate this movie (1-5)", 1, 5)
#     if st.button("Update Rating"):
#         with get_connection() as conn:
#             c = conn.cursor()
#             c.execute("SELECT * FROM movie_ratings WHERE userid = ? AND title = ?", (userid, selected_movie))
#             existing_rating = c.fetchone()
#             if existing_rating:
#                 # Updating rating
#                 c.execute("UPDATE movie_ratings SET rating = ? WHERE userid = ? AND title = ?",
#                           (rating, userid, selected_movie))
#                 conn.commit()
#                 st.success(f"Your rating for '{selected_movie}' has been updated.")
#             else:
#                 # Inserting the new rating
#                 c.execute("INSERT INTO movie_ratings (userid, title, rating) VALUES (?, ?, ?)",
#                           (userid, selected_movie, rating))
#                 conn.commit()
#                 st.success(f"Your rating for '{selected_movie}' has been submitted.")

# elif selected_move == "Delete user":
#     if st.button("Delete User"):
#         # Deleting the user from the database
#         with get_connection() as conn:
#             c = conn.cursor()
#             c.execute("DELETE FROM movie_ratings WHERE userid = ?", (userid,))
#             conn.commit()
#             st.success(f"User with ID {userid} has been deleted.")

# elif selected_move == "Add Movie":
#     st.header("Add Movie:")
#     with st.form(key='add_movie_form'):
#         movie_id = st.number_input(label="Enter Movie ID", step=1)
#         movie_title = st.text_input(label="Enter Movie Title")
#         submit_button = st.form_submit_button(label='Add Movie')

#         if submit_button:
#             # Insert the movie into the database
#             with get_connection() as conn:
#                 c = conn.cursor()
#                 c.execute("INSERT INTO movie_ratings (movieid, title) VALUES (?, ?)",
#                           (movie_id, movie_title))
#                 conn.commit()
#                 st.success(f"Movie with ID {movie_id} has been added to the database.")

# elif selected_move == "View Ratings":
#     st.header("View Your Ratings:")
#     with get_connection() as conn:
#         c = conn.cursor()
#         c.execute("SELECT title, rating FROM movie_ratings WHERE userid = ?", (userid,))
#         user_ratings = c.fetchall()
#         if user_ratings:
#             st.write("Your Ratings:")
#             for movie, rating in user_ratings:
#                 st.write(f"- {movie}: {rating}")
#         else:
#             st.write("You haven't rated any movies yet.")

# elif selected_move == "Top Rated Movies":
#     st.header("Top Rated Movies:")
#     with get_connection() as conn:
#         c = conn.cursor()
#         c.execute("SELECT title, AVG(rating) AS avg_rating FROM movie_ratings GROUP BY title ORDER BY avg_rating DESC LIMIT 10")
#         top_rated_movies = c.fetchall()
#     if top_rated_movies:
#         st.write("Top Rated Movies:")
#         for movie, avg_rating in top_rated_movies:
#             st.write(f"- {movie}: Average Rating - {avg_rating:.2f}")
#     else:
#         st.write("No ratings available yet.")

# elif selected_move == "Most Popular Movies":
#     st.header("Most Popular Movies:")
#     with get_connection() as conn:
#         c = conn.cursor()
#         c.execute("SELECT title, COUNT(*) AS rating_count FROM movie_ratings GROUP BY title ORDER BY rating_count DESC LIMIT 10")
#         popular_movies = c.fetchall()
#     if popular_movies:
#         st.write("Most Popular Movies:")
#         for movie, rating_count in popular_movies:
#             st.write(f"- {movie}: Ratings Count - {rating_count}")
#     else:
#         st.write("No ratings available yet.")

# c.close()


import streamlit as st
import pandas as pd
import sqlite3

# Function to establish database connection
def get_connection():
    conn = sqlite3.connect('tutorial.db')
    return conn

# Function to get similar movies based on scores
def get_similar_movies(movie_name, rating):
    similar_ratings = corrMatrix[movie_name] * (rating - 2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    return similar_ratings

# Reading all parquet data files
# movie_df = pd.read_parquet(path= "movies.parquet", engine='auto')
corrMatrix = pd.read_parquet(path="corrmatrix.parquet", engine="auto")
merged = pd.read_parquet(path="movie_rating.parquet", engine="auto")

# Title of the app
st.title("Movie Recommendation System")

# Enter user id
st.sidebar.header("Enter User ID:")
userid = st.sidebar.number_input(label="User ID", step=1)
userid = int(userid)

# Check if the user ID is present in the movie_ratings table
with get_connection() as conn:
    c = conn.cursor()
    c.execute("SELECT * FROM movie_ratings WHERE userid = ?", (userid,))
    existing_user = c.fetchone()
    if existing_user:
        st.write("Existing user.")
    else:
        st.write("New user.")

# Genre selection
st.sidebar.header("Genre Selection")
genres = st.sidebar.radio("Select Genre", ("Action", "Adventure", "Comedy", "Drama", "Horror", "Sci-Fi", "Thriller", "Romance", "Animation", "Documentary"))

# get movie suggestions

# Functions to perform
st.sidebar.header("User options")
get_suggestions = st.sidebar.checkbox("Get Suggestions")
update_ratings = st.sidebar.checkbox("Update Ratings")
delete_user = st.sidebar.checkbox("Delete User")
add_movie = st.sidebar.checkbox("Add Movie")
view_ratings = st.sidebar.checkbox("View Ratings")
top_rated_movies = st.sidebar.checkbox("Top Rated Movies")
most_popular_movies = st.sidebar.checkbox("Most Popular Movies")

# get movie suggestions
if get_suggestions:
    # Movie rating section
    st.header("Rate Movie:")

    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT DISTINCT title FROM movie_ratings")
        movie_titles = [row[0] for row in c.fetchall()]

    selected_movie = st.selectbox("Select a Movie", movie_titles)
    rating = st.slider("Rate this movie (1-5)", 1, 5)

    if st.button("Submit and get Recommendations"):
        with get_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO movie_ratings (userid, title, rating) VALUES (?, ?, ?)", 
                      (userid, selected_movie, rating))
            conn.commit()
            temp_df = get_similar_movies(selected_movie, rating)
            st.write(temp_df.head())
            st.success(f"Your rating for '{selected_movie}' has been submitted.")

if update_ratings:
    st.header("Search Movie:")

    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT DISTINCT title FROM movie_ratings")
        movie_titles = [row[0] for row in c.fetchall()]

    selected_movie = st.selectbox("Select a Movie", movie_titles)
    rating = st.slider("Rate this movie (1-5)", 1, 5)
    if st.button("Update Rating"):
        with get_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM movie_ratings WHERE userid = ? AND title = ?", (userid, selected_movie))
            existing_rating = c.fetchone()
            if existing_rating:
                # Updating rating
                c.execute("UPDATE movie_ratings SET rating = ? WHERE userid = ? AND title = ?",
                          (rating, userid, selected_movie))
                conn.commit()
                st.success(f"Your rating for '{selected_movie}' has been updated.")
            else:
                # Inserting the new rating
                c.execute("INSERT INTO movie_ratings (userid, title, rating) VALUES (?, ?, ?)",
                          (userid, selected_movie, rating))
                conn.commit()
                st.success(f"Your rating for '{selected_movie}' has been submitted.")

if delete_user:
    if st.button("Delete User"):
        # Deleting the user from the database
        with get_connection() as conn:
            c = conn.cursor()
            c.execute("DELETE FROM movie_ratings WHERE userid = ?", (userid,))
            conn.commit()
            st.success(f"User with ID {userid} has been deleted.")

if add_movie:
    st.header("Add Movie:")
    with st.form(key='add_movie_form'):
        movie_id = st.number_input(label="Enter Movie ID", step=1)
        movie_title = st.text_input(label="Enter Movie Title")
        submit_button = st.form_submit_button(label='Add Movie')

        if submit_button:
            # Insert the movie into the database
            with get_connection() as conn:
                c = conn.cursor()
                c.execute("INSERT INTO movie_ratings (movieid, title) VALUES (?, ?)",
                          (movie_id, movie_title))
                conn.commit()
                st.success(f"Movie with ID {movie_id} has been added to the database.")

if view_ratings:
    st.header("View Your Ratings:")
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT title, rating FROM movie_ratings WHERE userid = ?", (userid,))
        user_ratings = c.fetchall()
        if user_ratings:
            st.write("Your Ratings:")
            for movie, rating in user_ratings:
                st.write(f"- {movie}: {rating}")
        else:
            st.write("You haven't rated any movies yet.")

if top_rated_movies:
    st.header("Top Rated Movies:")
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT title, AVG(rating) AS avg_rating FROM movie_ratings GROUP BY title ORDER BY avg_rating DESC LIMIT 10")
        top_rated_movies = c.fetchall()
    if top_rated_movies:
        st.write("Top Rated Movies:")
        for movie, avg_rating in top_rated_movies:
            st.write(f"- {movie}: Average Rating - {avg_rating:.2f}")
    else:
        st.write("No ratings available yet.")

if most_popular_movies:
    st.header("Most Popular Movies:")
    # Write code to display most popular movies

c.close()
