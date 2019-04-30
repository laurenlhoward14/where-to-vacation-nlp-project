import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from unicodedata import normalize, category
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer

def clean_article(article):

    # Find all proper nouns and names in article - keep to one side
    nouns_list = []
    for tup in pos_tag(word_tokenize(article)):
        if 'NNP' in tup:
            nouns_list.append(tup[0].lower())

    # Remove accents (keep as just letters)
    article = ''.join([c for c in normalize('NFD',article.lower()) if category(c) != 'Mn'])
    article = re.sub(r'[-|—|’|“|”|£]', ' ', article)
    article = re.sub('\(.*?\)', '', article)

    # Tokenize article in words
    tokens = nltk.word_tokenize(article)

    # Remove all punctuation & numbers
    for idx, word in enumerate(tokens):
        tokens[idx] = "".join(l for l in word if l not in string.punctuation)

    for idx, word in enumerate(tokens):
        if re.compile('\w*\d\w*').match(word):
            tokens[idx] = ''

    # Remove stopwords
    stops = list(stopwords.words('english'))

    for idx, word in enumerate(tokens):
        if word in stops:
            tokens[idx] = ''

    # Remove 'credit' from words
    for idx, word in enumerate(tokens):
        if "credit" in word:
            tokens[idx] = ''
        if "euro" in word:
            tokens[idx] = ''
        if "city" in word:
            tokens[idx] = ''

    # Remove spaces and 2 letter words and words over 15 letters
    final_list = []
    for word in tokens:
        if 2<len(word)<15:
            final_list.append(word)

    # Remove nouns and names
    total_list = []
    for word in final_list:
        if word not in nouns_list:
            total_list.append(word)

    # Lemmatize words & stem
    for idx, word in enumerate(total_list):
        new_word = WordNetLemmatizer().lemmatize(word, pos='v')
        new_word = LancasterStemmer().stem(new_word)
        total_list[idx] = new_word


    return ' '.join(total_list)
