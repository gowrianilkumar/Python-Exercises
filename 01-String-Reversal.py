def reverse_word(sentence):
    words = sentence.split()
    reversed_words = ' '.join(word[::-1] for word in words)
    return reversed_words


sentence = "Python is Awesome"
result = reverse_word(sentence)
print(result)  
