import streamlit as st

st.title("Prepare the database")
st.write("""Before trying to connect to the database, we should prepare the database first.
         In this page i will show you how to host your database with [FreeMySQLHosting](https://www.freemysqlhosting.net/).
         It is free a database hosting service, but it has a limit of 5mb for free user""")


st.title("Prepare the data")
st.write("""It will be better if you already have the data to put in the Database,
            if you are going to host the database at the same service like. Make sure the data isn't more than 5mb.
         """)
st.markdown("There are a lot of websites that provides a lot of datasets, such as :")
st.write("1. [Kaggle](https://www.kaggle.com/datasets)")
st.write("2. [Socrata](https://opendata.socrata.com/)")
st.write("3. [Google Public Dataset](https://cloud.google.com/bigquery/public-data/)")
st.write("and a lot more...")
st.write("When you found the data you needed, the next step is to make the database online and upload your dataset. In this case, i will show you how to do it with FreeMySQLHosting")

st.title("Database Online!")
st.write("Here are step by step to do it:")
st.write("1. Visit this page [FreeMySQLHosting](https://www.freemysqlhosting.net/).")
st.write("2. Make a free account by clicking the 'Start my free Account' button.")
st.image('resources/images/Register.png')
st.write("3. Fill the form and follow the instruction to confirm your email")
st.write("4. Once your account created, go to MySQL Hosting on the navbar. Here you can create your database, once it created, the credential of your database will be sent to your email")
st.image('resources/images/Myaccount.png')
st.write("5. After you recieved the database credential, click on the 'Follow this link to phpMyadmin'")
st.write("6. The link will redirect you to phpMyAdmin login page, login with the credential that you received recently")
st.write("7. If your login succeeded, you will be shown the phpMyAdmin database management interface. Click on your database, and click import at the navbar")
st.write("8. Upload your dataset and make sure to chose the file format according to the dataset you downloaded before")
st.image('resources/images/import.png')

st.write("Once it's succesfuly imported, your database is ready to use!. You can access it with the credential at your email")