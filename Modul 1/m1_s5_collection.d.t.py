#COLLECTION DATA TYPE

# #------------------------------------------------
# #LIST CIRI:
# #Ditandai demgam [] ,,,,, dapat menampung item dari berbagai macam tipe data ( str , int , bool , dll)
# #dapat menampung nilai yang sama atau duplikat
# # mutable/item dalam list bisa diubah/diganti
# #berurutan , jadi bisa di indexing

# ####----------------------------
# #dapat menampung item dari berbagai macam tipe data

# list_contoh=['hello' ,1,2, True]
# print(list_contoh)

# #list dalam list
# list_dalam_list=['hello',1,2,3,True,[10,20,30]]
# print(list_dalam_list)

# #dapat menampung nilai yang sama
# list_contoh=['hello' ,1,2, True ,6,6,6]
# print(list_contoh)

#cara mengubah data di dalam list
# list_contoh=['hello' ,1,2, True ,6,6,6]
# list_contoh[3] = False
# print(list_contoh[4])
# print(list_contoh)


# ##--------- BERURUTAN , JADI BISA DIINDEXING
# list_dalam_list=['hello',1,2,3,True,[10,20,30]]
# print(list_dalam_list[3])    #3
# print(list_dalam_list[1:4])     # 1,2,3
# print(list_dalam_list[-1])         #10,20,30
# print(list_dalam_list[-1][1])         #20

# list_inner = list_dalam_list[-1]
# print(list_inner[1])           #20

# print(list_dalam_list[ : :-1])   ##CARA BEERJLAN MUNDUR DI DALAM LIST

# print(list_dalam_list[-1][-1: :-1])  #[30,20,10]


#cek item dalam list
# list_dalam_list=['hello',1,2,3,True,[10,20,30]]
# print(3 in list_dalam_list)    #Hasil bool , TRUE karena ada angka 3
# print(10 in list_dalam_list)  #FALSE
# print([10,20,30] in list_dalam_list)   # true

# if 3 in list_dalam_list:
#     print('ada')

# else:
# #     print('tidak ada')

# list_dalam_list=['hello',1,2,3,True,[10,20,30]]
# print(len(list_dalam_list))


###_-----------------------####

# list_dalam_list=['hello',1,2,3,True,[10,20,30]]
# print(list_dalam_list)

# list_baru=list_dalam_list.copy()     ##Gunakan .copy agar list di awalk tdk terubah
# print(list_baru)

# list_baru[0] = 'bye'
# print(list_baru)
# print(list_dalam_list)

###---------------------------
#List concatenating
# list_angka = [1,2,3,4,5]
# list_huruf = ['a','b','c','d']

# list_concat= list_angka + list_huruf    #Gabungin list
# print(list_concat)    #[1, 2, 3, 4, 5, 'a', 'b', 'c', 'd']


###----------------
#### Mencari index item pada sebuah list

# list_dalam_list=['hello',1,2,3,True,[10,20,30]]
# print(list_dalam_list.index('hello'))

# ###---------------------
# #mengurutkan item dalam list (sorting)/// DIurutkan berdasarkan alphabet

# mobil = ['toyota','bmw','mercedes','hyundai','bentley']
# print(mobil)

# mobil.sort() #tidak perlu disimpan dalam variabel , .sort digunakan untuk mengurutkan
# print(mobil)

#LIST 2 dimensi

# kendaraan = [
#     ['mobil','ferari',1],
#     ['motor','ducati',3]
# ]

# print(kendaraan)
# print(kendaraan[0][1])       #ferari

##LIST 3 dimensi

# list_bilangan = [[[1,2,3],
#                     [100,200,300],

#                     [[4,5,6],
#                     [400,500,600]]
#                     ]]


# print(list_bilangan)
# print(list_bilangan[0][1][2])   #300
# print(len(list_bilangan[0][1]))   #3

##method/function .append() ---> untuk menambahkan 1 item di index terakhir

# mobil_lama= ['toyota' , 'bmw', 'mercedez','hyundai','bentley']
# mobil_baru = [ 'vw','ferarri']

# mobil_lama.append(mobil_baru)       #['toyota', 'bmw', 'mercedez', 'hyundai', 'bentley', ['vw', 'ferarri']]
# print(mobil_lama)
# print(len(mobil_lama))

## MENYELIPKAN SEBUAH ITEM DALAM LIST // .INSERT
# mobil_lama= ['toyota' , 'bmw', 'mercedez','hyundai','bentley']
# mobil_baru = [ 'vw','ferarri']

# mobil_lama.insert(2,mobil_baru)      #2 itu adalah index
# print(len(mobil_lama))
# print(mobil_lama)

#### MENGHAPUS ITEM PADA LIST // .REMOVE

# mobil_lama= ['toyota' , 'bmw', 'mercedez','hyundai','bentley']
# print(mobil_lama)

