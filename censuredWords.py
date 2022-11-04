import requests
from bs4 import BeautifulSoup

class censuredWords:
    def __init__(self):
        page = requests.get("http://www.bannedwordlist.com/lists/swearWords.txt")
        soup = BeautifulSoup(page.content, 'html.parser')

        self.censuredWords = soup.get_text().splitlines()

    def deleteWords(self, phrase):
        # Delete all the censured words from the phrase
        for word in self.censuredWords:
            phrase = phrase.replace(word, "")

        return phrase
