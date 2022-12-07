import math

# x = 4
# y = 3
# z = 2
# print(pow((x+(y*z))/(x*y),2))    #NO 1


#No 2
# pertanyaan = input("silahkan masukan angka :")

# print(pow(int(pertanyaan),2))

# No3
# total_hari = 485
# tahun = 360
# bulan = 30

# jumlahtahun =(math.floor(total_hari/360))

# sisabulan = total_hari%360
# jumlahbulan =(math.floor(sisabulan/30))

# sisaminggu=sisabulan%30
# jumlahminggu=(math.floor(sisaminggu/7))

# sisahari= sisaminggu%7
# jumlahhari=(math.floor(sisahari))

# print(f'{jumlahtahun} tahun {jumlahbulan} bulan {jumlahminggu} minggu {jumlahhari} hari')

#No 4
# varA=4
# varB=10
# varC=49

# umurA = varA/(varA+varB)*varC
# print(umurA+2)

# umurB = varB/(varA+varB)*varC
# print(umurB+2)

# #no5

# jarak = 120
# mobilA = 60/60  #bagi 60 karena convert dari hour ke minute
# mobilB = 40/60
# waktu = jarak/(mobilA + mobilB)
# jam = 9 + waktu //60
# menit = waktu%60
# print (f'waktu tabrakan (menit) adalah {waktu}, dalam (jam) {int(jam)} , {int(menit)} menit')


# ##################################
# #no1

# angka= int(input('masukan angka :'))
# if angka%2==1:
#     print('ganjil')

# else :
#     print('genap')

# ##################
# #No2

# massa= int(input('masukan massa dalam KG '))
# tinggi= int(input('masukan tinggi dalam M '))
# IMT = massa /(tinggi/100)**2

# print(f'massa {massa} kg/ tinggi {tinggi/100}) m')

# if IMT < 18.5 :
#     print(f' IMT={IMT} , BERAT BADAN KURANG')

# elif IMT < 25:
#     print(f' IMT={IMT} , BERAT BADAN KURANG IDEAL')

# elif IMT <30 :
#     print(f' IMT {IMT} ,BERAT BADAN BERLEBIH')

# elif IMT <40 :
#     print(f' IMT {IMT} ,BERAT BADAN SANGAT BERLEBIH')

# else:
#     print(f' IMT {IMT} , OBESITAS')

# #No 3

# apel = int(input("Masukan Jumlah Apel :"))
# Jeruk = int(input("masukan jumlah Jeruk :"))
# Anggur = int(input("Masukan jumlah anggur :"))

# hargaapel = apel*10000
# hargajeruk = Jeruk*15000
# hargaanggur = Anggur*20000
# total= hargaapel+hargajeruk+hargaanggur

# print(f'''
# apel : {apel} * 10000 = {hargaapel}
# jeruk : {Jeruk} * 15000 ={hargajeruk}
# anggur : {Anggur} * 20000 = {hargaanggur}
# total = {total}
# ''')

# jumlahuang=int(input("Masukan Jumlah Uang :"))
# if jumlahuang < total:
#     print(f' transaksi anda dibatalkan')
# elif jumlahuang == total:
#     print(f'Terima kasih ')

# else:
#     print(f'terima kasih \nuang kembalian anda {jumlahuang-total}')




