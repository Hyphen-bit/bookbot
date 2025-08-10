def words_in_book(text):
    wordlist = text.split()
    return len(wordlist)

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


def dict_lists(dic):
    #define getcount function
    def getcount(adic):
        return adic["num"]

    #convert dictionary to LIST of individual dictionairies.
    #must create two entries in each dictionary, storing each propery, character and number as seperate key-value pairs.
    dict_list = []
    for entry in dic:
        dict_list.append({"char":entry,"num":dic[entry]})
    #apply sort method to new list of dictionaries (char,number key value pairs), use getcount function as argument
    dict_list.sort(reverse=True,key=getcount)
    return dict_list
