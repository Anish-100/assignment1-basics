from pre_tokenizer import pre_tokenize
from collections import Counter

lines = '''\
low low low low low
lower lower widest widest widest
newest newest newest newest newest newest\
'''

words = Counter( [x.groups() for x in pre_tokenize(lines)])


def replace_words_with_greatest_token(new_pairs:dict):
    ''' max is a tuple of token and frequency'''
    max_word_tup = get_max_token(new_pairs)
    max_word_str = ''.join(max_word_tup)
    word_len = len(max_word_tup)
    new_words = {}

    for word_list in words:
        new_word_list = []
        word_list_len = len(word_list)
        i = 0
        # Obtain the new tokenized form of the new words
        while i < word_list_len:
            found = False
            for j in range(word_len+1):
                if word_list[i:i+j]== max_word_tup:
                    new_word_list.append(max_word_str) # We add the string form of max_word to the new list
                    i+=j
                    found = True
                    break
            if found:
                continue
            new_word_list.append(word_list[i])
            i+=1
        new_word_tup = tuple(new_word_list)
        # assign it to the same frequency. 
        new_words[new_word_tup] = words[word_list]

    print(f'replace words with tokens result {max_word_tup}')
    print(new_words)
    return new_words

            


def get_max_token(new_pairs):
    max = None
    for token, freq in new_pairs.items():
        if max is None or freq > max[1]:
            max = (token,freq)
        elif freq == max[1]:
            if token > max[0]:
                max = (token,freq)
    return (max[0])
    

def tokenizer():
    ''' A naive tokenizer'''
    new_pairs = {}
    for word, freq in words.items():
        for i in range(1,len(word)):
            token =word[i-1:i+1]
            new_pairs[token]= freq + new_pairs.get(token,0)
    return new_pairs
    

if __name__ == '__main__':
    for i in range(6):
        print('words before tokenizer',words)
        # new_pairs = tokenizer()
        # print('words after tokenizer',new_pairs)
        # words = replace_words_with_greatest_token(new_pairs)
        # print(f'{i}th round results')
        # print(words)