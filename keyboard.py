#Minimum click time
def Linear_Keyboard(n:int,keyboard:str,s:str)->int:
  
# The loop calculates the minimum time required to type the word s on the keyboard.

    for i in range(1, len(s)):    

                                #S characters on the keyboard are found by the index method.
                                # Then the sum value of the difference of successive keys is calculated
        result= sum([abs(keyboard.index(s[i]) - keyboard.index(s[i-1]))])
    print(result)
    

if __name__=="__main__":
    n= int(input('enter a number:'))                # input an integer in range(1,1000)
    for _ in range(n):
        keyboard = input('enter your keyboard: ')   #input your Keyboard with custom layout
        s = input('enter your word:')               #input yor word or phrase
    Linear_Keyboard(n,keyboard,s)
