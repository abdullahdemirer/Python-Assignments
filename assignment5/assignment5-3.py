import sys
def bubble_sort(un_order_list):
    for j in range(len(un_order_list)):
        for i in range(len(un_order_list)-1):
            if un_order_list[i]>un_order_list[i+1]:
                temp=un_order_list[i]
                un_order_list[i]=un_order_list[i+1]
                un_order_list[i+1]=temp
    return un_order_list

def sayi_yap(alfabe):
    letter = {'a': '01', 'A': '01', 'b': '02', 'B': '02', 'c': '03', 'C': '03', 'ç': '04', 'Ç': '04', 'd': '05',
              'D': '05', 'e': '06', 'E': '06',
              'f': '07', 'F': '07', 'g': '08', 'G': '08', 'ğ': '09', 'Ğ': '09', 'h': '10', 'H': '10', 'ı': '11',
              'I': '11', 'i': '12', 'İ': '12',
              'j': '13', 'J': '13', 'k': '14', 'K': '14', 'l': '15', 'L': '15', 'm': '16', 'M': '16', 'n': '17',
              'N': '17', 'o': '18', 'O': '18',
              'ö': '19', 'Ö': '19', 'p': '20', 'P': '20', 'q': '21', 'Q': '21', 'r': '22', 'R': '22', 's': '23',
              'S': '23', 'ş': '24', 'Ş': '24',
              't': '25', 'T': '25', 'u': '26', 'U': '26', 'ü': '27', 'Ü': '27', 'v': '28', 'V': '28', 'w': '29',
              'W': '29', 'x': '30', 'X': '30',
              'y': '31', 'Y': '31', 'z': '32', 'Z': '32'}
    sayi = []#isimleri sayiya cevirdim

    for i in alfabe:
        k = ''
        for j in range(len(i)):
            k = k + letter[i[j]]
        sayi.append(k)

    return sayi

def harf_yap(harf_number):
    capital={'01':'A','02':'B','03':'C','04':'Ç','05':'D','06':'E','07':'F','08':'G',
             '09':'Ğ','10':'H','11':'I','12':'İ','13':'J','14':'K','15':'L','16':'M',
             '17':'N','18':'O','19':'Ö','20':'P','21':'Q','22':'R','23':'S','24':'Ş',
             '25':'T','26':'U','27':'Ü','28':'V','29':'W','30':'X','31':'Y','32':'Z',}
    low_letter={'01':'a','02':'b','03':'c','04':'ç','05':'d','06':'e','07':'f','08':'g',
             '09':'ğ','10':'h','11':'ı','12':'i','13':'j','14':'k','15':'l','16':'m',
             '17':'n','18':'o','19':'ö','20':'p','21':'q','22':'r','23':'s','24':'ş',
             '25':'t','26':'u','27':'ü','28':'v','29':'w','30':'x','31':'y','32':'z',}

    sayilar_var=[]#sayilari gruplamak icin olusturdum
    for i in harf_number:
        t=len(i)
        var=[]
        for j in range(0,t,2):
            toplam=i[j]+i[j+1]
            var.append(toplam)
        sayilar_var.append(var)#sayilari ayirdim....
    harf=[]# isimleri atmak icin yaptım

    for k in sayilar_var:
        isim=''
        for l in range(len(k)):
            if l==0:
              isim=isim+capital[k[l]]
            else:
                isim=isim+low_letter[k[l]]
        harf.append(isim)

    return (harf)#sayilari isim yaptim


def binary_searc(find, loow, hiigh, target):
        isim_sirali = harf_yap(find)
        print('')
        yazdirilacak_dosya.write('\n')
        for i in range(loow,hiigh,1):
            print (isim_sirali[i], end=' ')
            yazdirilacak_dosya.write(isim_sirali[i]+' ')
            kontrol=isim_sirali[i]
        if ((loow+hiigh) % 2 == 0):
            ortalama = ((loow+hiigh) // 2) - 1
        else:
            ortalama = ((loow+hiigh) // 2)

        if (find[ortalama] == target[0]):
            print ('')
            yazdirilacak_dosya.write('\n')
            if(kontrol==isim_sirali[ortalama]):
                return 1
            else:
                print (isim_sirali[ortalama])
                yazdirilacak_dosya.write(isim_sirali[ortalama])
                return 1
        elif(hiigh==loow):
            return -1

        elif (find[ortalama] > target[0]):
            hiigh=ortalama
            return binary_searc(find, loow, hiigh, target)

        else:
            loow=ortalama+1
            hiigh=hiigh
            return binary_searc(find, loow, hiigh, target)



data=[]#tum bilgi bunun icinde
data_isim=[]#isimler bunun içince
yazdirilacak_dosya=open('output.txt','w')
data_file=open(sys.argv[1],'r')
for i in data_file.read().split('\n'):
   t=i.split(':')
   data_isim.append(t[0])
   data.append(t)


sayilar=sayi_yap(data_isim) #isimleri sayi yaptim
order_list = bubble_sort(sayilar)  # sayilari sırala
isimler=harf_yap(order_list)    # sayilari isim yap

name_list=[]
name=(sys.argv[2])
name_list.append(name)
number_isim=sayi_yap(name_list)#Girilen ismi sayiya cevirdim...
low_value=0
high_value=len(order_list)
print ("Searching value is :%s\n"%(name))# aranan ismi yazdirdi
yazdirilacak_dosya.write("Searching value is :%s\n\n"%(name))
for i in range(len(data_isim)):  # isimleri sırasiz yazdirdi...
    print (data_isim[i], end=' ')
    yazdirilacak_dosya.write(data_isim[i]+' ')
find=binary_searc(order_list,low_value,high_value,number_isim)

if(find==-1):
    print ("")
    print ("The search string was not found in file")
    yazdirilacak_dosya.write("\nThe search string was not found in file")
else:
    for i in data:
        if(i[0]==name):
            print ("The search string is  %s"%(name)," and the city is %s"%(i[1]))
            yazdirilacak_dosya.write("\nThe search string is  %s"%(name))
            yazdirilacak_dosya.write(" and the city is %s"%(i[1]))