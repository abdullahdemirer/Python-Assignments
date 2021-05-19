def inn_mod(life,counter,list_out=[],list_in=[],listy=[],letter=[],word=[]):
    gu=life
    c=0
    w=len(word)
    leng=len(letter)
    cou=counter
    t=(leng-cou)
    for i in letter[t:]:
        a=0
        b=0
        for j in range(len(word)):
            if( i == word[j]) and (i) not in list_in:
                a=a+1
                listy[j]=word[j]
            elif(i == word[j]) and i in list_in:
                b=b+1


        if(a>0):
            print ("Guessed word:",i," You are in IN mod")
            print (" You have",gu,"guesses left")
            print (listy)
            print ("---------------------------------------------")
            list_in.append(i)
            cou=cou-1
            for p in range(len(word)):
                if(listy[p]==word[p]):
                   c=c+1
            if(c==w) and gu!=0:
                print ("You won the game")
                break
            elif(c!=w) and gu==0 and cou==0:
                print ("You lost game")
                break
            elif(c!=w) and gu==0 and cou!=0:
                print ("You lost the game")
                break
            elif (c != w) and gu != 0 and cou == 0:
                print ("You finished all leters")
                print ("You lost the game")
                break
            c=0
        elif(b>1):
            gu = gu- 1
            print ("Guessed word:",i, " is used in IN mode. The game turned into OUT mode")
            print (" You have", gu, "guesses left")
            print (listy)
            print ("---------------------------------------------")
            list_in.append(letter[i])
            cou=cou-1
            for p in range(len(word)):
                if(listy[p]==word[p]):
                   c=c+1
            if(c==w) and gu!=0:
                print ("You won the game")
                break
            elif(c!=w) and gu==0 and cou==0:

                print ("You lost game")
                break
            elif(c!=w) and gu==0 and cou!=0:
                print ("You lost the game")
                break
            elif (c != w) and gu != 0 and cou == 0:
                print ("You finished all leters")
                print ("You lost the game")
                break
            c=0
            return out_mod(gu,cou, list_out, list_in, listy, letter, word)
        else:
            gu=gu-1
            print ("Guessed word:",i, " The game turned into OUT mode")
            print (" You have",gu, "guesses left")
            print (listy)
            print ("---------------------------------------------")
            list_in.append(i)
            cou=cou-1
            for p in range(len(word)):
                if(listy[p]==word[p]):
                   c=c+1
            if(c==w) and gu!=0:
                print ("You won the game")
                break
            elif(c!=w) and gu==0 and cou==0:
                print ("You lost game")
                break
            elif(c!=w) and gu==0 and cou!=0:
                print ("You lost the game")
                break
            elif (c != w) and gu != 0 and cou == 0:
                print ("You finished all leters")
                print ("You lost the game")
                break
            c=0

            return out_mod(gu,cou, list_out, list_in, listy, letter, word)




def out_mod(life,counter,list_out=[],list_in=[],listy=[],letter=[],word=[]):
    length=len(letter)
    coun=counter
    w=len(word)
    c=0
    q=len(word)
    k=(length-coun)
    for i in letter[k:]:
        a=len(word)
        b=len(word)
        for j in range(len(word)):
            if i!= word[j] and i not in list_out :
                a=a-1
            elif i!= word[j] and i  in list_out :
                b=b-1
        if (a == 0):
            print ("Guessed word:", i, " The game turned into IN mode")
            print (" You have", life, "guesses left")
            print (listy)
            print ("---------------------------------------------")
            list_out.append(i)
            coun= coun - 1
            for p in range(len(word)):
                if(listy[p]==word[p]):
                   c=c+1
            if(c==w) and life!=0:
                print ("You won the game")
                break
            elif(c!=w) and life==0 and coun==0:
                print ("You lost game")
                break
            elif(c!=w) and life==0 and coun!=0:
                print ("you lost the game")
                break
            elif (c != w) and life != 0 and coun == 0:
                print ("You finished all leters")
                print ("You lost the game")
                break
            c=0
            return inn_mod(life, coun, list_out, list_in, listy, letter, word)
        elif (b<q):
            life = life - 1
            print ("Guessed word:", i, " is used in OUt mode. The game turned into OUT mode")
            print (" You have", life, "guesses left")
            print (listy)
            print ("---------------------------------------------")
            list_out.append(i)
            coun = coun-1
            for p in range(len(word)):
                if(listy[p]==word[p]):
                   c=c+1
            if(c==w) and life!=0:
                print ("You won the game")
                break
            elif(c!=w) and life==0 and coun==0:
                print ("You lost game")
                break
            elif(c!=w) and life==0 and coun!=0:
                print ("You lost the game")
                break
            elif (c != w) and life != 0 and coun == 0:
                print ("You finished all leters")
                print ("You lost the game")
                break
            c=0

        else:
            life=life-1
            print ("Guessed word:",i, " You are in OUT mode")
            print (" You have", life, "guesses left")
            print (listy)
            print ("---------------------------------------------")
            list_out.append(i)
            coun=coun-1
            for p in range(len(word)):
                if(listy[p]==word[p]):
                   c=c+1
            if(c==w) and life!=0:
                print ("You won the game")
                break
            elif(c!=w) and life==0 and coun==0:
                print ("You lost game")
                break
            elif(c!=w) and life==0 and coun!=0:
                print ("You lost the game")
                break
            elif (c != w) and life != 0 and coun == 0:
                print ("You finished all leters")
                print ("You lost the game")
                break
            c=0

