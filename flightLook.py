import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://www.google.com/travel/explore?tfs=CBwQAxoaagwIAhIIL20vMDJqM3cSCjIwMjEtMDItMjcaGhIKMjAyMS0wMy0wM3IMCAISCC9tLzAyajN3cAGCAQsI____________AUABSAGYAQGyAQIYAQ&tfu=GgA&hl=en-US&gl=US'

page = requests.get(url)

# Store the contents of the website under doc
soup = BeautifulSoup(page.content, 'html.parser')

pprint(soup.select("body"))
