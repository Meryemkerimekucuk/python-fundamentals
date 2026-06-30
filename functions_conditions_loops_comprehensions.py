##########################
# Fonksiyon Okuryazarlığı
##########################

print("a","b",sep="**")

######################
#Fonksiyon Tanımlama
######################

def calculate(a):
    print(a**2)

calculate(46)


def summer(x,y,z):

    #DOCSTRING
    """
    Summer of the args...
    Args:
        x:
        y:
        z:

    Returns:

    """
    print(x+y+z)



summer(63,89,36)
summer(x=24,y=632,z=345)

######################################
# Fonksiyonların Statment/Body Bölümü
######################################

def persona(name):
    print(name)
    print("Yaş: 22" )
    print("Meslek: Doktor")

persona("Sıla")

def restoran_mutfagi(siparis_adi, adet):
    # --- BURASI FONKSİYONUN MUTFAĞIDIR (GÖVDE KISMI) ---
    # Malzemeler hazırlanıyor, işlemler yapılıyor...
    hazirlik_notu = f"{adet} adet {siparis_adi} için malzemeler dolaptan çıkarıldı."
    pisirme_durumu = f"{siparis_adi} yüksek ateşte pişirildi."

    # Tabaklama ve sunum hazırlanıyor
    hazir_tabak = f"Sıcak sıcak servis edilen: {hazirlik_notu} ve {pisirme_durumu}"

    return hazir_tabak  # Yemek salona çıkıyor!
    # --------------------------------------------------


# Mutfak dışarıdan çağrılıyor (Sipariş veriliyor)
gelen_servis = restoran_mutfagi("Pizza", 2)

# Sonuç ekrana yazdırılıyor
print(gelen_servis)








summer_list= []
def summer(a, b):
    c = a+b
    summer_list.append(c)
    print(summer_list)

summer(5,9)
summer(14565432,876543456)


######################################
# Ön Tanımlı Argümanlar, Parametreler
######################################

def persona_info(name= "Meryem"):
    print(name)
    print("Yaş: 21.5")
    print("Meslek: Jr. Data Scientist")

persona_info()

def us_alma(us):
    # Dış fonksiyon, taban değerini alacak olan iç fonksiyonu hazırlar
    def hesapla(taban):
        return taban**us

    # İç fonksiyonu çalıştırmadan, bir nesne olarak geri döndürüyoruz
    return hesapla


# 1. Adım: Fabrikayı kullanarak özel fonksiyonlar üretiyoruz
kare_al = us_alma(2)  # us = 2 olarak hafızaya alındı
kup_al = us_alma(3)  # us = 3 olarak hafızaya alındı

# 2. Adım: Ürettiğimiz bu yeni fonksiyonları kullanıyoruz
print("5'in karesi:", kare_al(5))  # Çıktı: 25
print("4'ün küpü:", kup_al(4))  # Çıktı: 64
















#################################################################
# Return: Fonksiyonların girdilerini çıktı olarak kullanabilmek
#################################################################

def calculate(warm,moisture, charge):
    return (warm+moisture)/charge

calculate(754,356,74)
calculate(754,356,74)*34    #Return kullanılmadığı takdirde bu işlem yapılmaz



def hesapla(üs, çıkar, çarp):
    üs= üs*üs
    çıkar= üs-454
    çarp= çıkar*5432
    return üs,çıkar,çarp
üs,çıkar,çarp=hesapla(53,532,532)



def all_calculation(varm,moisture, charge):
    a = calculate(varm,moisture,charge)
    b= hesapla(üs,çıkar,çarp)
    print(b*45)

all_calculation(45,74,245)


################################
# Lokal ve Global Değişkenler
################################

liste= [4,6] #global değişken
def add_element(a, b):
    c= a+b #lokal değişken
    liste.append(c)
    print(liste)

add_element(6,2)




#############
# if Koşulu
#############

def number_check(num):
    if num==78:
        print("Number is correct")

number_check(78)
number_check(18)


##############
# else koşulu
##############

def number_check(num):
    if num==78:
        print("Number is correct")
    else:
        print("Number is not correct")
number_check(78)
number_check(355)


##############
# elif koşulu
##############

def ehliyet_kayit(yas):
    if yas<18:
        print("Kayıt yaptıramazsınız")
    elif yas==18 or yas>18:
        print("Kayıt yaptırabilirsiniz")
    else:
        print("Lütfen yaşınızı giriniz")

ehliyet_kayit(2)
ehliyet_kayit(34)


##############
# for döngüsü
##############

student_name=["Venessa","Maria","Josh","Srina","Ashley"]
for student in student_name:
    print(student)


employee_salary={"Serpil ":35000, "Canan ":50000, "Ahmet ":28000, "Can ":120000, "Akın ": 348550}
for employee, salary in employee_salary.items():
    print(f"Çalışan: {employee} - Maaş: {salary}")

salary= [3500,3300,10000,1340]
for salary in salary:
    print(salary)
    new_salary= int((salary*50/100)+salary)
    print(salary,new_salary)

salary= [3500,3300,10000,1340]
def salary_rate(salary,rate):
    return int((salary*rate/100)) + salary

for salary in salary:
    print(salary_rate(salary, 50))



########################################################
# Uygulama Mülakat Sorusu
# Before: hi my name is john and i am learning python
# After: Hi mY nAmE iS JoHn aNd i aM LeArNiNg pYtHoN
########################################################

