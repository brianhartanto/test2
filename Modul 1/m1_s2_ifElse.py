#conditional statement
#comparison : operator perbandingan

# print(10>3)  #lebih dari
# print(10<3)  #kurang dari
# print(10>=3) #lebih dari atau sama dengan
# print(10<=3) #kurang dari atau sama dengan

# print(10==3) #sama dengan
# print(10!=3) #tidak sama dengan


# #logical operator : and , or , not
# #AND --> semua kondisi harus true

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# #OR --> Minimal 1 kondisi harus true
# print(True or True)
# print(True or False)

# #not
# print(not True)
# print(not False)

#conditional statement
#program akan dijalani bila sesuai dengan statement atau terpenuhi
#boleh ujian sim untuk 17 tahun ke atas
#if True:
 #   print('kondisi terpenuhi')
  #  print('aaa')


# #umur = int(input('masukan umur :'))
#if umur > 17 :
 #   print('silahkan ikut ujian SIM')

#if else statement: jika kondisi if false , maka statement else yang akan dijalankan

#umur : 14
#if umur>=17 :
 #   print('silahkan ikut ujian SIM')

#else:
 #   print('Balik lagi kalau sudah 17 tahun')


#if elif else statement
#jika kondisi if terpenuhi/true , maka statement di if dijalankan
#jika kondisi di if tidak terpenuhi/false , maka statement di elif dijalankan
#jika kondisi di elif tidak terpenuhi/false , maka statement di else dijalankan
#hanya salah satu kondisi dijalankan

nilai = 90

#if nilai > 90:
 #   print("nilai A")
#elif nilai > 80:
 #   print("nilai B")
#elif nilai > 60:
 #   print("nilai C")
#else :
 #   print("nilai D") 

if nilai > 90:
    print("nilai A")
    if nilai > 95:
        print("+")
    else:
        print("-")

else:
    print("nilai B")
    if nilai > 80:
        print("+")
    else:
        print("-")

        #bisa if dan elif , ga pake else , kalau tidak ada kondisi yg terpenuhi , maka tidak ada yang dieksekusi