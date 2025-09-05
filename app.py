import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.title("Hello World! this is my Python in a browser!!")
st.write("This is runing live on a port!")


#GETTING THE HTML

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


# EXTRACT DATA

quotes_data = []
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

for quote, author in zip(quotes, authors):
    quotes_data.append({
        "quote": quote.get_text(),
        "author": author.get_text()
    })



# SAVE TO CSV

df = pd.DataFrame(quotes_data)
df.to_csv("quotes.csv", index=False)


print("Scraping complete! Saved to quotes.csv")


# LOAD DATA TO BROWSER

df = pd.read_csv("quotes.csv")

st.title("Quotes & Their Authors")
st.write("Here are some quotes I scraped from the web:")

# Show table
st.dataframe(df)

# Add a filter for authors
authors = df['author'].unique()
selected_author = st.selectbox("Filter by author:", ["All"] + list(authors))

if selected_author != "All":
    filtered_df = df[df['author'] == selected_author]
else:
    filtered_df = df

st.dataframe(filtered_df)