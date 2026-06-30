
###############
# Tip değiştirme
###############

a= 534
print(type(a))
print(a)

print(type(a))

print(int(a))

#####################################
# Karakter dizinlerinde slice işlemi
#####################################
name = "Meryem"
name="Hi! i am learning python."
print(name[0])
print(name[0:2])
print(name[::])
print(name[:-1])
print(name[::-1])
print("Mer" in name)

###################
# String metodları
###################

dir(str)  # str metotlarını listelemek için kullanılır. int de kullanılabilir dir(int)
name="Hi! i am learning python."
len(name) #stringin uzunluğunu öğrenmek için kullanılır.

name="Hi! i am learning python."
len(name)
name.startswith("ar")
name.endswith("N")


name.split()


name.replace("python","java")
name.split()
name.capitalize()

name.upper() # bütün harfleri büyük yazmak için kullanılır
name.lower()
name.replace("m","M") # var olan bir değeri başka bir değer ile değişitirmek için kullanılır

text= "hello AI Era"
text.split() # listelere ayırmak için kullanılır

text.capitalize() # başlangıç harflerini büyük yazmak için kullanılır
name.replace("python","java")
text.startswith("ar") # verilen değer ile başlıyor mu diye kontrol etmek için kullanılır

######################
# Liste (List)
# Değiştirilebilir
# Sıralıdır
# Kapsayıcıdır
######################

notes = [99,100,45,67]
names = ["Meryem","Aslı","Zeynep"]
mix = [345,67,32,"Murat","Can", ["Math","Biology", "Scientist"]]

mix[4]
mix[3] = "Mert"
mix


###################
# Liste Metotları
###################

len(notes)

notes.append(56) # listenin içerisine eleman eklemek için kullanılır

mix.pop(0) # Belirlenen indeksteki değeri kaldırmak için kullanılır

notes.insert(0,90) #Belirlenen indeksteki değerin yerine verilen değeri eklemek için kullanılır
notes


#########################################
# Sözlükler (Dictionary)
# Değiştirilebilir.
# Sırasızdır. (3.7 v sonra sıralıdır)
# Kapsayıcı
##########################################

dictionary = {"REG": "Regression", "LOG": "Logistic Regression", "CART": "Classification and Regression"}
dictionary["REG"]

exam_notes = {"Math": ["Vize",45, "Final", 100], "Biology": ["Vize", 100, "Final", 100]}
exam_notes["Math"]

exam_notes.get("Math")

dictionary["LOG"] = "Logistic"
dictionary

dictionary.keys() # keyleri göstermek için kullanılır
dictionary.values() # valueları göstermek için kullanılır
dictionary.items() # Tüm çiftleri tuple halinde listeye çevirir.

exam_notes.update({"Biology":34})  # Verilen keydeki value değerini değiştirmek için kullanılır
exam_notes

######################
# Demet (Tuple)
# Değiştirilemez
# Sıralıdır
# Kapsayıcıdır
# Kullanımı çok azdır
######################

demet = (1,3,6,8,"Belgin")
type(demet)
demet[4]


######################
# Set
# Değiştirilebilir
# Sırasız + Eşsizdir
# Kapsayıcıdır
######################

set1 = set([1,2,3,4,5,7,9])
set2 = set([0,1,2,4,6,8])

set1.difference(set2) # set1 seti arasında set2 de olmayan değerleri listeler

set2.difference(set1) # set2 seti arasında set2 de olmayan değerleri listeler

set1.symmetric_difference(set2) # 2 set arasında 1 kere kullanılan değerleri listeler yani set1 ve set2 de aynı değer var


set1.intersection(set2) # 2 set arasında ortak olan değerleri listeler
set2.intersection(set1) # 2 set arasında ortak olan değerleri listeler

set1 & set2

set1.union(set2) # 2set arasındaki bütün değerleri listeler

set1.isdisjoint(set2) # 2 kümenin kesişimi boş mu

set2.issubset(set1)   # set1 set2 in alt kümesi mi


numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = {x for x in numbers}
print(unique_numbers)