data_1={
    'NamaKaryawan' : 'Reyhan' ,
    'Umur'         :  '21'  ,
    'Jabatan'      :  'OB'  ,
    'JenisKelamin' :   'Pria' ,
    'Gaji'         :    'Rp3000000'
}
data_2={
    'NamaKaryawan'  : 'Bimo' ,
    'Umur'          : '18' ,
    'Jabatan'       : 'CustomerService' ,
    'JenisKelamin'  : 'Pria' ,
    'Gaji'          : '3000000'
}

data_3={
    'NamaKaryawan'  : 'Ananda' ,
    'Umur'          : '24' ,
    'Jabatan'       : 'Penonton' ,
    'JenisKelamin'  : 'Pria' ,
    'Gaji'          :  '4000000'
}

def menu_utama():

    print('''
=============Welcome To =============
1.Report Data Karyawan
2.Menambahkan Data Karyawan
3.Mengubah Data Siswa
4.Menghapus Data Siswa
5.Exit

    ''')

    UserInput1 = int(input(f'Silahkan Pilih Menu Tersebut :'))
    return UserInput1 #untuk Membalikan panggilan user input 1

def menu1():
    print('''=============Report Data Karyawan=============
    1. Report Seluruh Data
    2. Report Data tertentu
    3. Kembali ke menu Utama
    ''')

    UserInput = int(input(f'Silahkan Pilih Sub Menu Data [1-3]:'))
    return UserInput

def menu2():
    print('''=============Report Data Karyawan=============
    1.Tambah Data Siswa
    2.Kembali ke Menu Utama ''')

    UserInput =int(input(f'Silahkan Pilih Sub Menu Data [1-2]:'))
    return UserInput

def menu3():
    print('''=============Mengubah Data=============
    1.Ubah Data Siswa
    2.Kembali ke Menu Utama ''')

    UserInput =int(input(f'Silahkan Pilih Sub Menu Data [1-2]:'))
    return UserInput

def menu4():
    print('''=============Menghapus Data Karyawan=============
    1.Hapus Data Karyawan
    2.Kembali ke Menu Utama ''')

    UserInput = int(input(f'Silahkan Pilih Sub Menu Data [1-2]:'))
    return UserInput
#####----LOOPING MENU 1
def start():
    while True:
        input1 = menu_utama()

        if input1 == 1 :
            UserInput = menu1()
            if UserInput == 3:
                continue
        elif input1 == 2:
            UserInput = menu2()
            if UserInput == 2:
                continue
        elif input1 == 3:
            UserInput = menu3()
            if UserInput == 2:
                continue
        elif input1 == 4:
            UserInput = menu4()
            if UserInput == 2:
                continue
        elif input1 == 5:
            break
        else:
            print('input yang anda masukan salah')
            continue

start()
