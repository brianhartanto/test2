#Function
#Function adalah sebuah blok kode terorganisir yang dapat menerima input dan dapat digunakan berkali kali

#contoh built in function (bawaan dari python
# # len--> input berupa list , output berupa jumlah item
# list_angka = [3,1,4,2]
# print(len(list_angka))


# #==================================
# #Regular function

# def tambah(angkaA , angkaB):         # def nama_function(parameter)
#     return angkaA + angkaB             #return return_value


# print(tambah(10,3))

# #======================================
# #Function tanpa input(parameter) dan tanpa output (return_value)

# def salam():
#     print('selamat pagi')
#     print('kita akan belajar function')

# salam()

#SOAL: Buat function dengan hasil print:
#Menu utama:
#1. Cek Kuota
#2. Isi pulsa
#3.exit


#jawaban



# def menu_utama():
#     print('''
#     menu utama
#     1.Cek kuota
#     2.Isi pulsa
#     3.Exit
#     ''')

# menu_utama()


#========================================
#Function dengan input (parameter) tapi tanpa output (return_value)

# def perkenalan(nama,umur):
#     print(f'halo nama saya {nama} , umur saya {umur} tahun')

# perkenalan('brian',22)

# #Soal: buat function bernama oscar dengan parameter
# #berupa nama aktor , film dan tahunya
# #output: 
# #pemenang aktor terbaik tahun 2016 adalah leonardo di caprio
# #pada film ' the revenant'

# def oscar (nama, film , tahun):
#     print(f'''
#     pemenang aktor terbaik tahun {tahun}adalah {nama} pada film {film}
#     ''')

# oscar('leonardo di caprio ', 'the revenant' , '2016')


###============================
## Function dengan input (parameter) dan dengan output (return_value)

#Soal: buat function dengan input sebuah angka , dan outputnya 
#berupa kuadrat dari angka tsb

# def angka (a):
#     return a**2

# print(angka(3))


#---------------
#SOAL :BUAT FUNCTION LUAS LINGKARAN
#JUMLAHKAN NILAI LUAS LINGKARAN BERADIUS 5CM
#DENGAN NILAI KUADRAT 10

# import math 

# def lingkaran (r):
#     return math.pi * r**2
#     print(hasil)

# def kuadrat(angka):
#     hasil=angka**2
#     print(hasil)

# print(lingkaran(5))
# print(kuadrat(10))

# print(lingkaran(5) + kuadrat(10))


##BELUM JADI YG DIATAS INI !!!!


####====================

#Default parameter

# def tambah(angkaA=0, angkaB=100):
#     return angkaA + angkaB

# print(tambah(2))  ##Tambahnya 2 itu di angka A
# print(tambah(angkaB=5))  # 5 merefer angka b dan angka a otomatis bernilai 0






    

   


