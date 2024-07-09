def reverse_each_word(sentence):
    def reverse_word_preserving_case(word):
        reversed_word = ''.join(reversed(word))
        result = ''.join(
            reversed_word[i].upper() if word[i].isupper() else reversed_word[i].lower()
            for i in range(len(word))
        )
        return result

    words = sentence.split()
    reversed_words_with_case = ' '.join(reverse_word_preserving_case(word) for word in words)
    return reversed_words_with_case


sentence = "Python is Awesome"
result = reverse_each_word(sentence)
print(result)  
