# BREAK , CONTINUE , PASS ( LOOP CONTROL STATEMENTS)

# BREAK --> Untuk keluar dari sistem looping
#Continue ---> melewati suatu tugas di dalam looping , kemudia lanjut ke putara selanjutnya
#Pass --> Tidak melakukan apa"

###--------------------------------------######### SOAL

# list_mobil = ['toyota' , 'bmw' ,'tesla']
# list_negara = ['jepang' , 'jerman' , 'usa']



# for i in range (0 , 3):
#     print(f' mobil {list_mobil[index]} asalnya dari {list_negara[index]}')

    ####BELUM SIAP YANG DIATAS

##BREAK

# Kalimat = " saya pakai sepatu adidas"

# for huruf in Kalimat :
#     if huruf == 'y' :
#         break
#     print(huruf)

##SOAL 2 , PRINT 1-10 , KALAU KTEMU ANGKA 7 , BREAK

# for i in range (1,10):
#     if i > 7 :
#         break
#     print(i)


####---------------------------------####
#Continue

# kalimat = 'saya pakai sepatu adidas'
# for i in kalimat:
#     if i == 'a' :
#         continue

#     print(i)


####---------####

# list_a = [True , 'toyota' , 123 , 7.3]

# for i in list_a:
#     if type(i) == int:
#         continue
#     print(f'{i} adalah {type(i)}')


####---------------------------##########

# kalimat = 'saya pakai sepatu adidas'

# for i in kalimat:
#     pass


#####--------------------#######
#NESTED LOOP --->> LOOPING DI DALAM LOOPING
#CARA KERJA ---> INNER LOOPING AKAN DISELESAIKAN DLU,BARU LANJUT KE OUTER LOOPING
#CARRA 1
# for i in range(1,6):
#     print(f'ini adalah suapan ke {i}')

#     for komponen in ['nasi', 'rendang' , 'soup']:
#         print(komponen)


# #CARA 2 PAKAI WHILE
# suap = 1
# while suap <= 5:
#     print(f' ini adalah suapan ke {suap}')
#     for komponen in ['nasi', 'rendang' , 'soup']:
# #         print(komponen)

####_------------------------###
# suap = 1
# while suap <= 3:
#     print(f'ini adalah suapan ke {suap}')

#     for komponen in ['nasi' , 'rendang' , 'sayur']:
#         print(komponen)

#     suap += 1

# else:
#     print('saya sudah kenyang')
    
## CARA 2 -----

# for suap in range (1,6):
#     print(f'ini adalah suapan ke {suap}')

#     for komponen in ['nasi' , 'rendang' , 'sayur']:
#         print(komponen)

#     if suap == 3 :
#         print("aku sudah kenyang")
#         break



###_--------------------##########




# angka = 1
# for i in range(0,3):
#     for j in range (1,5):
#         print(angka,end=' ')

#     print(angka)

####-----------------######
logo = '*'
for i in range(1,5):
    for j in range(i):
        print(logo, end=' ')
    print()
    
 

           



    
    
    