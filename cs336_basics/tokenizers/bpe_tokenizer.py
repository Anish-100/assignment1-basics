from pre_tokenizer import pre_tokenize
from collections import Counter

lines = '''\
low low low low low
lower lower widest widest widest
newest newest newest newest newest newest\
'''


initial_words = Counter([str.encode(x) for x in lines.split()])
initial_words[str.encode('|<endoftext>|')] = 1


def replace_most_common_byte(most_common_byte_pair, words:dict[bytes]):
    ''' Replaces the most common pair with a new byte_pair '''
    new_byte_words = {}
    most_common_byte_text = b''.join(most_common_byte_pair)
    for tup_byte_word in words:
        new_byte_list = []
        len_n = len(tup_byte_word)
        i = 0
        while i < len_n:
            # special case if final character is not part of most_common_byte_pair
            print(tup_byte_word[i:i+2],most_common_byte_pair)
            if tup_byte_word[i:i+2] == most_common_byte_pair and i != len_n-1 :
                new_byte_list.append(most_common_byte_text)
                i+=2
            else:
                new_byte_list.append(tup_byte_word[i])
                i+=1
        new_tup_byte_word = tuple(new_byte_list)
        new_byte_words[new_tup_byte_word] =  words[tup_byte_word] + new_byte_words.get(new_tup_byte_word,0)
    
    return new_byte_words


def get_byte_pair_map(bytes_map):
    ''' Converts a tuple of bytes into a tuple of byte-pairs'''
    byte_pair_map = {}
    for byte_word in bytes_map.keys():
        freq = bytes_map[byte_word]
        for i in range(len(byte_word)):
            if byte_word[i:i+1] == str.encode('|<endoftext>|'):
                continue
            elif i != len(byte_word)-1:
                byte_pair = byte_word[i:i+2]
                byte_pair_map[byte_pair] = freq + byte_pair_map.get(byte_pair,0)
    return byte_pair_map



def convert_to_tuple_of_bytes(words):
    ''' Gets an inital map of bytes objects and makes them into tuples of bytes.'''
    freq_map = {}
    for byte_word in words:
        byte_list = []
        byte_freq = words[byte_word]
        if byte_word == str.encode('|<endoftext>|'):
            continue
        for i in range(len(byte_word)):
            byte = byte_word[i:i+1]
            byte_list.append(byte)
        tup_byte_list = tuple(byte_list)
        freq_map[tup_byte_list] = byte_freq+ freq_map.get(tup_byte_list,0)

    return freq_map

def take_most_freq_byte(byte_pair_map):
    ''' Finds the most common byte-pair and removes it from the dictionary'''
    max_val = None
    max_key = None
    for key,val in byte_pair_map.items():
        if max_val is None or val > max_val:
            max_key = key
            max_val = val
        elif max_val == val:
            if key > max_key:
                max_key = key
    return max_key

if __name__ == '__main__':
    word_bytes_map = convert_to_tuple_of_bytes(initial_words)
    for i in range(6):
        byte_pair_map  = get_byte_pair_map(word_bytes_map)
        #print(byte_pair_map)
        most_common_pair = take_most_freq_byte(byte_pair_map)
        #print(most_common_pair)
        word_bytes_map = replace_most_common_byte(most_common_pair,word_bytes_map)
        print(word_bytes_map)

