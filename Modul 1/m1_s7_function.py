###+=================
# local variable
#variable yang hanya berlaku di dalam sebuah function
#variable tsb hangus ketika function selesai dijalankan

#Global variabel
#variabel yang didefinisikan di luar function
#cakupanya global , berarti variabel ini memegang nilai sepanjang program dijalan
#berlaku di luar atau di dalam function apapun


# x = 100

# def tambah(angkaA , angkaB):
#     hasil = angkaA + angkaB ## --> variabel hasil atau local variable
#     return(hasil)

# # print(hasil(10,3))
# print(x)
# # print(hasil)

# def kali (angkaC , angkaD):
#     perkalian = angkaC * angkaD * x
#     return perkalian

# print(kali(2,4))


##=======================
# PRIORITAS LOCAL VARIABLE DARIPADA GLOBAL VARIABLE
# def coba():
#     x = 100
#     print(x + 2)
#     return x + 3

# x = 5
# print(coba())  #103 --> Menggunakan local variabel
# print(x) #---> menggunakan global variabel


###----------------

# def coba () :     ##EROR
#     x = x + 100
#     print(x+2)
#     return x + 3

# x=5
# print(coba())

##=======
#SOLUSI 1 --> memasukan local variabel ke dalm function

# def coba () :     
#     x = x + 100
#     print(x+2)
#     return x + 3

# x=5
# print(coba())   #108
# print(x)        #5

# #======================
# #SOLUSI 2 --> menggunakan keyword global

# def coba () :
#     global x   
#     x = x + 100
#     print(x+2)
#     return x + 3

# x=5
# print(coba())  #108
# print(x)        #105 --> nilai berubah di dalam function

#-------------------------
#CALL BACK FUNCTION

# def tambah(angkaA , angkaB):
#     hasil = angkaA + angkaB
#     return hasil

# def kurang(angkaA , angkaB):
#     hasil = angkaA - angkaB
#     return hasil

# def operasi_mat(my function , numberA , numberB):
#     hasil_operasi = my_function(numberA , numberB)
#     return hasil_operasi

# print(operasi_mat(tambah ,10,3))

#=========================
#Calling other function
#function yg digunakan di dalam function lainya

# def tampilkan(jawaban):
#     print(f'jawaban adalah {jawaban}')


# def kurang(angkaA , angkaB):
#     hasil = angkaA - angkaB
#     tampilkan(hasil)

# print(kurang(10,3))


# #====
# #Recursive function
# #function yang memanggil dirinya sendiri

# # def menu():
# #     user_input = input('masukan angka 1 atau 2 :')

# #     if user_input == '1':
# #         print('masuk menu 1')
# #     elif user_input == '2':
# #         print('masuk menu 2')
# #     else:
# #         menu() #Memanggil dirinya sendiri

# # menu()


# ####================
# #Lambda Function
# #function kecil yang tidak punya nama
# #bisa punya beberapa parameter , tapi hanya punya 1 statemen/expression
# # #syntax --> lambda parameter : expression

# kuadrat = lambda angka : angka**2
# print(kuadrat(5))

# perkalian = lambda angkaA, angkaB: angkaA * angkaB
# print(perkalian(5,10))

# # ##===============
# # #MAP
# # #Digunakan untuk mengubah nilai atau bentuk
# # #dari item yang ada di collection data type

# # # list_angka = [1,2,3,4]
# # # list_baru = []

# # # for angka in list_angka:
# # #     list_angka.append(angka**2)

# # # list_angka = list_baru
# # # print(list_angka)

# # # #list comprehension
# # # print([angka**2 for angka in list_angka])


# # #================
# # #Map

# # #syntax --> (nama , function , list)
# # #outputnya dalam bentuk map object
# # #kita ubah menjadi list agar ditampilkan

# # list_angka = [1,2,3,4]

# # def kuadrat(angka):
# #     return angka**2

# # #regular function
# # print(list(map(kuadrat , list_angka)))
# # #lambda function
# # print(list(map(lambda angka : angka ** 2 , list_angka)))


# ##===================
# # # Soal 1

# # # Tarif taxi per kilometer adalah 5000
# # # Awal buka pintu sudah dikenakan tarif 8000
# # # Berapa tarif taxi untuk perjalanan sejauh 1, 2, 3, 4, dan 5 kilometer?
# # # input dan output berupa list


# #=--------------------
# # #JAWABAN
# # kilometer = [1,2,3,4,5]

# # #function
# # def harga_taxi(jarak):
# #     harga =  jarak*5000 + 8000
# #     return harga
# # #Map (regular function)
# # print(list(map(harga_taxi , kilometer)))

# # #map (lambda function)
# # print(list(map(lambda jarak : (jarak*5000+8000), kilometer)))


# ###===============
# #FILTER
# #digunakan untuk filtering (memilih) item collection data type
# #jumlah item akan berkurang
# #nilai item tidak berubah
# #yang ditampilkan adalah nilai yg kondisinya true

# # syntax --> filter(function , list)


# kilometer = [1,2,3,4,5]

# def genap(angka):
#     if angka%2 == 0:
#         return True
#     else:
#         return False

# print(genap(4))

# print(list(filter(genap , kilometer)))

# #variebel kilometer jumlah itemnya tetap sama
# print(kilometer)

# #menyimpan hasil filtering pada sebuah variabel
# #setelah filter ,jumlah itemnya tinggal 2
# hasil_filter_genap = list(filter(genap,kilometer))
# print(hasil_filter_genap)


#==================
#Soal KTP
#JAWABAN

# list_angka = [1,3,4,5]




# def a(angka):
#     if angka %2 == 0:
#         return'genap'
#     else:
#         return'ganjil'
    

# #regular function
# hasil = list(map(a , list_angka))
# print(hasil)

x = 50/10
print(type(x))





