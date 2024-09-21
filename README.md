**Quote Scraper

Overview
The Quote Scraper is a Streamlit-based web application that allows users to scrape motivational and success quotes from the QuoteFancy website based on a given topic or keyword. This tool helps gather quotes along with their associated categories and provides an option to download the results as a CSV file.

#Features
Dynamic Keyword Input: Users can input any topic or keyword, and the app will convert it into a format suitable for the QuoteFancy URL.
Automated Scraping: The scraper navigates through multiple pages (up to 10) to extract quotes and their respective categories.
Data Visualization: Displays the scraped quotes and categories directly in the Streamlit app interface.
CSV Download: Users can download the scraped quotes and categories as a CSV file with categories split into separate columns for easy analysis.

#How It Works
User Input: The user enters a keyword related to the type of quotes they want to scrape (e.g., "Success Quotes", "Motivational Wallpapers").

URL Formatting: The input keyword is converted into a URL-friendly format by replacing spaces with dashes. For example, "Success Quotes" becomes "Success-Quotes".

Web Scraping: The app sends requests to the QuoteFancy website for up to 10 pages. It extracts the quote text and categories associated with each quote using BeautifulSoup.

Data Display and Download: The scraped quotes and categories are displayed on the web interface. Users can download the data as a CSV file where each quote is followed by its categories in adjacent columns.

#Usage Instructions
Enter the desired keyword or topic in the text input box and click "Scrape Quotes".
The app will fetch quotes and their categories from QuoteFancy based on the provided keyword.
View the scraped quotes and categories directly on the page.
Click the "Download CSV" button to download the results. The CSV file will have separate columns for the quote text and categories.

#Technologies Used
Streamlit: For building the interactive web application.
Requests: For making HTTP requests to the QuoteFancy website.
BeautifulSoup: For parsing and extracting data from the HTML content.
Pandas: For handling and structuring data before converting it to CSV.

#Prerequisites
To run this application locally, you need to have Python installed along with the following packages:

Streamlit
Requests
BeautifulSoup4
Pandas

You can install all dependencies by running:


pip install -r requirements.txt

Clone the repository:

git clone https://github.com/Iamkrmayank/Suvichaar_Quotes_Scraper.git

Navigate to the project directory:

cd Suvichaar_Quotes_Scraper

Run the Streamlit app:

streamlit run app.py

Open your browser and go to http://localhost:8501 to access the app.

#Deployment
The application can be easily deployed on Streamlit Cloud by connecting your GitHub repository and specifying the app.py file as the entry point.

Example Use Case
If you want to scrape quotes related to "Perseverance", you would enter "Perseverance Quotes" in the text box. The scraper will then extract quotes from the first 10 pages of the corresponding section on QuoteFancy and display them in the app, along with categories like "Hard Work", "Motivational Wallpapers", etc. You can then download these quotes and categories in a CSV format for further use.

Contribution
Feel free to fork this repository and make contributions. Pull requests are welcome for any improvements or feature additions.
