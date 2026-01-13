sentance=input('enter a sentance').         #to cehck different words in a sentence and no of time it repeats
d={}
words=sentance.split()
for word in words:
    if word not in d:
        d[word]=1
    else:
        d[word]+=1
print(d)