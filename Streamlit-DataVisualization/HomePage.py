import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)


st.title("Welcome to SICKATHON Example App")
st.write("Welcome, SICKATHON participants! This app is made to help you and provide you some overview about what app you're going to make.")


st.header("App Purpose")
st.write("The app will show you about:")
st.write("- Connecting to a database.")
st.write("- Fetch and explore data with ease.")
st.write("- Visualize data using various chart types.")


st.header("Getting Started")
st.write("To get started, you need to follow these steps:")
st.write("1. Create a Python virtual environment using the venv module.")
st.code("""
    python -m venv venv
""", language="shell")
st.write("2. Activate the Virtual Environment.")
st.code("""
    source venv/bin/activate
""", language="shell")
st.write("3. Make sure to install the Streamlit package.")
st.code("""
    pip install streamlit
""", language="shell")
st.write("You might also need")
st.code("""
    pip install SQLAlchemy mysqlclient
""", language="shell")

st.write("Now, you're ready to develop your streamlit app!")

st.header("Contact Us")
st.write("If you have any questions or need assistance during the hackathon, please feel free to contact us mentors.")

# You can add more sections or customize the text as needed for your SICKATHON-specific introduction.
