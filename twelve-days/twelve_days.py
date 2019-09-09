def recite(start_verse, end_verse):
    data=open('data','r')
    line = [line for line in data if line != "\n"]
    l= [line[no].replace("\n","")  if "\n" in line[no] else line[no] for no in range(start_verse-1 , end_verse ) ]
    print l
    return l




