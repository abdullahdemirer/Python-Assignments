def sifre(liste=[]):
    key=[]
    sayi = ['0', '1']
    for i in range(len(liste)):
        if liste[i][0] not in sayi:
            key.append(liste[i])
    return key

def var_mi(liste=[]):
    new_list=[]
    sayi=['0','1']
    for i in range(len(liste)):
        for j in range(len(sayi)):
            if(liste[i][0] == sayi[j]):
                new_list.append(liste [i])
    return new_list

def binary_hex(binary_list=[]):
    hexi = []
    hexi1 = []

    for i in binary_list[::-1]:
        hexi1.append(i)
    t=len(hexi1)

    for i in range(0, t, 4):
        a = 0
        toplam=0
        while a < 4:
            toplam = toplam + int(hexi1[i]) * (2 ** a)
            a = a + 1
            i = i + 1
        if (toplam > 9):
            if (toplam == 10):
                hexi.append("A")
            elif (toplam == 11):
                hexi.append("B")
            elif (toplam == 12):
                hexi.append("C")
            elif (toplam == 13):
                hexi.append("D")
            elif (toplam == 14):
                hexi.append("E")
            elif (toplam == 15):
                hexi.append("F")
        else:
            hexi.append(toplam)

    return hexi

def find(liste=[],lis1=[],list2=[]):#list1 l list2 7F
    t=len(liste)
    letter=[]
    for i in range(0,t,2):
        bil=0
        bil=str(bil)
        l=i+1
        bil=str(liste[i])+str(liste[l])
        for i in range(len(list2)):
            if(bil==list2[i]):
                letter.append(lis1[i])
            else:
                i=i+1
    return letter

def findd(liste=[],lis1=[],list2=[]):#list1 l list2 7F
    numb=[]
    for i in range(len(liste)):
        for j in range(len(lis1)):
            if(liste[i]==lis1[j]):
                numb.append(list2[j])
            else:
                j=j+1
    return numb


def complement(key_i=[]):
    n_liste=[]
    comp=[]
    list2=[]
    sayi=['1','0']
    key_i=str(key_i)
    for i in key_i[0::]:
        if i in sayi:
           n_liste.append(i) #listeyi parcalara ayırdık '1'
    if(n_liste[0]=='1'):#listenin ilk elemanını kontrol ettik...
        for i in n_liste[::-1]:
            comp.append(i)  #listeyi ters çevir
        for i in range(len(comp)):
            if comp[i]=='1':
                list2.append('0')
            else:
                list2.append('1')
        comp=[]
        toplam = int(list2[0]) + 1
        if toplam < 2:
            list2[0]=toplam
            for i in list2[::-1]:
                comp.append(i)
            return neg_binary_dec(comp)
        else:
            list2[0] = toplam
            for i in range(len(list2)):
                if int(list2[i]) >= 2:
                    list2[i + 1] = int(list2[i + 1]) + (int(list2[i]) / 2)
                    list2[i] = list2(t[i]) % 2
            for i in list2[::-1]:
                comp.append(i)
            return neg_binary_dec(comp)
    else:
        return poz_binary_dec(n_liste)

def poz_binary_dec(numb=[]):
    poz_num = []
    for i in numb[::-1]:
        poz_num.append(i)
    a = 0
    toplam = 0
    for i in range(len(poz_num)):
        toplam = toplam + int(poz_num[i]) * (2 ** a)
        a = a + 1

    numb.insert(0, toplam)
    return numb

def neg_binary_dec(number=[]):
    neg_num=[]
    for i in number[::-1]:
        neg_num.append(i)
    a=0
    toplam=0
    for i in range(len(neg_num)):
        toplam=toplam+int(neg_num[i])*(2**a)
        a=a+1
    toplam=-(toplam)
    number.insert(0,toplam)
    return number
def repair(mes=[],key=[],lis_a=[],lis_b=[]):#message[i],valu,list_a=l,list_b=7F
    x=0
    new_mes=[]
    r=len(lis_a)
    for i in range(len(mes)):
        for j in range(len(lis_a)):
            if mes[i]==lis_a[j]:
                x=(j-(valu))%r
                new_mes.append(lis_a[x])
            else:
                j=j+1
    return new_mes

def repairt(mes=[], key=[], lis_a=[], lis_b=[]):  # message[i],valu,list_a=l,list_b=7F
        x = 0
        new_mes = []
        r = len(lis_a)
        for i in range(len(mes)):
            for j in range(len(lis_a)):
                if mes[i] == lis_a[j]:
                    x = (j + (valu) )% r
                    new_mes.append(lis_a[x])
                else:
                    j = j + 1
        return new_mes
def re(last_mesage=[]):
    be=[]
    for i in range(len(last_mesage)):
        y=len(last_mesage[i])
        a=str(last_mesage[i][0])
        for j in range(1,y,1):
            a=a+str(last_mesage[i][j])
        be.append(a)
    return be

def trans(hexlist=[]):
    numbers=[]
    for i in range((len(hexlist))):
        t = len(hexlist[i])
        for j in range(0, t, 1):
            l = len(hexlist[i][j])
            for k in range(l):
                numbers.append(hexlist[i][j][k])
    list_new = []
    sayilar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    for i in range(len(numbers)):
        t = 0
        for j in range(len(sayilar)):
            if numbers[i] == sayilar[j]:
                list_new.append(numbers[i])
            else:
                t = t + 1
            if (t == 10):
                if numbers[i] == ("A"):
                    list_new.append('10')

                elif numbers[i] == ("B"):
                    list_new.append('11')

                elif numbers[i] == ("C"):
                    list_new.append('12')

                elif numbers[i] == ("D"):
                    list_new.append('13')

                elif numbers[i] == ("E"):
                    list_new.append('14')

                elif numbers[i] == ("F"):
                    list_new.append('15')
    return hesap(list_new)
