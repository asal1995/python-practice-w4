def Linear_Keyboard()->int:
    n= int(input('enter a number:'))                
    for _ in range(n):
        keyboard = input('enter your keyboard: ')   
        s = input('enter your word:')              

        # for i in range(1, len(s)):    

        #                             #S characters on the keyboard are found by the index method.
        #                             # Then the sum value of the difference of successive keys is calculated
        #     print(sum([abs(keyboard.index(s[i]) - keyboard.index(s[i-1]))]))
        # print(result)
        print(sum([abs(keyboard.index(s[i]) - keyboard.index(s[i - 1]))
            for i in range(1, len(s))]))

if __name__=="__main__":
                  
    Linear_Keyboard()
