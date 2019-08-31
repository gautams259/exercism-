from collections import Counter

def count_words(sentence):

    sentence=sentence.replace('_'," ")
    sentence=sentence.replace(','," ")
    phrase = str("".join(filter(lambda x :x not in "!&@$%^:.,", sentence.lower())))
    phrase = [i.replace("'","") if i[0]=="'" or i[-1]=="'" else i for i in phrase.split()]
    return Counter(map(str,phrase))
    



count_words("Joe can't tell_between_app, apple and a.")