def in_mod(y,guess,word=[],letter=[],list_in=[],listy=[],list_out=[]):
    counter=y
    w=len(word)
    c=0
    life=guess
    for i in range(len(letter)):
        a=0
        b=0
        for j in range(len(word)):
            if(letter[i] == word[j]) and (letter[i]) not in list_in:
                a=a+1
                listy[j]=word[j]
            elif(letter[i] == word[j]) and (letter[i]) in list_in:
                b=b+1


        if(a>0):
            print ("Guessed word:",letter[i]," You are in IN mod")
            print (" You have",life,"guesses left")
            print (listy)
            print ("---------------------------------------------")
            list_in.append(letter[i])
            counter=counter-1
            for p in range(len(word)):
                if(listy[p]==word[p]):
                   c=c+1
            if(c==w) and life!=0:
                print ("You won the game")
                break
            elif(c!=w) and life==0 and counter==0:
                print ("You lost game")
                break
            elif(c!=w) and life==0 and counter!=0:
                print ("You lost the game")
                break
            elif (c != w) and life != 0 and counter == 0:
                print ("You finished all leters")
                print ("You lost the game")
                break
            c=0
        elif(b>1):
            life = life - 1
            print ("Guessed word:", letter[i], " is used in IN mode. The game turned into OUT mode")
            print (" You have", life, "guesses left")
            print (listy)
            print ("---------------------------------------------")
            list_in.append(letter[i])
            counter=counter-1
            for p in range(len(word)):
                if(listy[p]==word[p]):
                   c=c+1
            if(c==w) and life!=0:
                print ("You won the game")
                break
            elif(c!=w) and life==0 and counter==0:
                print ("You lost game")
                break
            elif(c!=w) and life==0 and counter!=0:
                print ("You lost the game")
                break
            elif (c != w) and life != 0 and counter == 0:
                print ("You finished all leters")
                print ("You lost the game")
                break

            c=0
            return out_mod(life,counter, list_out, list_in, listy, letter, word)
        else:
            life=life-1
            print ("Guessed word:",letter[i], " The game turned into OUT mode")
            print (" You have", life, "guesses left")
            print (listy)
            print ("---------------------------------------------")
            list_in.append(letter[i])
            counter=counter-1
            for p in range(len(word)):
                if(listy[p]==word[p]):
                   c=c+1
            if(c==w) and life!=0:
                print ("You won the game")
                break
            elif(c!=w) and life==0 and counter==0:
                print ("You lost game")
                break
            elif(c!=w) and life==0 and counter!=0:
                print ("You lost the game")
                break
            elif(c!=w) and life!=0 and counter==0:
                print ("You finished all leters")
                print ("You lost the game")
                break
            c=0
            return out_mod(life,counter, list_out, list_in, listy, letter, word)


import sys
word = str(sys.argv[1])
letter = str(sys.argv[2].split(','))
letter=eval(letter)
y=len(letter)
x=len(sys.argv[1])
listy=[]
guess=5
list_in=[]
list_out=[]
for i in range(0,x,1):
    listy.append('-')
print("You have 5  guesses left ")
print( listy)
print ("---------------------------------------------")

y=in_mod(y,guess,word,letter,list_in,listy,list_out)

