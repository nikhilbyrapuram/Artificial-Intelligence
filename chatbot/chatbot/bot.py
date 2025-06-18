import re
import nltk
from nltk.corpus import wordnet

# Download required NLTK datasets
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')

# Define the keywords for each intent
list_words = ['hello', 'admission', 'courses', 'timings', 'events']
list_syn = {}

# Use WordNet to get synonyms for each keyword
for word in list_words:
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            lem_name = lem.name().replace('_', ' ')
            synonyms.add(lem_name.lower())
    list_syn[word] = synonyms

# Create dictionary for intents and corresponding regex patterns
keywords = {}
keywords_dict = {}

for word in list_words:
    intent_name = word
    keywords[intent_name] = []
    for synonym in list_syn[word]:
        keywords[intent_name].append(r'\b' + re.escape(synonym) + r'\b')

# Compile regex
for intent, keys in keywords.items():
    keywords_dict[intent] = re.compile('|'.join(keys), re.IGNORECASE)

# Responses
responses = {
    'hello': 'Hello! How can I assist you today?',
    'admission': 'To apply for admission, please visit our admissions page on the website. The application deadline is June 30th.',
    'courses': 'We offer various undergraduate and postgraduate programs. You can find detailed course information on our website.',
    'timings': 'Our office hours are from 9 AM to 5 PM, Monday to Friday. The college campus is open from 8 AM to 8 PM.',
    'events': 'Upcoming events include the Annual Tech Conference on April 10th and a Workshop on Machine Learning on April 15th.',
    'fallback': 'I am not sure about that. Could you please ask something else or be more specific?'
}

# Function to get response
def get_response(user_input):
    matched_intent = None
    for intent, pattern in keywords_dict.items():
        if re.search(pattern, user_input.lower()):
            matched_intent = intent
            break
    return responses[matched_intent] if matched_intent else responses['fallback']
