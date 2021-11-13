
t=int(input('Enter test case number:'))
output=list()
result=list()
for _  in range(t):
    n=int(input("Enter counter list number:"))
    list_num=list(map(int,input('Enter numbers of list:').split()))
    #result=list()
    for i in range(n):
        res=0
        #output=0
        res+=max(0,list_num[i]-(i+1+res))
    result.append(res)
    # last=result.pop()
    # output.append(last)
for i in result:
    print(i)

