# # Exercise: Function


# # ==========================================================================================
# # Soal 1

# # Tarif taxi per kilometer adalah 5000
# # Awal buka pintu sudah dikenakan tarif 8000
# # Berapa tarif taxi untuk perjalanan sejauh 1, 2, 3, 4, dan 5 kilometer?
# # input dan output berupa list


# #JAWABAN 1 TIPE 1
# # kilometer = [1,2,3,4,5]

# # print([i*5000+8000 for i in kilometer])

# ##JAWABAN 1 TIPE 2

# def tarif_perjalanan(jarak):                                        # Cara 2, menggunakan function def
#     buka_pintu = 8000
#     tarif_kilometer = 5000

#     list_tarif = []

#     for i in jarak:                                                 
        
#         tarif = i * tarif_kilometer + buka_pintu
#         list_tarif.append(tarif)

#     return list_tarif

# print(tarif_perjalanan([1,2,3,4,5]))






# # # ==========================================================================================
# # # Soal 2

# # # buat function dengan parameter yang akan diisi dengan argumen berupa sebuah kalimat, contoh
# # # argumen: teh cukup murah
# # # output: teh pukuc harum

# # # syarat: 
# # # hanya kata yg memiliki panjang lebih dari 3 huruf yang dibalik
# # # input hanya berupa huruf dan spasi, tanpa tanda baca

# # # sugestion: 
# # # pakai looping string dan list
# # # pakai conditional if

# # #JAWABAN ==============================
# def kalimat(kata_kata):
#     # list_kata = []
#     kalimat_baru = ''
#     a = kata_kata.split()
    
#     for i in a:
    
#         if len(i) > 3:
#             # list_kata.append(i [::-1])
#             kalimat_baru = kalimat_baru + i[::-1] + ' '
#         else:
#             # list_kata.append(i)
#             kalimat_baru = kalimat_baru + i + ' '


#     return kalimat_baru

# hasil =  kalimat(str(input('masukkan kata: ')))
# print(hasil)

  

    


# ==========================================================================================
# Soal 3

# Buat algoritma untuk memutar list di dalam list yang berukuran 3x3 satu kali searah jarum jam.
# misal:
# input
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]

# output
# [[7,4,1],
#  [8,5,2],
#  [9,6,3]]  

# nested loop
##JAWABAN 

A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
 ]

for i in range(len(A)):
    angka = []
    for j in range(len(A)):
        angka.append(A[-1-j][i])
    print(angka) 