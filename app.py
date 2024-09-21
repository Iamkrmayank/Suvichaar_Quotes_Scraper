import streamlit as st
import requests
from bs4 import BeautifulSoup
import csv
from io import StringIO
import pandas as pd

st.title("Quote Scraper")

user_input = st.text_input("Enter a string:")

if st.button("Scrape Quotes"):
    if user_input:
        dashed_string = "-".join(user_input.split())
        quotes = []

        for i in range(1, 11):
            url = f"https://quotefancy.com/{dashed_string}/page/{i}"
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                quote_containers = soup.find_all('div', class_='q-wrapper')

                for container in quote_containers:
                    quote_link = container.find('a', class_='quote-a')
                    quote_text = quote_link.text if quote_link else 'No quote found'

                    author_paragraphs = container.find_all('p', class_='author-p')
                    categories = []
                    for author_paragraph in author_paragraphs:
                        category_elements = author_paragraph.find_all('a')
                        for category in category_elements:
                            categories.append(category.text)

                    quotes.append([quote_text] + categories)

        st.write("Quotes and Categories:")
        for quote_row in quotes:
            st.write(f"- **Quote:** {quote_row[0]}")
            st.write(f"  **Categories:** {', '.join(quote_row[1:])}")

        max_categories = max(len(quote_row) - 1 for quote_row in quotes)
        headers = ["Quote"] + [f"Category {i+1}" for i in range(max_categories)]
        df = pd.DataFrame(quotes, columns=headers)

        csv_data = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name= f"quotes_with_{user_input}.csv",
            mime="text/csv",
        )
    else:
        st.warning("Please enter a string to scrape quotes.")
