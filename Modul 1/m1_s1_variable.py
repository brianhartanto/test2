print("hello world")

#membuat variable bernama box yang berisi text/string
box = 'Selamat Pagi'
print(box)
#menganti isi variabel box
box = 'Saya mau makan'
print(box)

#kapanpun kita panggil variable box , yang terpanggil adalah yang terakhir
print(box)

#variable --> fitur dalam bahasa pemograman untuk menyimpan suatu nilai/bisa dianalogikan sebagai sebuah box /box ini menyimpan sebuah nilai

namasiswakelasA = 'brian'
print(namasiswakelasA)

nama_siswa = 'lemmy'
print(nama_siswa)

#cara penamaan variable yg salah
# 1_nama_siswa = 'deny'
# print(1_nama_siswa)
# nama siswa = 'moris'
# print(nama siswa)
#nama-siswa = 'nicolas'
#print(nama-siswa)

#------------------
# data type (tipe data dari suatu variable)

my_var = 'brian'     #String (text: haru pakai kutip)
print(type(my_var))  #--- TYPE untuk mencari tau tipe data

my_var = 30          #--- Interger ( text tidak memakai kutip)
print(type(my_var))

my_var = 30.55       #--- float (dencimal)
print(type(my_var))

my_var = True  #boolean (true/false)
my_var = False

my_var = None   #none

# collection data type

my_var= [1,2,3]  #list
my_var= {1,2,3}  #set (tidak punya urutan)
my_var= (1,2,3)  #tuple
print(type(my_var))
my_var= [1,2,3]
print(my_var[0])   # Memanggil angka , angka pertama di mulai dari 0
print(type(my_var[0]))

my_var[0] = 100    #tuple tidak bisa diganti nilai itemnya
print(my_var)

#dictionary di dalam list
my_var = [{'id' : 101,'nama' :'brian', 'kelas' : 'data science'},
{'id' : 102,'nama' :'hartanto', 'kelas' : 'data science'}]      ### KEY->ID , VALUE ->101  , Kalo key ada yg duplikat, maka ditampilkan yg terakhir

print(my_var[0]['nama'])



#--------------------- Arithmetic Operation

hasil = 3+5
hasil = 3-5
hasil = 3*5
hasil = 3/5
hasil = 3//5    #pembagian pembulatan ke bawah
hasil = 10%3     #MODULUS--> Sisa pembagian 
hasil = 10**3    #pangkat
hasil = 5e4   # dikali 10 pangkat sekian
print(hasil)