def alternating(string):
    new_string=""
    for string_index in range(len(string)):
        if string_index%2==0:
            new_string+= string[string_index].upper()
        else:
            new_string+= string[string_index].lower()
    print(new_string)

alternating("hi my name is john and i am learning python")



##########
#Break
##########

notes=[45,97,100,62,57,75]
for note in notes:
    if note > 69:
        break # 69'dan büyük bir sayı gördüğünde döngüyü bitir
    print(note)
        
############
#Continue
############

for note in notes:
    if note == 100:
        continue # 100 ü gördüğünde atla ve döngüye devam et
    print(note)

########
#While
########

number=3
while number<10:   #Sayı 10dan küçük olduğu sürece
    print(number)
    number+=1


############
#Enumurate
############

student=["Josh","Steven","Sara","Lydia"]

for index,student in enumerate(student):
    print(index,student)



A=[]
B=[]
students=["Josh","Steven","Sara","Lydia"]

for index,student in enumerate(students):
    if index%2==0:
        A.append(student)
    else:
        B.append(student)

print("A Listesi (Çift İndeksler):", A)
print("B Listesi (Tek İndeksler):", B)


#################################################################
#Mülakat Sorusu - Uygulama
# divide_students fonksiyonu yazınız
# Çift indekste yer alan öğrencileri bir listeye alınız.
# Tek indekste yer alan öğrencileri bir başka listeye alınız
# Fakat bu 2 liste tek bir liste olarak return olsun
###################################################################

students=["Josh","Steven","Sara","Lydia","John","Nicole"]

def divide_students(students):
    groups = [[],[]]
    for index,student in enumerate(students):
        if index%2==0:
            groups[0].append(student)
        else:
            groups[1].append(student)

    print(groups)
    return groups
divide_students(students)






######################################################
# alternating fonksiyonunun enumerate ile kullanımı
######################################################

def alternating_with_enumerate(string):
    new_string=""
    for i, letter in enumerate(string):
        if i%2==0:
            new_string+=letter.upper()
        else:
            new_string+=letter.lower()
    print(new_string)

alternating_with_enumerate("hi my name is meryem i am learning python with miuul")




#######
#ZİP
#######

student_name= ["Aslı","Meryem","Can","Serap","Ahmet","Eray","Zehra"]
notes= [24,56,100,45,68,34,49]
lessons= ["Matematik","Edebiyat","Türkçe","İngilizce","Felsefe","Almanca","Beden Eğitimi"]

list(zip(student_name,notes,lessons))



#################################################
#lambda, map, filter, reduce
#lambda 'kullan at, tek seferlik kullanım gibi'
##################################################

new_sum = lambda a,b: a+b
new_sum(53,35)

#################################
#map 'döngü yazmaktan kurtarır'
##################################

salary = [1000,2000,3000,4000,5000,6000]
def new_salary(salary):
    return (salary*20/100)+salary
new_salary(5000)

list(map(new_salary,salary))


#del new_salary


salary = [1000,2000,3000,4000,5000,6000]
list(map(lambda x: x*20/100+x,salary))


##########
#FILTER
##########

list_store= [1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x: x%2==0,list_store))

##############################
#REDUCE 'indirgemek demektir'
##############################

from functools import reduce
list_store= [1,2,3,4,5,6,7,8,9,10]
reduce(lambda a,b: a+b,list_store)





################
#COMPREHENSIONS
################

"""
Python'da Comprehensions (Kavramlar/Anlayışlar), listeler, sözlükler veya kümeler (set) gibi veri yapılarını daha kısa, tek satırda ve daha okunabilir bir şekilde oluşturmanızı sağlayan harika bir sözdizimi (syntax) özelliğidir.

"""
#####################
#List Comprehension
######################


salary = [1000,2000,3000,4000,5000,6000]
[salary*2 for salary in salary]


[salary*2 for salary in salary if salary < 3000] # Comprehensions yapılarında eğer tek bir if yapısı kullanılıyorsa yani else kullanılmıyor kod bloğunun sağına yazılır.

[salary * 2 if salary <3000 else new_salary(salary) for salary in salary] #Comprehensions yapılarında eğer if ve else var ise for döngüsü sağa yazılır


dictionary={"a":1, "b":2, "c":3, "d":4}

{k: v**3 for (k,v) in dictionary.items()}

{k.upper(): v for (k,v) in dictionary.items()}



öğrenciler= ["Aslı", "Zeynep", "Meryem", "Mert", "Can", "Murat"]
öğrenci_no= ["Serap", "Esma","Aylin","Batuhan"]

[ öğrenci.lower() if öğrenciler in öğrenci_no else öğrenci.lower() for öğrenci in öğrenciler]





######################
#Dict Comprehensions
#######################

dictionary={"a":1, "b":2, "c":3, "d":4}

{k: v**3 for (k,v) in dictionary.items()}

{k.upper(): v for (k,v) in dictionary.items()}



#####################################################################
#Uygulama- mülakat sorusu
# Çift sayıların karesi alınarak bir sözlüğe eklemek istenmektedir
#####################################################################
numbers= range(1,10)
new_dict={}


{n: n**2 for n in numbers if n%2==0}


################################################################################################################
#Uygulama1
# Bir veri setindeki değişkenlerin isimlerini değiştirmek
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']
################################################################################################################

değişkenler= ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

[değişken.upper() for değişken in değişkenler]


####################################################################################
#Uygulama2
#######################
# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.
#######################
#####################################################################################

[ "FLAG_" +değişken if "INS" in değişken else "NO_FLAG" + değişken for değişken in değişkenler ]













