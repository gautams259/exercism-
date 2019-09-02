def is_isogram(string):
    c=0
    string = string.lower()
    for i in string:
        if i not in "$_,- " and  string.count(i) >1:
            c=c+1
            print i
    if c==0:
        return True
    else:
        return False



print(is_isogram("alphAbet"))
