import sys
import operator
def test(built,ful_knowledge):#built ilk girdi / ful_knowldge ise tüm bilgilerin tutulduğu yer

    try:

        l=built.split(',')
        let=l[0]
        assert let == 'A' or let == 'R' or let == 'S' or let == 'L' or let == 'E' or let == 'H' or let == 'Q'
        if(l[0]=='A'):
            return test_A(built,ful_knowledge)

        elif (l[0] == 'S'):
            return test_S(built,ful_knowledge)

        elif (l[0] == 'R'):
            return test_R(built, ful_knowledge)

        elif (l[0] == 'H'):
            return test_H(built, ful_knowledge)

        elif (l[0] == 'L'):
            return test_L(built, ful_knowledge)
        
        elif (l[0] == 'Q'):
            return test_Q(built, ful_knowledge)

        elif (l[0] == 'E'):
            return test_E(built, ful_knowledge)

    except AssertionError:
        print('Yanlıs İslem sectiniz... ')
        new_input = input("Enter Command:")
        return test(new_input, ful_knowledge)

def test_A(knowledge,special): # knowlde=girdi / specil tüm bilgiler
        tru_knowledge=[]
        try:
            t=knowledge.split(',')
            if(len(t)!=7):
                raise AttributeError#ben giris sayını kontol etmek ıcın olusturdum bu hatayı
            letter=t[0]
            serial=t[1]
            price=t[2]
            name=t[3]
            genre=t[4]
            director=t[5]
            state=t[6]
            serial=int(serial)
            price=int(price)
            for i in range(3,7,1):
                k=0
                for j in t[i]:
                    if j=='\"':
                        k=k+1
                if(k!=2):
                    raise ZeroDivisionError#çift tırnak kullanımı
            tru_knowledge.append(serial)
            tru_knowledge.append(price)


            for i in special:
                if (serial == i[0]):
                    raise StopIteration #serial numara kontrolü

            for i in range(3, 7, 1):
                k=t[i][1:-1]
                b=0
                for j in k:
                    if j==' ':
                        b=b+1
                if(len(k)==b or len(k)==0):
                    raise ReferenceError
                tru_knowledge.append(k)

            if tru_knowledge[3] != 'Action' and  tru_knowledge[3] != 'Fantastic' and tru_knowledge[3] != 'Love' and tru_knowledge[3] != 'History' and tru_knowledge[3] != 'Horror':
                print ("Genre of a movie can be Action,Fantastic,Love,History and Horror.")
                x = input("Enter Command:")
                return test(x, special)
            if tru_knowledge[5]!="Inv" :
                print(" Yeni girilen dvd state Inv olmak zorunda.. Lutfen bastan giriniz")
                x = input("Enter Command:")
                return test(x, special)

            return (tru_knowledge)


        except ValueError:
            print ('Price and Serial Must be integer ...Input Definition: A,{serial},{price},{Name},{Genre},{Director},{State}')
            x = input("Enter Command:")
            return test(x, special)
        except AttributeError:
            print ("Input degerlerini eksik girdiniz !Input Definition: A,{serial},{price},{Name},{Genre},{Director},{State}")
            x = input("Enter Command:")
            return test(x, special)
        except ZeroDivisionError:
            print ("Input Definition:Lutfen Name,Genre,Director ve State girerken \" Name vb.\" seklinde giriniz")
            x = input("Enter Command:")
            return test(x, special)
        except ReferenceError:#virgul koyup birsey yazmaz veya icini bosluk doldurursa
            print ("Lutfen tum degerleri doldurunuz..Input Definition: A,{serial},{price},{Name},{Genre},{Director},{State}")
            x = input("Enter Command:")
            return test(x, special)
        except StopIteration:
            print ("Lutfen Farkli Serial Numarasi Deneyiniz!")
            x = input("Enter Command:")
            return test(x, special)


