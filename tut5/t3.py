# Use the following command to save the english-words.txt into Google Server
# !curl https://jiangkan.pythonanywhere.com/static/english-words.txt -o english-words.txt
# Use the following code to create the English word list
with open('english-words.txt', 'r') as file:
  english_words = file.read().split('\n')

def breaker_word(word, i, dictionary):
  if i == len(word):
    return None

  w1, w2 = word[:i], word[i:]
  if w1 in dictionary and w2 in dictionary:
    return (w1, w2)
  return breaker_word(word, i+1, dictionary)