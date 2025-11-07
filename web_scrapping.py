import requests
from bs4 import BeautifulSoup

# NEW URL: A site designed specifically for web scraping practice
url = 'http://quotes.toscrape.com/'

# Define a standard User-Agent (we'll keep this just in case)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # 1. Fetch the content from the URL
    response = requests.get(url, headers=headers)
    response.raise_for_status() 

    # 2. Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    print("--- Successfully Scraped Quotes from To Scrape ---")
    
    # 3. Find and extract the quotes and authors
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    
    # 4. Print the extracted data
    for i in range(min(5, len(quotes))): # Print the first 5 quotes
        quote = quotes[i].text.strip()
        author = authors[i].text.strip()
        print(f"\nQuote {i+1}: \"{quote}\"")
        print(f"Author: {author}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")
