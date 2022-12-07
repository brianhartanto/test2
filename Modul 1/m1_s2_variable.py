#python function for arithmetic


#library yang menyimpan function untuk operasi matematika
import math

my_number = 63.8788

hasil = math.floor(my_number)   # MathFloor-> Pembulatan ke bawah
print(hasil)

hasil = math.ceil(my_number)   #mathceil --> pembulatan ke atas
print(hasil)

hasil = math.pow(my_number, 2)   #---> mathpow , perpangkatan , angka 2 dikarenakan pangkat 2 , **2 argumen
print(hasil)

hasil = math.sqrt(my_number) #---> mathsqrt artinya akar /square root
print(hasil)

hasil = math.fabs(-5.7) #---> mathfabs --> mengubah nilai negatif menjadi positif/absoulute/dimutlakan
print(hasil)

print(math.pi) #--> pi adalah 3.14 atau rumus V dari lingkaran

#my number diakarkan kemudian dibulatkan ke atas 
#fungsi tersebut diproses dari kanan
print(math.ceil(math.sqrt(my_number)))

#soal : berapa luas lingkaran berdiameter 10cm
diameter = 10
radius = diameter/2

luas_lingkaran = math.pow(radius,2) * math.pi  #VI r pangkat 2
print(round(luas_lingkaran,5) , 'cm')  #--> cara tambahin cm

#Pembulatan
print(round(3.475 ,2))


##########################################################
#caasting--> Mengubah tipe data dari sebuah variable

varA = '123'  # TIPE DATA --> str
print(varA)
print(type(varA))

new_varA = int(varA)  # Mengubah string menjadi interger
print(new_varA)
print(type(new_varA))

new_varB = float(new_varA)  #mengubah interger menjadi float .... ** FLOAT TIDAK BISA DIUBAH MENJADI String KARENA STR ADALAH BILANGAN BULAT**
print(new_varB)
print(type(new_varB))

new_varC = int(new_varB)  # mengubah float menjadi interger
print(new_varC)
print(type(new_varC))

varB = True    #---> Tipe data Boolian
print(varB)
print(type(varB))

new_varB = str(varB) #---> mengubah dari boolian menjadi string
print(new_varB)
print(type(new_varB))

new_varBB = int(varB)  #--> boolean menjadi interger (FALSE = 0 , TRUE=1 )
print(new_varBB)
print(type(new_varBB))


##### user input = meminta input dari user/ manusia
#umur =int(input('berapa umur anda?'))   #mengubah dari string ke int
#print(umur)
#print(type(umur))

#lima_tahun = umur + 5
#print(lima_tahun)

#umur = input('masukan umur:')
#print(int(umur)+5)


## TANDA PETIK PADA STRING
print('saya nonton avatar')
print("saya nonton avatar")
print('saya nonton "avatar"')

print('''saya nonton "black panther"''')


### ESCAPE CHARACTER
print("saya nonton \"Avatar\"")

##### LEN --> Lenght/ jumlah karakter dalam sebuah kalimat
kalimat = 'This is python'
print(len(kalimat))
print(kalimat.index('th')) #mencari indnex subsstring di dalam string .. ** index digunakan untuk mencari huruf di dalam kalimat

#Mengubah menjadi upper&Lower
print(kalimat.upper())
print(kalimat.lower())
#Huruf kapital di awal kata
print(kalimat.capitalize())
#String/Slicing/Indexing

print(kalimat[0]) #karakter awal
print(kalimat[-1]) #karakter akhir
print(kalimat[0:14]) #print kata lebih dari 1 kata
print(kalimat[ : : 2]) ###Start stop step
print(kalimat[ : : -2])  # step mundur

##String formating
umur = 20
print('umur saya', umur , 'tahun')

print(f'umur saya {umur} tahun')   #f'artinya untuk formating kurung keriting

#STING CHECK

kalimat = 'saya sedang belajar data science'
print('bela' in kalimat) #--> artinya apakah kata bela ada di dalam kalimat?
print('bela' not in kalimat)#--> artinya apakah kata bela tidak ada di dalam kalimat?

print(kalimat.count('a'))  #menghitung jumlah kata A di dalam kalimat
print(kalimat.count('data'))
print(kalimat.isalpha()) #--> mengecek apakah huruf alphabet , hasilnya false karena ada mengandung spasi
print(kalimat[ :4].isalpha()) #--> hasilnya true karena tidak mengandung spasi
print(kalimat.isalnum()) #--> apakah ada numbering?


nama = 'boeing828'
print(nama.isalnum())
print(nama.isspace()) # apakah mengandung spasi?
print(nama.isupper()) # apakah mengandung huruf besar?
print(nama.islower())

