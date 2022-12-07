# EXERCISE: LOOPING

# ====================================================================================
# 1. 
# kalimat = 'Kamu harus menampilkan hanya kata yang berawalan huruf k pada kalimat ini'
# Tampilkan hanya kata yang berawalan huruf k pada kalimat ini

##----------JAWABAN NO 1--------------------######
kalimat = "kamu harus menampilkan hanya kata yang berawalan huruf k pada kalimat Ini "

# x=(kalimat.split())
# print(x)

# for i in x:
#     if i[0] == 'k':
#         print(i)

##---------JAWABAN NO 1 TIPE 2----------------#####

# for a in kalimat.split():
#     if a.startswith('k'):
#         print(f'kata yang berawal dengan huruf k adalah : {a}')
#     elif a.startswith('K'):
#         print(f'kata yang berawal dengan huruf k adalah : {a}')

##------------JAWABAN NO 1 TIPE 3 ---------------###
# list_kalimat = kalimat.split(' ')

# for kata in list_kalimat:
#     if kata[0] == 'k' or kata[0] =="K":
#         print(kata)


# ====================================================================================
# 2. 
# Dari angka 1 hingga 50, tampilkan angka yang habis dibagi 3!



##--------JAWABAN NO 2-----------#####
# for i in range (3,51,3):
#     print(i)




# ====================================================================================
# 3. 
# kalimat = 'Tampilkan kata yang memiliki jumlah karakter berjumlah genap pada kalimat ini'
# # Tampilkan kata yang memiliki jumlah karakter berjumlah genap!

# x=(kalimat.split())
# print(x)

# for i in x:
#     if len(i)%2 == 0:
#         print(i)
    
    
    
    
 
 
 
    






# ====================================================================================
# 4. 
# Buatlah program yang menampilkan integer dari 1 hingga 100 dengan spesifikasi:
    # - Jika angka merupakan kelipatan 3, maka print 'kelipatan 3'
    # - Jika angka merupakan kelipatan 5, maka print 'kelipatan 5'
    # - Jika angka merupakan kelipatan 3 dan 5, maka print 'kelipatan 3 & 5'

# for i in range (1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f'{i} adalah pembagian 3 dan 5')
#     elif i % 3 == 0:
#         print(f'{i}adalah kelipatan 3')
#     elif i % 5 == 0:
#         print(f'{i}adalah kelipatan 5')
#     else:
#         print(i)

    
        


# ====================================================================================
# 5. 
# Dari list berikut: [12, 15, 1, 7, 4, 100]
# Buat algoritma untuk mencari angka tertinggi di dalam list tanpa menggunakan fungsi max atau sort
# list_angka = [12 ,15, 1, 7, 4, 100]

# list_angka = [12 ,15, 1, 7, 4, 100]
# nilaiterbesar = list_angka[0]

# for nilai in list_angka:
#     if nilaiterbesar < nilai:
#         nilaiterbesar = nilai
# print(f'Angka tertinggi didalam list = {nilaiterbesar}')





#####---------TUGAS MEMBALIKAN ANGKA SEPERTI 1234 -> 3412-----------####

while True:
    try:
        a=int(input(f'masukan 4 angka bebas:'))
        if(len(str(a))) == 4 :  ### LEN TIDAK BISA DNGAN INT , HARUS DIUBAH JADI STR
            b = a//100
            c = a%100
            d = c*100
            e = d + b
            print(a)
            print(e)
            break
        else:
            print("lebih dari 4 angka")
    except:
        print(' yang dimasuk harus angka bro')
        
