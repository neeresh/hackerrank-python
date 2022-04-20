def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words): # ['programming', 'is', 'awesome']  
    score = 0
    for word in words: # programming
        num_vowels = 0
        for letter in word: # p, r, o, g, r, a, m, m, i, n, g.
            if is_vowel(letter):
                num_vowels += 1 # o -> 1, i-> 1+1 = 2
        if num_vowels % 2 == 0:
            score += 2 # 0 + 2 = 2, 
        else:
            score = score + 1
    return score