# mobil_lama.remove('mercedez')
# print(mobil_lama)

### MENGHAPUS ITEM TERAKHIR ,/// .POP
# mobil_lama= ['toyota' , 'bmw', 'mercedez','hyundai','bentley']
# mobil_lama.pop()
# print(mobil_lama)

#MENGHAPUS BISA MENGGUNAKAN DEL JUGA
# del mobil_lama[0]
# print(mobil_lama)

## CLEAR UNTUK MENGHAPUS SELURUH INDEX

# mobil_lama.clear()
# print(mobil_lama)


#SOAL --> BUAT LIST BERISI ANGKA GENAP PADA RENTANG 1-30
# list_angka_genap =  []

# for angka in range (2,31,2):
#     list_angka_genap.append(angka)

# print(list_angka_genap)
c
#SOAL : BUAT LIST BERISI [1,10,100,1000,10000]
# list_10pangkat = []
# for i in range(0,5):
#     list_10pangkat.append(10**i)
# print(list_10pangkat)


###LIST COMPREHENSION
#membuat sebuah list yang basis logikanya berasal dari loop
#SOAL --> BUAT LIST BERISI ANGKA GENAP PADA RENTANG 1-30

# list_genap = [ angka for angka in range (2,31,2)]
# print(list_genap)

#SOAL : BUAT LIST BERISI [1,10,100,1000,10000]
# list = [10**angka for angka in range (0,5)]
# print(list)

# #SOAL BUAT LIST BERISI [1,4,9,16,25,36]
# list_kuadrat = []

# for angka in range (1,7):
#     list_kuadrat.append(angka**2)

# print(list_kuadrat)

# list_kuadrat2 = [angka **2 for angka in range (1,7)]
# print(list_kuadrat2)


######-------------------
###Tuple

## DItandai dengan ()
#mirip dengan list , dapat menyimpan item dengan berbagai macam data type
#berurutan , bisa diindexing dan duplikat
#innutable , item dalam tuple tidak bisa diganti

# # tuple_contoh = ('hello',1,2,3,True,10,10,10)
# # print(tuple_contoh)

# # #indexing dengan urutan
# # print(tuple_contoh[5])

# #EROR !!!! TIDAK BS MENGUBAH DARI ITEM DIDALAM TUPLE
# # tuple_contoh[5]=333
# # print(tuple_contoh)

# #mengubah tuple menjadi list
# # list_asalnya_tuple = list(tuple_contoh)
# # print(list_asalnya_tuple)

# # list_asalnya_tuple[-3]=333

# # tuple_final=tuple(list_asalnya_tuple)
# # print(tuple_final)

# ###+==============================================
# list_angka = [45]
# print(list_angka)
# print(type(list_angka))


# list_angka = (45)    #INTERGER
# print(list_angka)
# print(type(list_angka))

# tuple_angka =(45,) #wajib pakai KOMA !!   TUPLE
# print(tuple_angka)
# print(type(tuple_angka))


##-------------------------
# CARA CEK ITEM DALAM TUPLE SAMA DENGAN DI LIST
#CARA CONCATE PADA TUPLE SAMA DENGAN DI LIST
#TUPLE 2 DIMENSI MIRIP DENGAN LIST 2 DIMENSI



#========================================
#DICTIONARY
#KONTAINER YANG BISA MENAMPUNG BANYAK VALUE DENGAN BERAGAM TIPE DATA
#ITEM PADA SEBUAH DICTIONARY TERDIRI DARI {KEY:VALUE}
# INDEXING MENGGUNAKAN KEY , BYUKAN PAKAI URUTAN/ANGKA
#KEY adalah KATA KUNCI , TIDAK BOLEH DUPLIKAT
#Biasanaya dictionary digunakan ketika suatu data memilik pola
#atau tipe data yang sama dan berhubungan satu dengan lainya

# Dict_contoh = {'nama': 'John' , 'Umur':30, 'domisili': 'batam' , 'bekerja' : True
# }
# print(Dict_contoh)

# #Indexing dengan key
# print(Dict_contoh['Umur'])       ##30

#kalau ada key yang duplikat , maka hanya ditampilkan terakhir

# Dict_contoh = {'nama': 'John' , 'Umur':30, 'domisili': 'sgp' ,'domisili': 'batam' , 'bekerja' : True
# }
# print(Dict_contoh)

# #CARA MENGUBAH VALUE NYA

# Dict_contoh = {'nama': 'John' , 'Umur':30, 'domisili': 'sgp' ,'domisili': 'batam' , 'bekerja' : True
# }
# Dict_contoh['Umur'] = 25      #25
# print(Dict_contoh)

# ##===========================
# #Membuat dictionary menggunakan function dict

