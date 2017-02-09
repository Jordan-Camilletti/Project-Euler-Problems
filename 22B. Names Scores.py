"""I used this to split single line into multiple lines of names
I had to manualy remove single name line chunk."""

wrd="\n,"
with open("names.txt","r+")as n:
    for x in n.readline():
        if(x==","):
            n.write(wrd)
            wrd="\n"
        wrd+=x