def test_S(knowledge_s,special_s):
    deger=[]
    coun_s=0
    try:
        t=knowledge_s.split(',')
        if(len(t)!=2):
            raise ZeroDivisionError
        search=t[1]
        for i in range(1, 2, 1):
            k = 0
            for j in t[i]:
                if j == '\"':
                    k = k + 1
            if (k != 2):
                raise ValueError

        for i in range(1, 2, 1):
            l = t[i][1:-1]
            b = 0
            for j in l:
                if j == ' ':
                    b = b + 1
                if (len(l) == b or len(l) == 0):
                    print ("Lutfen inputu dogru giriniz S,{Name}")
                    x = input("Enter Command:")
                    return test(x, special_s)
                else:
                    deger.append(l)
        if(len(deger[0])<3):
            raise ReferenceError
        if(len(special_s)==0):
            print ("Kayıtta Hıc dosya bulunamamaktadır uzgunuz bu ıslemı gerceklestıremezsınız..")
            x = input("Enter Command:")
            return test(x, special_s)

        for i in special_s:
            if(deger[0] in i[2]):
                print ("serial:%d" % (i[0]))
                print ("price:%d" % (i[1]))
                print ("name:%s" % (i[2]))
                print ("genre:%s" % (i[3]))
                print ("director:%s" % (i[4]))
                print ("state:%s" % (i[5]))
                print ("\n")
            else:
                coun_s=coun_s+1
        if(coun_s==len(special_s)):
            print ("Girdiginiz bilgiyi iceren hic bir kayıt bulunmamaktadır.")
            x = input("Enter Command:")
            return test(x, special_s)
    except ReferenceError:
        print ("Gireceginiz bilgi minumum 3 karakterli olmalidir.")
        x = input("Enter Command:")
        return test(x, special_s)
    except ZeroDivisionError:
        print ("Lütfen 2 adet deger giriniz...")
        x = input("Enter Command:")
        return test(x, special_s)
    except ValueError:
        print ("Aradiginiz degeri \" \" arasina yaziniz")
        x = input("Enter Command:")
        return test(x, special_s)
    finally:
        print ("-----HUBM DVD-----")
        print ('A:  Add new  dvd\n'
               'R:  Remove   dvd\n'
               'S:  Search   dvd\n'
               'L:  List     dvd\n'
               'E:  Edit     dvd\n'
               'H:  Hire     dvd\n'
               'Q:  Quit')
        x = input("Enter Command:")
        return test(x, special_s)



def test_R(knowledge_r,special_r):
    counter=[]#listenin içine attım serialle ulasan degeri
    cou=0# hangi indiste oldugunu bulamama yardım etti
    try:
        know_r=knowledge_r.split(',')
        serial_r=know_r[1]#seriali giristen aldik
        serial_r=int(serial_r)#integere cevirdim
        if len(know_r)!=2:
            raise IndexError

        for i in special_r:
            if(i[0]==serial_r):
                print ("serial:%d" % (i[0]))
                print ("price:%d" % (i[1]))
                print ("name:%s" % (i[2]))
                print ("genre:%s" % (i[3]))
                print ("director:%s" % (i[4]))
                print ("state:%s" % (i[5]))
                karar=input("Bu Bilgileri Gercekten Silmek Istiyor musunuz? [Y/N]")
                if(karar=='Y'):
                    if(i[5]=='Hired'):
                        print ("Bu Bilgilerin state Hired oldugu icin bu bigileri silemezsininz! Lutfen baska serial giriniz ")
                        x = input("Enter Command:")
                        return test(x, special_r)
                    else:
                         counter.append(cou)
                elif(karar=='N'):
                    x = input("Enter Command:")
                    return test(x, special_r)
                else:
                    print ("hatali islem islem..")
                    x = input("Enter Command:")
                    return test(x, special_r)
            else:
                cou=cou+1
        if(len(special_r)==0):
            print ("Kayıtta hic dosya yoktur bu islemi yapamazsiniz..Lutfen baska islem seciniz")
            x = input("Enter Command:")
            return test(x, special_r)
        elif(cou==len(special_r)):
            print ('Girdiginiz serial degeri yoktur ... Lutfen bastan giriniz.')
            x = input("Enter Command:")
            return test(x, special_r)
        else:
            special_r.pop(counter[0])


        special_r.insert(0,'R')
        return (special_r)

    except IndexError:
        print ("Gırıs isleminiz hatalidir .. Input Definition: R,serial ")
        x = input("Enter Command:")
        return test(x, special_r)
    except ValueError:
        print ("Serial number must be integer ")
        x = input("Enter Command:")
        return test(x, special_r)