def hesap(liste=[]):
    liste_1=[]
    for i in liste[::-1]:
        liste_1.append(i)
    a = 0
    toplam = 0
    for i in range(len(liste_1)):
        toplam = toplam + (int(liste_1[i]) * (16 ** a))
        a = a + 1
    return hex_binary(toplam)


def hex_binary(sonuc):
    x = 0
    sayilar = []
    son1 = []
    while (sonuc >= 2):
        sayilar.append(int(sonuc % 2))
        sonuc = sonuc // 2
        x = x + 1
    sayilar.append(sonuc)
    y = len(sayilar)
    while True:
        if (y % 4 == 0):
            break
        else:
            y = y + 1
            x = x + 1
            sayilar.append(0)
    for i in sayilar[::-1]:
        son1.append(i)
    return son1




import sys
liste=[]#içinde binary sayilar var
new_list=[]
new_list2=[]


hurap_file = open(sys.argv[1], "r")
for i in hurap_file.read().split('\n'):
    liste.append(i)
sayi_mi=var_mi(liste)
sayi_mi_l=len(sayi_mi)
key=sifre(liste)

a=0
new = {}#içinde hex var
for i in range(len(sayi_mi)):
    hexi=binary_hex(sayi_mi[i])
    t=len(hexi)
    for i in range(t-1,-1,-1):
        new_list.append(hexi[i])
    new[a]=new_list
    new_list=[]
    a=a+1
for i in range(len(new)):
     new_list2.append(new[i])

print("""*********************
     Mission 00 
*********************""", end="\n\n")

print("""--- hex of encrypted code ---
-----------------------------""", end="\n\n")
for i in range(len(new_list2)):
    t=len(new_list2[i])
    for j in range(0,t,1):
        print (new_list2[i][j],end='')
    print('')


list_a=[]
list_b=[]
schuckscii_file = open(sys.argv[2], "r")
for i in schuckscii_file.read().split('\n'):
    y=i.split('\t')
    a1=y[1]
    a2=y[0]
    list_a.append(y[0])
    list_b.append(y[1])
word={}#içinde hafler var
for i in range((len(new_list2))):
    new_message=find(new_list2[i],list_a,list_b)
    word[i]=new_message
    new_message=0
message=[]
for i in range(len(word)):
        message.append(word[i])
print("""\n--- encrypted code ----
-----------------------""", end="\n\n")
for i in range(len(message)):
    t = len(message[i])
    for j in range(0, t, 1):
        print (message[i][j], end='')
    print('')
#complement alma kismi

new_number=complement(key)
valu=new_number[0]
del new_number[0]

sentence={}
for i in range(len(message)):
    message1=repair(message[i],valu,list_a,list_b)
    sentence[i]=message1
    message1=0
last_message=[]
for i in range(len(sentence)):
    last_message.append(sentence[i])
print("""\n--- decrypted code ---
----------------------""", end="\n\n")
for i in range(len(last_message)):
    t = len(last_message[i])
    for j in range(0, t, 1):
        print (last_message[i][j], end='')
    print('')

print("""\n*********************
     Mission 01 
*********************""", end="\n\n")
virus1=[]
virus_codes_file = open(sys.argv[3], "r")
for i in virus_codes_file.read().split('\n'):
    y=i.split(':')
    a=y[0]
    a1=y[1]
    virus1.append(y)

metin=re(last_message)
for i in virus1:
    for j in range(len(metin)):
        metin[j]=metin[j].replace(i[0],i[1])
for i in range(len(metin)):
    t = len(metin[i])
    for j in range(0, t, 1):
        print (metin[i][j], end='')
    print('')

message_las={}
for i in range(len(metin)):
    message_1 = repairt(metin[i], valu, list_a, list_b)
    message_las[i] = message_1
    message_1 = 0
lastt_message=[]
for i in range(len(message_las)):
    lastt_message.append(message_las[i])
print("""\n*********************
     Mission 10 
*********************""", end="\n\n")


print("""--- encrypted code ---
----------------------""", end="\n\n")

for i in range(len(lastt_message)):
    t = len(lastt_message[i])
    for j in range(0, t, 1):
        print (lastt_message[i][j], end='')
    print('')

new_hex={}
for i in range(len(lastt_message)):
    number_2=findd(lastt_message[i],list_a,list_b)
    new_hex[i]=number_2
    number_2=0
hexi_num=[]
for i in range(len(new_hex)):
    hexi_num.append(new_hex[i])
print("""\n--- hex of encrypted code ---
-----------------------------""", end="\n\n")

for i in range(len(hexi_num)):
    t=len(hexi_num[i])
    for j in range(0,t,1):
        print (hexi_num[i][j],end='')
    print('')
new_binary={}
print("""\n--- bin of encrypted code ---
-----------------------------""", end="\n\n")
for i in range(len(hexi_num)):
    binary=trans(hexi_num[i])
    new_binary[i]=binary
    binary=0

binary_last_number=[]
for i in range(len(new_binary)):
    binary_last_number.append(new_binary[i])

for i in range(len(binary_last_number)):
    t = len(binary_last_number[i])
    for j in range(0, t, 1):
        print (binary_last_number[i][j], end='')
    print('')

hurap_file.close()
schuckscii_file.close()
virus_codes_file.close()