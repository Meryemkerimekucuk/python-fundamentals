################
#GÖREV1
################
from functions_conditions_loops_comprehensions import index

x= 8
type(x)

y= 3.2
type(y)

z= 8j+18
type(z)

a= "Hello World"
type(a)

b= True
type(b)

c= 23<22
type(c)

l= [1,2,3,4]
type(l)

d= ("Machine Learning", "Data Science")
type(d)

s= {"Python", "Java", "C++", "PHP"}
type(s)

################
#GÖREV2
################

text= "The goal is to turn data into information into insight"
a= text.upper()
a.replace(" ", ",")


################
#GÖREV3
################

lst= ["D","A","T","A","S","C","I","E","N","C","E"]
len(lst)

lst[0]
lst[10]

lst[0:4]

lst.pop(8)
lst

lst[8]= "N"
lst

lst.append("C")
lst




################
#GÖREV4
################

dict= { 'Christian': ["America",18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain",22],
        'Dante': ["Italy",25]

}

dict.keys()
dict.values()

dict["Daisy"][1]= 13
dict

dict["Ahmet"]= ["Turkey",24]
dict

dict.pop("Antonio")
dict



##################
#GÖREV5
##################

#Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız
l= [2,13,18,93,22]

def liste(l):
    a = []
    b = []
    for liste in l:
          if liste%2==0:
              a.append(liste)
          else:
             b.append(liste)

    return a,b
cift,tek= liste(l)
print(tek)
print(cift)



##################
#GÖREV6
##################

ogrenciler= ["Ali", "Veli","Ayşe","Talat","Zeynep"]

for sıra,öğrenci in enumerate(ogrenciler[:3],1):
    print(f"Mühendislik Fakültesi {sıra}. öğrenci: {öğrenci}")

for sıra, öğrenci in enumerate(ogrenciler[3:],1):
    print(f"Tıp Fakültesi {sıra}. öğrenci: {öğrenci}")




##################
#GÖREV7
##################

ders_kodu= ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi= [3,4,2,4]
kontenjan= [30,75,150,25]

for ders, kredi, kontenjan in zip(ders_kodu,kredi,kontenjan):
    print(f"Kredisi {kredi} olan {ders} kodlu dersin kontenjanı {kontenjan}")


#################
#GÖREV8
################

kume1= set(["data", "python"])
kume2= set(["data", "function", "qcut","lambda","python","miuul"])

def küme():
    if kume1.issuperset(kume2):
        print(kume2.intersection(kume1))
    else:
        print(kume2.difference(kume1))

küme()







# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################

list1= [
    'num_total',
    'num_speeding',
    'num_alcohol',
    'num_not_distracted',
    'num_no_previous',
    'num_ins_premium',
    'num_ins_losses',
    'abbrev'
]

["NUM_"+ liste1.upper() for liste1 in list1]



# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################

list1= [
    'num_total',
    'num_speeding',
    'num_alcohol',
    'num_not_distracted',
    'num_no_previous',
    'num_ins_premium',
    'num_ins_losses',
    'abbrev'
]


[ liste + "_FLAG" for liste in list1 if "no" not in liste]










# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.
#
# # Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']



# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################

og_list = ["abbrev", "no_previous"]

# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.
#
# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630
#




