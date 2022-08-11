import spacy
import requests
from bs4 import BeautifulSoup
from collections import Counter

nlp = spacy.load("en_core_web_sm")
response = requests.get("http://lite.cnn.com/en")
soup = BeautifulSoup(response.text, "html.parser")

# https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
[s.extract() for s in soup(['style', 'script', '[document]', 'head','title'])]
text = soup.getText()
doc = nlp(text)

names = []
for ent in doc.ents:
    if ent.label_ == "PERSON":
        names.append(ent.lemma_)

print("These people are in the headlines today")
print(Counter(names).most_common(20))