def test_H(knowledge_h,special_h):
    coun_h=0
    try:

        know_h = knowledge_h.split(',')
        if (len(know_h)) < 2:
            print (" Eksik deger girdiniz Lutfen Modunuzu ve Serial numaranizi giriniz!")
            x = input("Enter Command:")
            return test(x, special_h)
        elif (len(know_h) > 2):
            print (" Fazla deger girdiniz Lutfen Modunuzu ve Serial numaranizi giriniz!")
            x = input("Enter Command:")
            return test(x, special_h)

        serial_h=know_h[1]
        serial_h=int(serial_h)

        for i in special_h:
            if(i[0]==serial_h):
                    if(i[5]=='Hired'):
                        print("State Durumunuz Hired dır tekrar Hiredlıyamazsiniz..")
                        x = input("Enter Command:")
                        return test(x, special_h)
                    else:
                        i[5] = 'Hired'
                        print ("serial:%d" % (i[0]))
                        print ("price:%d" % (i[1]))
                        print ("name:%s" % (i[2]))
                        print ("genre:%s" % (i[3]))
                        print ("director:%s" % (i[4]))
                        print ("state:%s" % (i[5]))

            else:
                coun_h=coun_h+1
        if(len(special_h)==0):
            print ("Kayıtta hic dosya bulunmamaktadır, uzgunuz bu islemi gerceklestiremezsiniz...")
            x = input("Enter Command:")
            return test(x, special_h)

        if(coun_h==len(special_h)):
            print (" Girdiginiz Seriale ait hic bir kayıt bulunmamaktadir.... Lutfen tekrar deneyin")
            x = input("Enter Command:")
            return test(x, special_h)

        special_h.insert(0, 'H')
        return (special_h)

    except ValueError:
        print (" Serial numarasi integer olmak zorunda.")
        x = input("Enter Command:")
        return test(x, special_h)




