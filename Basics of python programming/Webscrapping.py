# import requests

# from bs4 import BeautifulSoup

# url ="http://quotes.toscrape.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find all quotes blocks
# quotes = soup.find_all('div', class_='quote')

# '''
# span: targeting specific pieces of content with  css or JavaScript
# class_:targeting elements with a specific class name

# '''

# for quote in quotes:
#     text = quote.find('span', class_='text').text()
#     author = quote.find('small', class_='author').text()
#     print(f'Quote: {text}\nAuthor: {author}\n')
    

