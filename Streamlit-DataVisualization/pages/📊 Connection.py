import streamlit as st

st.title("Most Streamed Spotify Songs 2023 Dataset")
st.write("""This dataset contains a comprehensive list of the most famous songs of 2023 as listed on Spotify. 
         The dataset offers a wealth of features beyond what is typically available in similar datasets. It provides 
         insights into each song's attributes, popularity, and presence on various music platforms. The dataset includes 
         information such as track name, artist(s) name, release date, Spotify playlists and charts, streaming statistics,
          Apple Music presence, Deezer presence, Shazam charts, and various audio features.""")
st.write("The data was obtained from [Kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023).")
st.image('resources/images/Kaggle.png')



st.title("Fetching the data from database")
st.write("If the database has been set, we're ready to fetch the data. But, first we have to establish a connection to the database :")
st.code("""
        import streamlit as st
        conn = st.experimental_connection('songs_db',type="sql")
        """)

st.write("""Before using those line of code, you should configure your database credential first, Create a file :red[secrets.toml] .
         The content of the file should look like this :""")
st.code("""[connections.songs_db]
type = "mysql"
dialect = "mysql"
host = "[database_server]"
port = 3306
database = "[database_name]"
username = "[database_username]"
password = "[database_password]"
        """)

st.write("When the connection established, you can query the data and show it with :red[dataframe]")
st.code("""
        query = "SELECT * FROM songs"
        data = conn.query(query)
        st.dataframe(data, hide_index=True)
        """)

st.write("The query result :")
conn = st.experimental_connection('songs_db',type="sql")

query = "SELECT * FROM songs"
data = conn.query(query)
st.dataframe(data, hide_index=True)

st.title("Data Visualization ")
st.write("""
        Visualization helps you understand your data better. It allows you to explore patterns, 
         trends, and relationships within the data that may not be immediately apparent in raw numbers or tables.
""")

st.write("Let's try to find top 10 streams of these songs")
st.code("""
    query = \"""
        SELECT
            `track_name`,
            `artist(s)_name`,
            `streams`
        FROM
            `songs`
        ORDER BY
            `streams` DESC
        LIMIT 10;
        \"""
    data = conn.query(query)
    st.dataframe(data)
""")

query = """
SELECT
    `track_name`,
    `artist(s)_name`,
    `streams`
FROM
    `songs`
ORDER BY
    `streams` DESC
LIMIT 10;
"""
data = conn.query(query)
st.write("Here are the results")
st.dataframe(data)
st.write("From the chart above, we can see that the most streamed song is :red[Anti Hero by Taylor Swift] with a total stream of almost 1 billion")

st.write("Next, let's try to find the the release year for the top 200 most streamed songs")
st.code("""
query= \"""
        SELECT
            `released_year`,
            COUNT(*) AS `song_count`
        FROM
            (
                SELECT
                    `track_name`,
                    `artist(s)_name`,
                    `streams`,
                    `released_year`
                FROM
                    `songs`
                ORDER BY
                    `streams` DESC
                LIMIT 200
            ) AS `top_200_songs`
        GROUP BY
            `released_year`
        ORDER BY
            `song_count` DESC;
\"""
data = conn.query(query)
""")

query= """
        SELECT
            `released_year`,
            COUNT(*) AS `song_count`
        FROM
            (
                SELECT
                    `track_name`,
                    `artist(s)_name`,
                    `streams`,
                    `released_year`
                FROM
                    `songs`
                ORDER BY
                    `streams` DESC
                LIMIT 200
            ) AS `top_200_songs`
        GROUP BY
            `released_year`
        ORDER BY
            `song_count` DESC;
"""
data = conn.query(query)
st.write("And then, let's show the query result into a bar chart as below:")
st.bar_chart(data, x='released_year', y=['song_count'])
st.write("The chart above, shows that most of these songs released on :red[2022]")



st.write("""Those are, just a simple example of the app. 
         This app use a simple database and visualization, you can use even more complex database and visualization if you wish
         """)