def test_E(knowledge_e,special_e):
    bilgi=[]
    coun_e=0
    try:

       if(len(special_e)==0):
           print ("Kayitli hicbir bilgi yoktur bu islemi gerceklestiremezsiniz...")
           x = input("Enter Command:")
           return test(x, special_e)

       know_e=knowledge_e.split(',')
       if(len(know_e)<3):
           print ("en az 3 deger girmeniz geremektedir.Mod ,Serial ve degistirmek istediginiz bilgi..")
           x= input("Enter Command:")
           return test(x, special_e)
       serial_e=know_e[1]
       serial_e=int(serial_e)
       for i in range(2, len(know_e), 1):
           k = 0
           l=0
           for j in know_e[i]:
               if j == '{':
                   k = k + 1
               if j=='}':
                   l=l+1
           if (l!=1) or (k!=1):
               print ("lutfen degestireceginiz degerleri { } icerisinde yaziniz....")
               x = input("Enter Command:")
               return test(x, special_e)


       for i in special_e:
           if(i[0]==serial_e):#seriale uygun mu
                for j in range(2,len(know_e),1):
                    z = know_e[j][1:-1]#{} ayırdık
                    z1=z.split('=')#= den ayırdim
                    if(len(z1)!=2):# z1 i kontrol ettik
                        print ("Dogru islem yapmadiniz.. {Name=\"yeni isim\"} seklinde giris yapın")
                        x = input("Enter Command:")
                        return test(x, special_e)
                    else:
                        if(z1[0]=='Name'):
                            tirnak=0
                            new_value=z1[1]
                            for m in new_value:
                                if m == '\"':
                                    tirnak = tirnak + 1
                            if(tirnak!=2):
                                print ("Name degerini degistirmek yeni simi \" \" icerisinde yaziniz")
                                x = input("Enter Command:")
                                return test(x, special_e)
                            else:
                                new_name=new_value[1:-1]
                                i[2]=new_name


                        elif(z1[0]=='Genre'):
                            tirnak=0
                            new_value=z1[1]
                            for m in new_value:
                                if m == '\"':
                                    tirnak = tirnak + 1
                            if(tirnak!=2):
                                print ("Genre degerini degistirmek yeni simi \" \" icerisinde yaziniz")
                                x = input("Enter Command:")
                                return test(x, special_e)
                            else:
                                new_genre=new_value[1:-1]
                                if new_genre != 'Action' and new_genre != 'Fantastic' and new_genre != 'Love' and new_genre != 'History' and new_genre != 'Horror':
                                    print ("Genre of a movie can be Action,Fantastic,Love,History and Horror.")
                                    x = input("Enter Command:")
                                    return test(x, special_e)
                                else:
                                    i[3]=new_genre
                        elif (z1[0] == 'Director'):
                            tirnak = 0
                            new_value = z1[1]
                            for m in new_value:
                                if m == '\"':
                                    tirnak = tirnak + 1
                            if (tirnak != 2):
                                print ("Director degerini degistirmek yeni simi \" \" icerisinde yaziniz")
                                x = input("Enter Command:")
                                return test(x, special_e)
                            else:
                                new_director = new_value[1:-1]
                                i[4] = new_director

                        elif (z1[0] == 'State'):
                            print ("State modunu degistiremezsiniz...Hatal islem")
                            x = input("Enter Command:")
                            return test(x, special_e)

                        elif (z1[0] == 'Price'):
                            tirnak = 0
                            new_value = z1[1]
                            if new_value != int(new_value):
                                raise TypeError
                            else:
                                i[1]=new_value

                        elif (z1[0] == 'Serial'):
                            print ("Serial modunu degistiremezsiniz...Hatal islem")
                            x = input("Enter Command:")
                            return test(x, special_e)
                        else:
                            print ("Lutfen Buyuk harf kullanınız Name,Genre,Price,State,Director,Serial")
                            x = input("Enter Command:")
                            return test(x, special_e)
           else:
                coun_e=coun_e+1
       if(len(special_e)==coun_e):
           print ("Girdiginiz serial degeri ile herhangi bir kayıt uyusmamaktadır..Lutfen tekrar deneyin")
           x = input("Enter Command:")
           return test(x, special_e)

    except ValueError:
        print("Serial  degeri integer olmak zorunda")
        x = input("Enter Command:")
        return test(x, special_e)
    except TypeError:
        print("Degistirmek istedigin Price  degeri integer olmak zorunda")
        x = input("Enter Command:")
        return test(x, special_e)
    except NameError:
        print("Degistirmek istedigin Serial  degeri integer olmak zorunda")
        x = input("Enter Command:")
        return test(x, special_e)

    finally:
        special_e.insert(0,'E')
        return (special_e)

def test_Q(knowledge_q, special_q):
    know_q = knowledge_q.split(',')
    if (len(know_q) != 1):
        print ("Giris isleminiz hatalidir..Input Definition: Q")
        x = input("Enter Command:")
        return test(x, special_q)

    yazilecek=open("dvdStore.txt","w")
    for i in special_q:
        for j in range(0,6,1):
            if(j==1 or j==0):
                yazilecek.write("%d,"%(i[j]))
            elif (j==2 or j==3 or j==4):
                yazilecek.write("%s," % (i[j]))
            else:
                yazilecek.write("%s;" % (i[j]))
        yazilecek.write('\n')
    return ("Q")

