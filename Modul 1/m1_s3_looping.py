#Loop Statement --> mengeksekusi sebuah kode secara berulang



# for i in range(0,5):
#     print("Saya sedang belajar python")

#WHILE LOOP
#Selama kondisinya terpenuhi(true) makan looping akan dijalankan terus
#looping akan berhenti ketika kondisi false

#INFINITE LOOP HARUS DIHINDADRI !!! UNTUK MENHENTIKAN INFINITE LOOP BISA CTRL+C DI TERMINAL!!
##--------------------------------------------------------------------


#CARA LOOPING YANG BENAR !!

# cetak = 1

# while cetak <= 5:          #WHILE BISA DIGABUNG DENGAN ELSE
#     print("Saya Sedang belajar python")

#     cetak = cetak + 1

#     print(cetak)
# else:
#     print('Sudah 5 kali')

    ##--SOAL -- Cetak 1 - 30 dengan while loop

# cetak = 1
# while cetak <= 30:
#     print(cetak)
#     cetak = cetak + 1   #Cara singkat cetak += 1
# else:
#         print('Sudah 30')

   #--SOAL -- Cetak 1-30 hanya bilangan ganjil
# cetak = 1
# while cetak <= 30:   #CARA 1
#     print(cetak)
#     cetak = cetak + 2

# cetak = 1
# while cetak <= 30:            #CARA 2
#     if cetak % 2 != 0:
#         print(cetak , end='--')   # CARA NGEPRINT DI TERMINAL KE SAMPING ( END='')
#     else:
#         pass
#     cetak += 1

############################################################
#_-------------------------------------------------------#
#FOR LOOP --> Looping akan dijalankan selama item dalam collection data type belum habis

#CONTOH LOOPING PADA LIST

# for item in [1,2,3,4,5]:
#     print(f' ini suapan ke {item}')

###################################################
#_--------------------------------------------#
#LOOPING PADA RANGE (Start,Stop,Step)

# for item in range(1,6,1):
#     print(item)


###------------------------------######
#SOAL
# for i in range (5,26,5):
#     print(f' angka {i} adalah kelipatan 5')

#----------------------------------
# list_isi_tuple = [(1,100) , (2,200) , (3,300)]

# for item_depan , item_belakang in list_isi_tuple:   #Cara Unpacking list isi tuple
#     print(item_depan)
#     print(item_belakang)

#looping pada tuple
# my_tuple = ('mangga' , 'jeruk' , 'apel')
# for buah in my_tuple:
#     print(buah)


# my_dict = {
#     'Toyota' : 'inova' ,
#     'honda'  :  'civic' ,
#     'lamborgini' : 'aventador'
#     }

# for mobil in my_dict:  #### .ITEMS --> output key nya saja
#     print(mobil)

# for mobil in my_dict.items():  #### .ITEMS --> output key dan valuenya dalam tuple
#     print(mobil)

# for mobil in my_dict.values():  #### .ITEMS --> output hanya value nyya aja
#     print(mobil)

# for a,b in my_dict.items():
#     print(f'{a} memproduksi {b}')

## Menjumlahkan angka di dalam list dengan for loop

# list_angka = [1,2,3,4,5]
# total = 0

# for i in list_angka:
#     total += i  ## Total = total + i

# print(total)


####-------------------------- LOOPING DENGAN LIST

list_mobil = ['ferari' , 'toyota' , 'honda' , 'bmw' , 'mercedes' , 'wuling']
print(len(list_mobil))

for i in range(len(list_mobil)):    #range(0,6,1)
    print(list_mobil[i])
    

for i in range(1, len(list_mobil),2):
    print(list_mobil[i])

for i in range(0, len(list_mobil),2):
    print(list_mobil[i+1])

###--------------------------------------------

# list_mobil = ['ferari','toyota','honda','bmw','mercedes','wuling']

# # for i in enumerate(list_mobil):
# #     print(i)

# for no , name in enumerate(list_mobil):
#     print(f'mobil urutan ke {no+1} adalah {name}')

