# EXERCISE: COLLECTION DATA TYPES

# ====================================================================
# No.1 

# Temukan angka minimum dan maksimum pada list berikut:
# list_angka = [31, 5, 1, 7, 88, 42]
# Output:
# Angka minimum = 1
# Angka maksimum = 88
##JAWABAN


# list_angka = [31, 5, 1, 7, 88, 42]
# list_baru = []

# for i in range(len(list_angka)):

#     minimum=list_angka[0]
#     for angka in list_angka:

#         if angka< minimum:
#             minimum=angka


# list_baru.append(minimum)


# list_angka.remove(minimum)

# print(list_baru)
###NO 1 BELUM SIAP !!!


    




# ====================================================================
# No.2

# Urutkan angka pada list berikut dari yang terkecil hingga terbesar tanpa menggunakan method sort!
# list_angka = [31, 5, 1, 7, 88, 42, 202, 29]
# Output:
# list_angka_sorted = [1, 5, 7, 29, 31, 42, 88, 202]

##JAWABAN
list_angka = [31, 5, 1, 7, 88, 42, 202, 29]
new_list = []

# while list_angka:
#     angkaMin = list_angka[0]  
#     for angka in list_angka: 
#         if angka < angkaMin:
#             angkaMin = angka
#     new_list.append(angkaMin)
#     list_angka.remove(angkaMin)    

# print (new_list)

#JAWBAAN TIPE 2 NO 2

# list_angka = [31, 5, 1, 7, 88, 42, 202, 29]
# # Output:
# # list_angka_sorted = [1, 5, 7, 29, 31, 42, 88, 202]

# new_list = []
# while list_angka:                   # while loop pada list akan mengecek apakah ada item pada list, jika tidak maka while berhenti
#                                         #  ketika ada item pada list, maka akan bernilai True
#                                         # ketika tidak ada item pada list, maka akan bernilai False

#     angkaMin = list_angka[0]      
#     for angka in list_angka:
#         if angka < angkaMin:
#             angkaMin = angka
#     new_list.append(angkaMin)
#     list_angka.remove(angkaMin)

# print(new_list)


# list_baru = []

# ====================================================================
# No.3

# Buat fungsi untuk mencari berapa kali tiap kata muncul dalam 1 kalimat.
# Contoh:
# kalimat = 'Aku baru makan nasi terus aku mau makan mie nanti malam'
# Output: 
# Jumlah kata 'Aku' ada sebanyak 2
# Jumlah kata 'Baru' ada sebanyak 1
# Jumlah kata 'Makan' ada sebanyak 2
# Jumlah kata 'Terus' ada sebanyak 1
# Jumlah kata 'Mau' ada sebanyak 1
# Jumlah kata 'Mie' ada sebanyak 1
# Jumlah kata 'Nanti' ada sebanyak 1
# Jumlah kata 'Malam' ada sebanyak 1
# #-----JAWABAN

# kalimat = 'Aku baru makan nasi terus aku mau makan mie nanti malam'
# kalimat_kecil = kalimat.lower()


# kalimat_split = kalimat_kecil.split()

# set_a = set(kalimat_split)
# for i in set_a:
#     print(f'Jumlah kata {i} ada sebanyak {kalimat_split.count(i)}')


# ##JAWABAN NO 3 TIPE 2


# a = kalimat.title().split()
# for i,j in enumerate(a):
#     if j == 'nasi':
#         continue
#     elif i == 5 or i == 7:
#         continue
#     else:
#         print(f'jumllah kata (j)')

        ## BELUM SIAP , JAWABAN DARI MORIS

# ====================================================================
# No.4 

# Input 5 film, dipisah koma untuk film kesukaan kamu dan kesukaan teman kamu.
# Output: Presentase kesamaan film yang kalian suka
# 'Masukkan 5 film kesukaan Anda dipisahkan dengan tanda koma: '
# 'Masukkan 5 film kesukaan teman Anda dipisahkan dengan tanda koma: '
# 'Kesukaan film kalian yang sama sebesar xx %'

# contoh:
# user1_list = ['spiderman','iron man','the avengers','ant man','thor']
# user2_list = ['spiderman','coco','doraemon','ant man','thor']

# output:
# Kesukaan film kalian yang sama sebesar 60%

#=========================
user1_list = ['spiderman','iron man','the avengers','ant man','thor']
user2_list = ['spiderman','coco','doraemon','ant man','thor']

# # output:

# # Kesukaan film kalian yang sama sebesar 60%


user1_set = set(user1_list)
user2_set = set(user2_list)

# print(user1_set)
# print(user2_set)

# # perhitungan jumlah kesamaan film
# a = len(user1_set.intersection(user2_set))

# # perhitungan jumlah kesukaan film 1 user
# b = len(user2_set)

# # presentase film kesukaan yang sama
# print(f' Kesukaan film kalian yang sama sebesar {a/b*100} %')


##JAWABAN No 4 TIPE 2

film_kamu = []
film_teman = []

for i in range(5):
    film=input('masukan nama film kesukaan kamu : ')
    film_kamu.append(film)
print(film_kamu)

for i in range(5):
    film=input('masukan nama film kesukaan kamu : ')
    film_teman.append(film)
print(film_teman)

a=set(film_kamu)
b=set(film_teman)
c=a.intersection(b)

print(f'list film yang sama {c}')
print(f'kecocokan kalian {len(c)/5*100}%')




#No 5

###===JAWABAN

# print(f'''
# Selamat Datang di Pasar Buah

# List Menu:
# 1. Menampilkan Daftar Buah
# 2. Menambah Buah
# 3. Menghapus Buah
# 4. Membeli Buah
# 5. Exit Program
# ''')
# a = int(input("Masukkan angka Menu yang ingin dijalankan: "))

# buah_1 ={
#     'Nama' : 'Apel',
#     'Stock' : '20',
#     'Harga' : 10000
# }

# buah_2 ={
#     'Nama' : 'Jeruk',
#     'Stock' : '15',
#     'Harga' : 15000
# }

# buah_3 ={
#     'Nama' : 'Anggur',
#     'Stock' : '25',
#     'Harga' : 20000
# }

# daftar_buah = {
#     '0' : buah_1,
#     '1' : buah_2,
#     '2' : buah_3
# }

# while True:
#     if a == 1:
#         print(f"{'Index':<9}| {'Nama':<9}| {'Stock':<9}| {'Harga':<9} ")

#         for buah in daftar_buah:
#             KEY = buah
            
#             NAMA    = daftar_buah[KEY]['Nama']
#             STOCK   = daftar_buah[KEY]['Stock']
#             HARGA   = daftar_buah[KEY]['Harga']

#             print(f"{KEY:<9}| {NAMA:<9}| {STOCK:<9}| {HARGA:<9} ")
        
#         a = int(input("Masukkan angka Menu yang ingin dijalankan: "))

#     elif a == 5:
#         break