def test_L(knowledge_l,special_l):
    copy=[]
    number=1

    know_l = knowledge_l.split(',')
    if(len(know_l)!=1):
        print ("Giris isleminiz hatalidir..Input Definition: L")
        x = input("Enter Command:")
        return test(x, special_l)

    x_value=['Serial','Price','Name','Genre','Director','State']
    x_valu2=[10,10,22,14,14,14]
    alt_tr=[3,3,15,9,9,9]
    for i in range(0,6,1):
        print (x_value[i]+(x_valu2[i]-len(x_value[i]))*' ',end='')
    print("")
    for i in range(0, 6, 1):
        print ((alt_tr[i]*'-')+(x_valu2[i] - alt_tr[i])*' ',end='')
    print("",end='')
    copy=special_l[:]

    special_l.sort(key=operator.itemgetter(2))
    for i in special_l:
        if(number%2!=0):
            print ('')
            for j in range(0,6,1):
                sayi=1
                if(j==1 or j==0):
                    number_l=i[j]
                    while (number_l > 9):
                        number_l=number_l//10
                        sayi=sayi+1
                    print (i[j],((x_valu2[j]-1)-sayi)*' ',end='')
                else:
                    print (i[j],((x_valu2[j]-1)-len(i[j]))*' ',end='')

            number=number+1

        else:
            print ('')
            print ('Press Enter...')
            onay = input('')
            if onay=="":
                for j in range(0,6,1):
                    sayi=1
                    if(j==1 or j==0):
                        number_l=i[j]
                        while (number_l > 9):
                            number_l=number_l//10
                            sayi=sayi+1
                        print (i[j],((x_valu2[j]-1)-sayi)*' ',end='')
                    else:
                        print (i[j],((x_valu2[j]-1)-len(i[j]))*' ',end='')
                number=number+2
            else:
                print ("Giris isleminiz hatalidir...")
                break
    print ()
    print ("-----HUBM DVD-----")
    print ('A:  Add new  dvd\n'
                   'R:  Remove   dvd\n'
                   'S:  Search   dvd\n'
                   'L:  List     dvd\n'
                   'E:  Edit     dvd\n'
                   'H:  Hire     dvd\n'
                   'Q:  Quit')
    x = input("Enter Command:")
    return test(x, copy)


t=10
full_knowledge=[]
try:
    dosya_bilgi=[]
    with open(sys.argv[1], 'r') as dosya:
        for i in dosya.read().split('\n'):
            cc=i.split(',')
            for j in range(0,6):
                if(j==0 or j==1):
                    y = cc[j]
                    k=''
                    for l in y:
                        if(l!=' '):
                          k=k+l
                    y=k
                    y=int(y)
                    dosya_bilgi.append(y)
                elif(j==2 or j==3 or j==4):
                    y = cc[j]
                    k=''
                    sayac=0
                    for l in y:
                        if(l!=' '):
                            if(sayac==0):
                                k=k+l
                            else:
                                if (ord(l) > 90):
                                    k = k + l
                                else:
                                    k = k + ' ' + l
                            sayac=sayac+1
                    y=k
                    dosya_bilgi.append(y)
                else:
                    y=cc[j].split(';')
                    k=''
                    sayac=0
                    for l in y[0]:
                        if(l!=' '):
                            if(sayac==0):
                                k=k+l
                            else:
                                if (ord(l) > 90):
                                    k = k + l
                                else:
                                    k = k + ' ' + l
                    y[0]=k
                    dosya_bilgi.append(y[0])
            full_knowledge.append(dosya_bilgi)
            dosya_bilgi=[]
except (IOError,IndexError):
    print ("",end='')
except ValueError:
    print ("",end='')
finally:
    print()

z=True
while(z==True):
    erro_r = []
    c=0
    print ("-----HUBM DVD-----")
    print ('A:  Add new  dvd\n'
           'R:  Remove   dvd\n'
           'S:  Search   dvd\n'
           'L:  List     dvd\n'
           'E:  Edit     dvd\n'
           'H:  Hire     dvd\n'
           'Q:  Quit')
    x_ilk= input("Enter Command:")

    erro_r=test(x_ilk,full_knowledge)


    if(erro_r[0]=='R' or erro_r[0]=='E' or erro_r[0]=='H' ):
        del erro_r[0]
        full_knowledge=erro_r

    elif (erro_r[0] == 'Q'):
        z = False
    else:
        full_knowledge .append(erro_r)



dosya.close()
