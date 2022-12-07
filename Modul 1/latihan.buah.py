buah_1 = {
    'nama'  : 'apel' ,
    'stock' : '20' ,
    'harga' :  '10000'
}

buah_2 = {
    'nama'  :  'jeruk' ,
    'stock' :  '15' ,
    'harga' :  '15000'

}

buah_3 = {
    'nama'  :  'anggur' ,
    'stock' :   '25' ,
    'harga' :   '20000'
}

dict_1 = {
    'nama'  : 'NAMA',
    'stock' : 'STOCK',
    'harga' : 'STOCK'
}


daftar_buah = [
    buah_1,
    buah_2,
    buah_3
]
while True:
    a = int(input('Pilih list menu yang mau dijalankan :'))
    if a == 1 :
        print(f"{'index':<9}|{'nama':<9}|{'stock':<9}|{'harga':<9}")

        for key in range (len(daftar_buah)) :

            NAMA = daftar_buah[key]['nama']

            STOCK = daftar_buah[key]['stock']
            HARGA = daftar_buah[key]['harga']
            print(f"{key:<9}|{NAMA:<9}|{STOCK:<9}|{HARGA:<9}")

    elif a == 5:
        break

    elif a== 2:
        buah_baru=dict.fromkeys(dict_1.keys())
        buah_baru['nama']=(input('masukan nama buah :'))

        buah_baru['stock']=(input('masukan stock buah :'))
        buah_baru['harga']=(input('masukan harga buah :'))

        daftar_buah.append(buah_baru)

    elif a==3:
        print(f"{'index':<9}|{'nama':<9}|{'stock':<9}|{'harga':<9}")

        for key in range (len(daftar_buah)) :

            NAMA = daftar_buah[key]['nama']

            STOCK = daftar_buah[key]['stock']
            HARGA = daftar_buah[key]['harga']
            print(f"{key:<9}|{NAMA:<9}|{STOCK:<9}|{HARGA:<9}")

        hapus = int(input('masukan index yang mau dihapus :'))


        del daftar_buah [hapus]
        print(f"{'index':<9}|{'nama':<9}|{'stock':<9}|{'harga':<9}")
        for key in range (len(daftar_buah)) :

            NAMA = daftar_buah[key]['nama']

            STOCK = daftar_buah[key]['stock']
            HARGA = daftar_buah[key]['harga']
            print(f"{key:<9}|{NAMA:<9}|{STOCK:<9}|{HARGA:<9}")
