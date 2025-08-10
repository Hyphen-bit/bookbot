def words_in_book(text):
    wordlist = text.split()
    print(f"{len(wordlist)} words found in the document")

def character_occ(text):
    #convert string to lowercase
    text = text.lower()
    #define blank dictionary
    occ = {}
    #for each character in string, check if in dict, if so increment value by 1 if if not create value.
    for character in text:
        if character in occ:
            occ[character] +=1
        else:
            occ[character] = 1
    return occ


def dict_list(dic):
    #define getcount function
    def getcount(adic):
        return adic["num"]
    
    #convert dictionary to LIST of individual dictionairies.
    #must create two entries in each dictionary, storing each propery, character and number as seperate key-value pairs.
    dict_list = []
    for entry in dic:
        dict_list.append({"char":entry,"num":dic[entry]})
    return dict_list


d = {'t': 29493, 'h': 19176, 'e': 44538, ' ': 70480, 'p': 5952, 'r': 20079, 'o': 24494, 'j': 497, 'c': 9011, 'g': 5795, 'u': 10111, 'n': 23643, 'b': 4868, 'k': 1661, 'f': 8451, 'a': 25894, 's': 20360, 'i': 23927, ';': 1350, ',': 5962, 'm': 10206, 'd': 16318, '\n': 7630, 'y': 7756, 'w': 7450, 'l': 12306, 'v': 3737, '.': 3121, '-': 173, ':': 211, '2': 19, '3': 15, '0': 18, '1': 91, '[': 2, '#': 1, '4': 12, '5': 12, ']': 2, '&': 5, '8': 24, '/': 8, '*': 97, '’': 144, 'x': 691, '_': 124, 'q': 325, '?': 208, '—': 123, '6': 9, 'z': 235, '(': 35, ')': 35, '7': 18, 'æ': 28, '!': 201, '“': 506, '”': 316, '9': 9, 'ë': 2, '‘': 43, 'â': 8, 'ê': 7, 'ô': 1, '™': 57, '•': 4, '%': 1, '$': 2}