# dict_karyawan = dict(nama= 'brian' , Umur=26 ,domisili= 'batam' , bekerja = True
# )
# print(dict_karyawan)

#CARA MENGHAPUS VALUE DI DICTIONARY
# Dict_contoh = {'nama': 'John' , 'Umur':30, 'domisili': 'sgp' ,'domisili': 'batam' , 'bekerja' : True
# }
# del Dict_contoh['domisili']
# print(Dict_contoh)

# Dict_contoh.pop('Umur')   #Menghapus item terakhir
# # print(Dict_contoh)

# # #Menghapus semua item

# # Dict_contoh.clear()
# # print(Dict_contoh)

# ##+++++++++++++++++=====================================
# #Looping pada dictionary

# Dict_contoh = {'nama': 'John' , 'Umur':30, 'domisili': 'sgp' ,'domisili': 'batam' , 'bekerja' : True
# }

# # #yang di looping key aja
# # for i in Dict_contoh:
# #     print(i)

# # for i in Dict_contoh.keys():
# #     print(i)

# #YANG DI LOOPING VALUE AJA
# for i in Dict_contoh.values():
#     print(i)


#     #yang dilooping key dan value nya(output dalam tuple)
# for i in Dict_contoh.items():
#     print(i)

#     ###============================
#     #Nested Dictionary (dictionary di dalam dictionary)

#     Menu = {'appetizer':{'nama' : 'siomay', ' harga' : 30},
#             'main_course':{'nama':'nasgor', 'harga' : 50},
#             'desert' :{'nama':'puding', 'harga': 10}}

#     print(Menu)
#     print(Menu['desert']['harga'])   #10
#     print(Menu['main_course']['nama'])  #nasgor


#     #==================================
#     #set

#     #Ditandai dengan {}
#     #Dapat menyimpan item dari berbagai macam tipe data
#     #tidak bisa duplikat , semua item unique
#     #tidak punya urutan , tidak bisa diindexing
#     #biasa digunakan untuk membuang duplikat

#     set_contoh = {1,2,3,4,5,5,4,3}
#     print(set_contoh) ## TIDAK BISA DUPLIKAT

#     # print(set_contoh[0])   #Tidak bisa indexing

#     set_coba = {5,2,10,3,7,4,100,55}  ##TIDAK BERUURUTAN TETAPI BISA DILOOPING
#     for angka in set_coba:
#         print(angka)

#         #================================
#         #menambahkan item ke dalam set

#     set_coba = {5,2,10,3,7,4,100,33}
#     print(set_coba)

#     set_coba.add(11)
#     print(set_coba)

#     set_coba.add(5)   #TIDAK MASUK ANGKA 5 karena sudah ada angka 5 dlluan
#     print(set_coba)

#     set_coba.update({999,323})
#     print(set_coba)




#     ###MENGHAPUS ITEM DALAM SET
# set_coba = {5,2,10,3,7,4,100,33}
# print(set_coba)

# set_coba.discard(33)
# print(set_coba)

# set_coba.remove(100)
# print(set_coba)

# set_coba.pop()  #HAPUS ITEM SECARA ACAK
# print(set_coba)


# set_coba.clear()
# print(set_coba)

# #-------------------------------------------
# #union,diffrence , symetric diffrence , intersection

# ganjil = {1,3,5,7,9}
# prima = {2,3,5,7,11}

# #menggabungkan 2 set tanpa duplikat ( full outer join)
# print(ganjil.union(prima))
# # Item di ganjil yang tidak ada di prima
# print(ganjil.difference(prima))
# #Item di prima yang tidak ada di ganjil
# print(prima.difference(ganjil))

# #yang hanya dimiliki prima dan hanya dimiliki ganjil
# print(ganjil.symmetric_difference(prima))

# #yg ada di kedua set atau irisan
# print(ganjil.intersection(prima))


###-----------------
#Cek subset , superset , disjoint

ganjil = {1,3,5,7,9}
angka = {3,5}
genap = {2,4,6}

#APAKAH ANGKA BAGIAN DARI GANJIL?  ---> TRUE
print(angka.issubset(ganjil))

#Apakah angka superset dari ganjil ---> FAlSE
print(angka.issuperset(ganjil))

#Apakah ganjil superset dari angka --> true
print(ganjil.issuperset(angka))

#apakah kedua set itemnya tidak ada yg sama
print(ganjil.isdisjoint(angka))   #---> FALSE KARENA 3 , 5 ada di kedua set

print(ganjil.isdisjoint(genap)) ##--> True karena tidak ada yg item yg sama


###----------------------------------
#ZIP

angka = [1,2,3,4]
huruf = ['a','b','c','d']

print(list(zip(angka,huruf)))  ##HARS LIST ATAU TUPLE BARU HASILNYA KLUAR



############

list_angka = [10,20]
b,a = a,b
print(a)
