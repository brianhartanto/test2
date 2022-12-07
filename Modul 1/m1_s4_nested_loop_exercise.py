# EXERCISE: NESTED LOOP

# ======================================================================================
# No. 1

# Output
# 9 8 7
# 6 5 4
# 3 2 1

###----------JAWABAN------######
# a = 9

# for i in range(0,3):
#     for j in range (0,3):
#         print(a,end=' ')
#         a -= 1
#     print()

# ======================================================================================
# No. 2

# list_angka = [1,2,3,4,5,6,7,8,9,10]
# Output: 1 4 16 25 49 64 100

# list_angka = [1,2,3,4,5,6,7,8,9,10]
# for i in list_angka:
#     if i in (3,6,9):
#         continue


#     print(i*i,end=' ')




# ======================================================================================
# No. 3

# * * * * *
# * * * *
# * * *
# * *
# *

# a = 5

# while a > 0:
#     for j in range (a):
#         print('*', end=' ')
#     print()
#     a += -1



###-------###
apel = 10
jeruk = 7
anggur = 6



transaction = True

stokapel = 10
stokjeruk = 7
stokanggur = 6

while transaction == True:
    Apel=int(input('Masukan Jumlah Apel: '))
    if Apel > stokapel:
        print(f'stok apel tinggal {stokapel}, coba lagi')
    else:
        hargaapel = Apel*10000
        break

while transaction == True:
    Jeruk=int(input('Masukan Jumlah Jeruk: '))
    if Jeruk > stokjeruk:
        print(f'stok apel tinggal {stokjeruk}, coba lagi')
    else:
        hargajeruk = Jeruk*15000
        break

while transaction == True:
    Anggur=int(input('Masukan Jumlah Anggur: '))
    if Anggur > stokanggur:
        print(f'stok apel tinggal {stokanggur}, coba lagi')
    else:
        hargaanggur = Anggur*20000
        break
                        
total = hargaapel+hargajeruk+hargaanggur

print(f'Apel : {Apel} x 10000 = {hargaapel} \nJeruk : {Jeruk} x 15000 = {hargajeruk} \nAnggur : {Anggur} x 20000 = {hargaanggur}')
print(f'Total : {total}')
jum_uang=int(input('Masukan Jumlah Uang: '))

if jum_uang < total:
    print(f'Transaksi anda dibatalkan \nuang kurang sebesar {total-jum_uang}')
    transaction = False
elif jum_uang == total:
    print(f'Terimakasih')
    transaction = False
else:
    print(f'Terimakasih \nuang kembali anda {jum_uang-total}')
    transaction = False






    

    