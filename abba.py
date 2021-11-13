n=int(input('enter a number:'))     #number of teast case
ab=0
ba=0
while n>0:
    s=str(input('enter your string:'))    
    d=[]
    ab=0
    ba=0
    for i in s:        #loop of list input
        d+=[i]
    #else:
        for i in range(len(s)):
            try:
                if d[i]=="a":
                    if d[i+1]=="b":
                        ab+=1
                elif d[i]=="b":
                    if d[i+1]=="a":
                        ba+=1
            except IndexError:
                break
    if ab==ba:
        print(s)
        
    elif len(s)==1:
        print(s)
        
    elif ab>ba:
        d[len(d)-1]="a"
        for i in d:
            print(i,end="")
        print()
    else:
        d[len(d)-1]="b"
        for i in d:
            print(i,end="")
        print()
    n-=1
