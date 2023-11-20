# DATA WAREHOUSE
product_stock = [
    {'sku':'S001', 'kategori':'smartwatch', 'produk':'Shark S1', 'stok': 20, 'cogs':500000},
    {'sku':'S002', 'kategori':'smartwatch', 'produk':'Shark Gt', 'stok': 15, 'cogs':350000},
    {'sku':'S003', 'kategori':'smartwatch', 'produk':'Shark Neo', 'stok': 20, 'cogs':250000},
    {'sku':'S004', 'kategori':'smartwatch', 'produk':'Shark Runner', 'stok': 20, 'cogs':700000},
    {'sku':'S005', 'kategori':'earphone', 'produk':'Lucifer T14', 'stok': 20, 'cogs':180000},
    {'sku':'S006', 'kategori':'earphone', 'produk':'Lucifer T6', 'stok': 20, 'cogs':320000},
    {'sku':'S007', 'kategori':'earphone', 'produk':'Lucifer T9', 'stok': 16, 'cogs':150000},
    {'sku':'S008', 'kategori':'funcooler', 'produk':'Cooler 2 Pro', 'stok': 20, 'cogs':300000},
    {'sku':'S009', 'kategori':'funcooler', 'produk':'Cooler Plus', 'stok': 13, 'cogs':250000},
    {'sku':'S010', 'kategori':'funcooler', 'produk':'Cooler 3 Pro', 'stok': 20, 'cogs':250000}
]


# STAFF INFORMATION
staff_akses = [
    {'name':'Diyan Pitriani', 'position':'Warehouse', 'id':'w02', 'password':'staff01'},
    {'name':'Emil Supriatna', 'position':'Sales', 'id':'s01', 'password':'staff02'},
    {'name':'Danil Ibnusina', 'position':'Finance', 'id':'f03', 'password':'staff03'},
    {'name':'Yana Ruhyana', 'position':'Purchase', 'id':'p04', 'password':'staff04'}
]


# FINANCE PART
shipping_cost = 10000
tax = 0.11
commission = 0.02
min_margin = 0.05


# SALES RECORDS
penjualan = [{'trx_no':'Trx-001', 'tanggal':'2023-11-15', 'produk':'Shark Gt', 'sales':3, 'cogs':350000, 'harga_jual':449000, 'total':1347000},
             {'trx_no':'Trx-002', 'tanggal':'2023-11-17', 'produk':'Lucifer T9', 'sales':4,'cogs':150000, 'harga_jual':229000, 'total':916000},
             {'trx_no':'Trx-003', 'tanggal':'2023-11-17', 'produk':'Shark Gt', 'sales':2,'cogs':350000, 'harga_jual':469000, 'total':938000},
             {'trx_no':'Trx-004', 'tanggal':'2023-11-19', 'produk':'Cooler Plus', 'sales':7,'cogs':250000,  'harga_jual':349000, 'total':2443000}]

position = ''

# ---------------------------------------------------------------------------------------------------------------------

# HELPER FUNCTION
def daftarProduct():      # berfungsi untuk menampilkan daftar produk beserta total stoknya
    print('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
    print('\n\t\t\tDAFTAR STOK')
    print('SKU\t KATEGORI\t PRODUK\t\t STOK\t COGS\n-----------------------------------------------------------')
    for i in product_stock:
        print('{}\t {}\t {}\t {}\t {}'.format(i['sku'],i['kategori'],i['produk'],i['stok'],format_rupiah((i['cogs']))))

def display_product_info(index):
    print('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n')
    print('SKU\t KATEGORI\t PRODUK\t\t STOK\t COGS')
    product_info = product_stock[index]
    print('{}\t {}\t {}\t {}\t {}'.format(product_info['sku'], product_info['kategori'], product_info['produk'],
                                           product_info['stok'], format_rupiah(product_info['cogs'])))
    print('\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')

def salam(data):             # ketika memasukkan posisi pekerjaan, sistem akan mmenyapa nama staff sesuai posisi yang diinput
    index = int(data)
    for i, staff in enumerate(staff_akses):
        if i == (index-1):
            print('\n\n-----------------------------------------------------------')
            print(f'\nHalo {staff["name"].upper()},\nSelamat Menggunakan layanan Kami!')
    return position

def salam_penutup():        # ketika staff divisi menutup sistem, sistem akan mengucapkan terima kasih atas penggunaan layanan
    print('\n"TERIMA KASIH TELAH MENGGUNAKAN LAYANAN KAMI.\nSEMOGA HARI ANDA MENYENANGKAN!"\n')
    

def pass_staff(data):      # menampilkan password dari staff tertentu
    index = int(data)
    for i, staff in enumerate(staff_akses):
        if i == (index-1):
            return str(staff['password'])

def input_pass():           # input password
    return input('Masukkan password Anda: ')

def productForSale():    # selain menampilkan daftar produk dan total stok, fungsi ini juga menampilkan harga modal dari produk sebagai panduan penjual menentukan harga jual 
    print('\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n')
    print('\t\tDAFTAR STOK UNTUK PENJUALAN')
    print('SKU\t KATEGORI\t PRODUK\t\t STOK\t HARGA JUAL MINIMAL\n-------------------------------------------------------------')
    for i in product_stock:
        print('{}\t {}\t {}\t {}\t {}'.format(i['sku'],
                                              i['kategori'],
                                              i['produk'],
                                              i['stok'],
                                              format_rupiah(i['cogs']+i['cogs']*min_margin+i['cogs']*tax+i['cogs']*commission+shipping_cost)))

def urutkan(nilai, data, urutan):  # fungsi ini membantu dalam melakukan sorting data sesuai value
    data = sorted(data, key=lambda x: x[nilai], reverse = urutan)
    return data

def format_rupiah(amount):    # fungsi ini membantu menampilkan format Rupiah
    rupiah = "Rp {:,}".format(amount)
    return rupiah

def print_bold(text):         # Fungsi ini membantu memberikan cetak tebal pada hasil print
    change = ("\033[1m" + text + "\033[0m")
    return change

def menu_tidakValid():
    print('\n"PILIHAN TIDAK VALID, SILAKAN PILIH SESUAI DAFTAR MENU!"')

def no_trx():                 # Membuat nomor transaksi terbaru untuk mengisi 'trx_no' pada variable penjualan
    trx_number = [i['trx_no'] for i in penjualan]
    length_number = len(trx_number)
    while 'Trx-00'+str(length_number) in trx_number:
        length_number += 1
    new_trx_no = 'Trx-00'+str(length_number)
    if len(new_trx_no) > 7:
        new_trx_no = new_trx_no[:4] + new_trx_no[-3:]
    return new_trx_no

def input_tanggal():        # memasukkan format tanggal
    from datetime import datetime
    while(True):
        try:
            tanggal_str = input("\nMasukkan tanggal (YYYY-MM-DD): ")
            return  datetime.strptime(tanggal_str, "%Y-%m-%d").date()
        except ValueError:
            print('\n"FORMAT TANGGAL TIDAK VALID. SILAKAN COBA LAGI!"')


# ------------------------------------------------------------------------------------------------------------------------


# MENU-FUNCTION
def menu_position():
    return input('''
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
                 
Selamat Datang Di "SABANG ERP"!
Kami memberi kemudahan dalam menjalankan operasional perusahaan Anda.
                    
Daftar Posisi:
1. Warehouse\t 2. Sales\t 3. Finance\t 4. Purchase\t 5. Exit
Silakan Masukkan Posisi Anda: ''').title()


# FUNCTION MENU 1: WAREHOUSE
def menu_warehouse():
    return input('''
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
                 
Menu Utama:
1. Lihat Daftar stok
2. Tambah stok Produk
3. Tambah Produk Baru
4. Edit Informasi Produk
5. Hapus Produk
6. Kembali
Silakan pilih menu Anda: ''')

def tampilkan_daftarProduk():
    global product_stock
    while(True):
        menu = input('''
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~

Submenu 'Lihat Daftar stok':
1. Tampilkan semua produk
2. Filter berdasarkan kategori
3. Urutkan data tertentu (A-Z)
4. Kembali
Silakan pilih submenu Anda: ''')
        if menu == '1':
            daftarProduct()
        elif menu == '2':
            kategori = input('\nMasukkan kategori yang ingin dilihat:').lower()
            kategori_list = [i['kategori'] for i in product_stock]
            if kategori not in kategori_list:
                print('\n"KATEGORI TIDAK DITEMUKAN. SILAKAN PERIKSA KEMBALI KATEGORI PRODUK YANG TERSEDIA!"\n')
            elif kategori in kategori_list:
                print('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
                print('\n\t\t\tDAFTAR STOK')
                print('SKU\t KATEGORI\t PRODUK\t\t STOK\t COGS\n-----------------------------------------------------------')
                for i in product_stock:
                    if i['kategori'] == kategori:
                        print('{}\t {}\t {}\t {}\t {}'.format(i['sku'],i['kategori'],i['produk'],i['stok'],format_rupiah(i['cogs'])))
        elif menu == '3':
            column_data = input('\nPilih kolom yang ingin Anda urutkan: ').lower()
            list_column = list(product_stock[0].keys())
            if column_data in list_column:
                product_stock = urutkan(column_data, product_stock, False)
                daftarProduct()
            else:
                print('\n"KOLOM DATA TIDAK DITEMUKAN. SILAKAN PERIKSA DAFTAR KOLOM!"')
        elif menu == '4':
            break
        else:
            menu_tidakValid()

def tambah_stok():
    global product_stock
    main_loop_flag = True
    while main_loop_flag:
        sku = input('\nMasukkan sku yang ingin diupdate: ').title()
        sku_list = [i['sku'] for i in product_stock]
        if sku not in sku_list:
            print('\n"SKU TIDAK DITEMUKAN. SILAKAN PERIKSA DAFTAR SKU DAN COBA LAGI!"')
            main_loop_flag = False
            break
        elif sku in sku_list:
            produk_sku = [i['produk'] for i in product_stock if i['sku']==sku]
            print('Anda ingin menambahkan stok pada produk {}'.format(produk_sku))
            sub_loop_flag = True
            while(sub_loop_flag):
                stok = input('Masukkan jumlah stok setelah "Stock Checking" pada barang yang sampai: ')
                try:
                    stok = int(stok)
                    if stok <= 0:
                        print('\n"STOK YANG DIMASUKKAN HARUS LEBIH DARI 0!"\n')
                    else:
                        print(f'\nStok pada produk {str(produk_sku)} akan ditambahkan sebanyak {stok} pcs.')
                        while(True):
                            penambahan = input('Tekan "Ya" jika ingin menyimpan penambahan stok, atau "Tidak" jika ingin membatalkan: ').lower()
                            if penambahan == 'tidak':
                                print('\n"STOK BATAL DITAMBAHKAN!"')
                                sub_loop_flag = False
                                main_loop_flag = False
                                break
                            elif penambahan == 'ya':
                                for item in product_stock:
                                    if item['sku'] == sku:
                                        item['stok'] += stok
                                        print(f'\nstok {produk_sku} berhasil ditambahkan. stok saat ini adalah {(item["stok"])} pcs.')
                                sub_loop_flag = False
                                main_loop_flag = False
                                break
                            else:
                                print('\nHanya masukkan (Ya/Tidak)!\n')
                except ValueError:
                    print('\n"SILAKAN MASUKKAN HANYA ANGKA PADA STOK!\n"')
                    continue

def tambah_produk():
    global product_stock
    main_loop_flah = True
    while main_loop_flah:
        sku = input('\nMasukkan sku produk: ').title()
        kategori = input('Masukkan kategori produk: ').lower()
        produk = input('Masukkan nama produk: ').title()
        sku_list = [i['sku'] for i in product_stock]
        produk_list = [i['produk'] for i in product_stock]

        max_length = {'sku': 7, 'kategori': 14, 'produk': 14}
        min_length = {'sku': 4, 'kategori': 7, 'produk': 7}
        if sku in sku_list:
            print('\n"SKU SUDAH TERDAFTAR. SILAKAN INPUT NOMOR SKU LAIN!"')
            continue
        elif produk in produk_list:
            print('\n"NAMA PRODUK SUDAH TERDAFTAR. SILAKAN INPUT NAMA PRODUK LAIN!"')
            continue
        elif len(sku) > max_length['sku'] or len(sku) < min_length['sku']:
            print(f'\n"Jumlah karakter pada kolom "SKU" harus lebih dari 4 dan kurang dari 7 karakter!"')
            continue
        elif len(kategori) > max_length['kategori'] or len(kategori) < min_length['kategori']:
            print(f'\n"Jumlah karakter pada kolom "Kategori" harus lebih dari 7 dan kurang dari 14 karakter!"')
            continue
        elif len(produk) > max_length['produk'] or len(produk) < min_length['produk']:
            print(f'\n"Jumlah karakter pada kolom "Nama Produk" harus lebih dari 7 dan kurang dari 14 karakter!"')
            continue
        elif sku not in sku_list and produk not in produk_list:
            try:
                stok = input('Masukkan jumlah stok: ')
                cogs = input('Masukkan cogs produk: ')
                stok = int(stok)
                cogs = int(cogs)
                if stok > 0 and cogs > 0:
                    while(True):
                        simpan = input('\nApakah Anda ingin menyimpan data?\nPastikan Anda telah mengisi informasi produk dengan benar. (Simpan/Batal): ').lower()
                        if simpan == 'simpan':
                            product_stock.append({
                                'sku': sku,
                                'kategori': kategori,
                                'produk': produk,
                                'stok': stok,
                                'cogs': cogs
                            })
                            print(f'\n"PRODUK {produk.upper()} BERHASIL DITAMBAHKAN.\nSILAKAN LIHAT PRODUK PADA DAFTAR STOK."')
                            main_loop_flah = False
                            break
                        elif simpan == 'batal':
                            print('\n"PENAMBAHAN PRODUK DIBATALKAN!"')
                            main_loop_flah = False
                            break
                        else:
                            print('\nHanya masukkan (SIMPAN/BATAL)!')
                else:
                    raise ValueError
            except ValueError:
                print('\n"SILAKAN INPUT HANYA ANGKA DAN HARUS LEBIH DARI 0 PADA INFORMASI STOK DAN COGS!"')
                continue

def edit_informasiProduk():
    global product_stock
    while(True):
        menu = input('''
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~

Submenu "Edit Informasi Produk":
1. Tampilkan daftar produk
2. Pilih sku yang ingin diedit
3. Kembali ke menu utama
Silakan pilih sub menu Anda: ''')
        if menu == '1':
            daftarProduct()
        elif menu == '2':
            notif_cogs = '\n"COGS HANYA DAPAT DIUBAH OLEH MANAJEMEN!"\n'
            notif_stok = '''
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~

STOK hanya dapat diubah dengan kondisi berikut:
1. Penambahan stok dilakukan pada menu "Tambah Stok Produk"
2. Pengurangan stok dapat dilakukan hanya jika terjadi penjualan

~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
            '''
            main_loop_flag = True
            while main_loop_flag:
                sku = input('\nMasukkan SKU yang ingin diubah: ').upper()
                sku_list = [item['sku'] for item in product_stock]
                if sku in sku_list:
                    index = sku_list.index(sku)
                    print(f'\nANDA INGIN MENGUBAH INFORMASI PADA PRODUK BERIKUT:')
                    display_product_info(index)
                    sub_loop_flag = True
                    while (sub_loop_flag):
                        offering = input('\nLanjutkan perubahan data? (Ya/Tidak): ').lower()
                        if offering == 'ya':
                            sub2_loop_flag = True
                            while(sub2_loop_flag):
                                kolom_input = input('Masukkan kolom yang ingin Anda ubah (SKU/kategori/produk): ').lower()
                                kolom_list = list(product_stock[0].keys())
                                if kolom_input in kolom_list[:3]:
                                    while(True):
                                        value = input(f'\nSilakan melakukan perubahan informasi nama {kolom_input} pada produk "{(product_stock[index]["produk"])}": ').title()
                                        value_terdaftar = sum([[i['sku'], i['produk']] for i in product_stock], [])
                                        max_length = {'sku': 7, 'kategori': 14, 'produk': 14}
                                        min_length = {'sku': 4, 'kategori': 7, 'produk': 7}
                                        if (len(value) > max_length[kolom_input]) or (len(value) < min_length[kolom_input]):
                                            print(f'\n"JUMLAH KARAKTER PADA KOLOM "{kolom_input.upper()}" HARUS LEBIH DARI {min_length[kolom_input]} DAN KURANG DARI {max_length[kolom_input]} KARAKTER!"\n')
                                            sub2_loop_flag = False
                                            sub_loop_flag = False
                                            main_loop_flag = False
                                            break
                                        elif value in value_terdaftar:
                                            print('\n"DATA SKU DAN PRODUK HARUS UNIK. SILAKAN MASUKKAN DATA LAIN UNTUK MENGHINDARI DUPLIKASI!"')
                                            break
                                        else:
                                            offering = input(f'\nApakah Anda ingin menyimpan informasi yang telah diupdate? (Ya/Tidak): ').lower()
                                            if offering == 'ya':
                                                product_stock[index][kolom_input] = value
                                                print('\nINFORMASI PRODUK BERHASIL DIUBAH:')
                                                display_product_info(index)
                                                sub2_loop_flag = False
                                                sub_loop_flag = False
                                                main_loop_flag = False
                                                break
                                            else:
                                                print('\nPERUBAHAN INFORMASI PRODUK DIBATALKAN!')
                                                sub2_loop_flag = False
                                                sub_loop_flag = False
                                                main_loop_flag = False
                                                break
                                elif kolom_input == kolom_list[3]:
                                    print(notif_stok)
                                    sub_loop_flag = False
                                    main_loop_flag = False
                                    break
                                elif kolom_input == kolom_list[4]:
                                    print(notif_cogs)
                                    sub_loop_flag = False
                                    main_loop_flag = False
                                    break
                                else:
                                    print('\n"KOLOM TIDAK DITEMUKAN. SILAKAN HANYA MASUKKAN KOLOM (SKU/kategori/produk)"\n')
                                    sub_loop_flag = False
                                    main_loop_flag = False
                                    break
                        elif offering == 'tidak':
                            print('\n"INFORMASI PRODUK BATAL DIUBAH!"')
                            main_loop_flag = False
                            break
                        else:
                            print('\nHanya masukkan (Ya/Tidak)!')
                            continue
                else:
                    print('\nSKU TIDAK DITEMUKAN.\nSILAKAN CEK SKU PADA DAFTAR PRODUK DAN COBA LAGI!')
                    break
        elif menu == '3':
            break
        else:
            menu_tidakValid()


def hapus_produk():
    global product_stock
    while(True):
        menu = input('''
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~

Submenu "Hapus Produk":
1. Tampilkan daftar stok
2. Pilih sku yang ingin dihapus
3. Kembali ke menu utama
Silakan pilih sub menu Anda: ''')
        if menu == '1':
            daftarProduct()
        elif menu == '2':
            sku = input('\nMasukkan sku yang ingin dihapus: ').title()
            sku_list = [i['sku'] for i in product_stock]
            if sku not in sku_list:
                print('\n"SKU TIDAK DITEMUKAN. SILAKAN INPUT SKU SESUAI DAFTAR PRODUK!"')
            elif sku in sku_list:
                index = sku_list.index(sku)
                print(f'\nANDA INGIN MENGHAPUS PRODUK BERIKUT:')
                display_product_info(index)
                while(True):
                    penghapusan = input('Lanjutkan penghapusan data? (Hapus/Batal): ').lower()
                    if penghapusan == 'hapus':
                        product_stock = [item for item in product_stock if item['sku'] != sku]
                        print(f'\nSKU "{sku.upper()}" BERHASIL DIHAPUS!')
                        break
                    elif penghapusan == 'batal':
                        print(f'\nPENGHAPUSAN SKU DIBATALKAN!')
                        break
                    else:
                        print(f'\nHanya masukkan (Hapus/Batal)\n')
                        continue
        elif menu == '3':
            break
        else:
            menu_tidakValid()


# FUNCTION MENU 2: SALES
def menu_sales():
    return input('''
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~

Daftar Menu:
1. Lihat Daftar Produk
2. Input Penjualan
3. Laporan Penjualan
4. Kembali
Silakan pilih menu Anda: ''')

def daftarProduk_untukJual():
    global product_stock
    while(True):
        menu = input('''
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~

Submenu 'Lihat Daftar Produk':
1. Tampilkan semua produk
2. Filter berdasarkan kategori
3. Urutkan data tertentu (A-Z)
4. Kembali
Silakan pilih submenu Anda: ''')
        if menu == '1':
            productForSale()
        elif menu == '2':
            kategori = input('\nMasukkan kategori yang ingin dilihat:').lower()
            kategori_list = [i['kategori'] for i in product_stock]
            if kategori not in kategori_list:
                print('\n"KATEGORI TIDAK DITEMUKAN. SILAKAN PERIKSA KEMBALI KATEGORI PRODUK YANG TERSEDIA!"\n')
            elif kategori in kategori_list:
                print('\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
                print('\n\t\tDAFTAR STOK UNTUK PENJUALAN')
                print('SKU\t KATEGORI\t PRODUK\t\t STOK\t HARGA JUAL MINIMAL\n-------------------------------------------------------------')
                for i in product_stock:
                    if i['kategori'] == kategori:
                        print('{}\t {}\t {}\t {}\t {}'.format(i['sku'],
                                                              i['kategori'],
                                                              i['produk'],
                                                              i['stok'],
                                                              format_rupiah(i['cogs']+i['cogs']*min_margin+i['cogs']*tax+i['cogs']*commission+shipping_cost)))
        elif menu == '3':
            column_data = input('\nPilih kolom yang ingin Anda urutkan: ').lower()
            list_column = list(product_stock[0].keys())
            if column_data in list_column[:4]:
                product_stock = urutkan(column_data, product_stock, False)
                productForSale()
            elif column_data == 'harga jual minimal':
                product_stock = urutkan('cogs', product_stock, False)
                productForSale()
            else:
                print('\n"KOLOM DATA TIDAK DITEMUKAN. SILAKAN PERIKSA DAFTAR KOLOM!"')
        elif menu == '4':
            break
        else:
            menu_tidakValid()

def input_penjualan():
    global penjualan
    main_loop_flag = True
    while(main_loop_flag):
        trx_numb = no_trx()
        tanggal = input_tanggal()
        sub_loop_flag = True
        while sub_loop_flag:
            sku = input('Masukkan sku terjual: ').title()
            sku_list = [i['sku'] for i in product_stock]
            if sku not in sku_list:
                print('\n"SKU TIDAK DITEMUKAN. SILAKAN PERIKSA DAFTAR SKU DAN COBA LAGI!"')
                sub_loop_flag = False
                main_loop_flag = False
                break
            elif sku in sku_list:
                index = sku_list.index(sku)
                print(f'\nAnda ingin MENJUAL produk berikut:')
                print('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n')
                print('SKU\t KATEGORI\t PRODUK\t\t STOK\t HARGA JUAL MINIMAL')
                data_index = product_stock[index]
                produk = product_stock[index]['produk']
                cogs = product_stock[index]['cogs']
                print('{}\t {}\t {}\t {}\t {}'.format(data_index['sku'],
                                                        data_index['kategori'],
                                                        data_index['produk'],
                                                        data_index['stok'],
                                                        format_rupiah(data_index['cogs']+data_index['cogs']*min_margin+data_index['cogs']*tax+data_index['cogs']*commission+shipping_cost)))           
                print('\nNOTE: PASTIKAN ANDA MENJUAL DENGAN ATAU DI ATAS "HARGA JUAL MINIMAL"!')
                print('\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
                sub2_loop_flag = True
                while(sub2_loop_flag):
                    sales = input('\nMasukkan quantity terjual: ')
                    harga_jual = input('Masukkan harga jual: ')
                    harga_jual_barang = product_stock[index]['cogs']+product_stock[index]['cogs']*min_margin+product_stock[index]['cogs']*tax+product_stock[index]['cogs']*commission+shipping_cost
                    try:
                        sales = int(sales)
                        harga_jual = int(harga_jual)
                        if(sales > product_stock[index]['stok']):
                            print('\n"STOK TIDAK MENCUKUPI,\nSILAKAN AJUKAN PERMOHONAN "PURCHASING" ATAU INPUT PENJUALAN SESUAI STOK YANG TERSEDIA!"')
                            sub3_loop_flag = True
                            while(sub3_loop_flag):
                                offering = input('\nIngin menginput quantity penjualan kembali? (Ya/Tidak): ').lower()
                                if offering == 'ya':
                                    sub3_loop_flag = False
                                    continue
                                elif offering == 'tidak':
                                    print('\n"PENCATATAN PENJUALAN DIBATALKAN!"')
                                    sub3_loop_flag = False
                                    sub2_loop_flag = False
                                    sub_loop_flag = False
                                    main_loop_flag = False
                                    break
                                else:
                                    print(f'\nHanya masukkan (Ya/Tidak)')
                                    continue
                        elif (sales <= 0) and (harga_jual <= 0):
                            print('\n"QUANTITY DAN HARGA JUAL TIDAK BOLEH KURANG DARI ATAU SAMA DENGAN 0.\nSILAKAN MASUKKAN INFORMASI SESUAI KETENTUAN!"')
                            continue
                        elif(harga_jual < harga_jual_barang):
                            print('\nPENJUALAN ANDA BERPOTENSI RUGI. SILAKAN JUAL DENGAN ATAU DI ATAS "HARGA JUAL MINIMAL"!')

                        else:
                            print(f'\nBerikut informasi penjualan yang ingin Anda catatkan:')
                            print('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n')
                            print('NO.TRX\t TANGGAL\t PRODUK\t\t QTY\t HARGA JUAL\t TOTAL PENJUALAN')
                            print(f'{trx_numb}\t {tanggal}\t {product_stock[index]["produk"]}\t {sales}\t {format_rupiah(harga_jual)}\t {format_rupiah(sales*harga_jual)}')           
                            print('\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
                            while(True):
                                offering = input('Apakah Anda ingin menyimpan penjualan ke dalam sistem? (Ya\Tidak): ').lower()
                                if offering == 'ya':
                                    penjualan.append({'trx_no':trx_numb,
                                                        'tanggal':str(tanggal),
                                                        'produk':produk,    
                                                        'sales':sales,
                                                        'cogs':cogs,
                                                        'harga_jual':harga_jual,
                                                        'total':sales*harga_jual})
                                    for j in range(len(product_stock)):
                                        if(product_stock[j]['sku'] == sku):
                                            product_stock[j]['stok'] -= sales
                                    print('\n"PENJUALAN BERHASIL DIREKAM, DAN STOK TELAH DIKURANGKAN DARI DAFTAR STOK!"')
                                    sub2_loop_flag = False
                                    sub_loop_flag = False
                                    main_loop_flag = False
                                    break
                                elif offering == 'tidak':
                                    print('\n"PENJUALAN BATAL DIREKAM!"')
                                    sub2_loop_flag = False
                                    sub_loop_flag = False
                                    main_loop_flag = False
                                    break
                                else:
                                    print(f'\nHanya masukkan (Ya\Tidak)\n')
                                    continue
                            
                    except ValueError:
                        print('\n"SILAKAN INPUT HANYA ANGKA DAN HARUS LEBIH DARI 0 PADA INFORMASI QTY DAN HARGA JUAL!"')
                        continue

def laporan_penjualan():
    main_loop_flag = True
    while(main_loop_flag):
        menu = input('''
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~

Submenu 'Lihat Daftar Produk':
1. Lihat Semua Catatan Penjualan
2. Laporan Penjualan Harian
3. Laporan Penjualan Produk
4. Kembali
Silakan pilih submenu Anda: ''')
        if menu == '1':
            print('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
            print('\n\t\t\tLAPORAN PENJUALAN')
            print('NO.TRX\t TANGGAL\t PRODUK\t\t QTY\t HARGA JUAL\t TOTAL PENJUALAN\n-------------------------------------------------------------------------------')
            for i in penjualan:
                print(f"{i['trx_no']}\t {i['tanggal']}\t {i['produk']}\t {i['sales']}\t {format_rupiah(i['harga_jual'])}\t {format_rupiah(i['total'])}")
        elif menu == '2':
            sales_harian = {}
            for item in penjualan:
                tanggal = item['tanggal']
                sales = item['sales']
                total = item['total']
                if tanggal in sales_harian:
                    sales_harian[tanggal]['sales'] += sales
                    sales_harian[tanggal]['total'] += total
                else:
                    sales_harian[tanggal] = {'tanggal':tanggal, 'sales':sales, 'total':total}
            sales_harian =  list(sales_harian.values())
            print('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
            print('\n\tLAPORAN PENJUALAN HARIAN')
            print('TANGGAL\t\t QTY\t TOTAL PENJUALAN\n-----------------------------------------')
            for i in urutkan('tanggal', sales_harian, False):
                print(f"{i['tanggal']}\t {i['sales']}\t {format_rupiah(i['total'])}")

        elif menu == '3':
            sales_product = {}
            for item in penjualan:
                produk = item['produk']
                sales = item['sales']
                total = item['total']
                if produk in sales_product:
                    sales_product[produk]['sales'] += sales
                    sales_product[produk]['total'] += total
                else:
                    sales_product[produk] = {'produk':produk, 'sales':sales, 'total':total}
            sales_product =  list(sales_product.values())
            print('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
            print('\n\tLAPORAN PENJUALAN PRODUK')
            print('TANGGAL\t\t QTY\t TOTAL PENJUALAN\n-----------------------------------------')
            for i in sales_product:
                print(f"{i['produk']}\t {i['sales']}\t {format_rupiah(i['total'])}")
            print('\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
            sub_loop_flag = True
            while(sub_loop_flag):
                offering = input('Apakah Anda ingin melihat data berdasarkan urutan? (Ya/Tidak): ').lower()
                if(offering == 'ya'):
                    sub2_loop_flag = True
                    while(sub2_loop_flag):
                        offering_2 = input('Urutkan data berdasarkan (Sales/Total): ').lower()
                        if(offering_2 == 'sales'):
                            print('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
                            print('\n\tLAPORAN PENJUALAN HARIAN')
                            print('TANGGAL\t\t QTY\t TOTAL PENJUALAN\n-----------------------------------------')
                            for i in urutkan('sales', sales_product, True):
                                print(f"{i['produk']}\t {i['sales']}\t {format_rupiah(i['total'])}")
                            print('\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
                            main_loop_flag = False
                            sub_loop_flag = False
                            sub2_loop_flag = False
                            break
                        elif(offering_2 == 'total'):
                            print('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
                            print('\n\tLAPORAN PENJUALAN PRODUK')
                            print('TANGGAL\t\t QTY\t TOTAL PENJUALAN\n-----------------------------------------')
                            for i in urutkan('total', sales_product, True):
                                print(f"{i['produk']}\t {i['sales']}\t {format_rupiah(i['total'])}")
                            print('\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
                            main_loop_flag = False
                            sub_loop_flag = False
                            sub2_loop_flag = False
                            break
                        else:
                            print(f'\nHanya masukkan (Sales\Total)\n')
                            continue
                elif(offering == 'tidak'):
                    break
                else:
                    print(f'\nHanya masukkan (Ya\Tidak)\n')
                    continue
        elif menu == '4':
            break
        else:
            menu_tidakValid()


# FUNCTION MENU 3: FINANCE
def menu_finance():
    return input('''
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~

Daftar Menu:
1. Laporan Penjualan Harian
2. Laporan Keuangan
3. Kembali
Silakan pilih menu Anda: ''')

def daily_report():
    sales_harian = {}
    for item in penjualan:
        tanggal = item['tanggal']
        gmv_total = item['total']
        cogs_total = item['cogs']*item['sales']
        shipping_total = item['sales']*shipping_cost
        if tanggal in sales_harian:
            sales_harian[tanggal]['gmv'] += gmv_total
            sales_harian[tanggal]['cogs'] += cogs_total
            sales_harian[tanggal]['shipping_cost'] += shipping_total
        else:
            sales_harian[tanggal] = {'tanggal':tanggal, 'gmv':gmv_total, 'cogs':cogs_total, 'shipping_cost':shipping_total}
    sales_harian =  list(sales_harian.values())
    print('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
    print('\n\t\tLAPORAN MARGIN HARIAN')
    print('TANGGAL\t\t PENJUALAN\t     MARGIN\t MARGIN(%)\n-----------------------------------------------------------')
    for i in urutkan('tanggal', sales_harian, False):
        margin = i['gmv']-i['cogs']-i['cogs']*tax-i['cogs']*commission-i['shipping_cost']
        print(f"{i['tanggal']}\t {format_rupiah(i['gmv'])}\t {format_rupiah(margin)}\t {round(margin/i['gmv']*100,2)}%")

def finance_report():
    global penjualan
    global shipping_cost
    global tax
    global commission
    global product_stock
    try:
        revenue = sum(i['total'] for i in penjualan)
        sales = sum(i['sales'] for i in penjualan)
        cogs_total = sum(j['sales']*i['cogs'] for i in product_stock for j in penjualan if i['produk'] == j['produk'])
        # BIAYA-BIAYA (COST)
        shipping_actual = int(shipping_cost*sales)
        commission_actual = int(revenue*commission)
        tax_actual = int(revenue*tax)
        total_cost = shipping_actual+commission_actual+tax_actual
        margin_percentage = round((revenue-cogs_total-total_cost)/revenue*100,1) if revenue != 0 else 0
    except ValueError:
        revenue, sales, cogs_total, shipping_actual, commission_actual, tax_actual, total_cost, margin_percentage = 0,0,0,0,0,0,0,0
    print(str('* ~ * '*8).center(70))
    print(f'''
                        {print_bold('INCOME STATEMENT')}
                
            Revenue:
            > Sales         {format_rupiah(revenue)}
                Total                   {format_rupiah(revenue)}

            > COGS                      {format_rupiah(cogs_total)}
                
            Expenses:
            > Shipping Cost {format_rupiah(shipping_actual)}
            > Commission    {format_rupiah(commission_actual)}
            > Tax           {format_rupiah(tax_actual)}
                Total                   {format_rupiah(total_cost)}
                                        --------
            Net Sales/Margin            {print_bold(str(format_rupiah(revenue-cogs_total-total_cost)))}
            margin percentage           {print_bold(str(margin_percentage))}%

            ''')
    print(str('* ~ * '*8).center(70))


# FUNCTION MENU 4: PURCHASE
def menu_purchase():
    return input('''
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~

Daftar Menu:
1. Filter stok
2. Kembali
Silakan pilih menu Anda: ''')

def filter_stokPurchase():
    global product_stock
    daftarProduct()
    main_loop_flag = True
    while(main_loop_flag):
        offering = input('\nApakah ingin melakukan filter stok? (Ya/Tidak): ').lower()
        if(offering=='ya'):
            while(True):
                batas_filter = input('Perlihatkan stok berjumlah di bawah (pcs): ')
                try:
                    batas_filter = int(batas_filter)
                    print('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
                    print('\n\t\t\tDAFTAR STOK')
                    print('SKU\t KATEGORI\t PRODUK\t\t STOK\t COGS\n-----------------------------------------------------------')
                    for i in product_stock:
                        if i['stok'] < batas_filter:
                            print('{}\t {}\t {}\t {}\t {}'.format(i['sku'],i['kategori'],i['produk'],i['stok'],format_rupiah(i['cogs'])))
                    main_loop_flag = False
                    break
                except ValueError:
                    print('\n"Silakan masukkan hanya angka!\n"')
                    continue
        elif(offering=='tidak'):
            break
        else:
            print(f'\nHanya masukkan (Ya\Tidak)')
            continue


# ----------------------------------------------------------------------------------------------------------------


# APLIKASI UNTUK OPERASIONAL PERUSAHAAN DAGANG
# DENGAN PERKIRAAN MEMILIKI 4 DIVISI (WAREHOUSE, SALES, FINANCE, PURCHASE)
while(True):
    position = menu_position()
    
# MENU 1: WAREHOUSE
    if(position=='1') and (pass_staff(position) == input_pass()):
        salam(position)
        while(True):
            menu = menu_warehouse()
            if(menu=='1')  : tampilkan_daftarProduk()
            elif(menu=='2'): tambah_stok()
            elif(menu=='3'): tambah_produk()
            elif(menu=='4'): edit_informasiProduk()
            elif(menu=='5'): hapus_produk()
            elif(menu=='6'): break
            else: menu_tidakValid()

# MENU 2: SALES
    elif(position=='2') and (pass_staff(position) == input_pass()):
        salam(position)
        while(True):
            menu = menu_sales()
            if(menu=='1'): daftarProduk_untukJual()
            elif(menu=='2'): input_penjualan()
            elif(menu=='3'): laporan_penjualan()
            elif(menu=='4'): break
            else: menu_tidakValid()

# MENU 3: FINANCE
    elif(position=='3') and (pass_staff(position) == input_pass()):
        salam(position)
        while(True):
            menu = menu_finance()
            if(menu=='1'): daily_report()
            elif(menu=='2'): finance_report()
            elif(menu=='3'): break
            else: menu_tidakValid()

# MENU 4: PURCHASE
    elif(position=='4') and (pass_staff(position) == input_pass()):
        salam(position)
        while(True):
            menu = menu_purchase()
            if(menu=='1'): filter_stokPurchase()
            elif(menu=='2'): break
            else: menu_tidakValid()

# MENU 5: EXIT
    elif(position=='5'):
        salam_penutup()
        break

# Jika input tidak sesuai daftar menu
    else:
        print('\n"POSISI ATAU PASSWORD TIDAK VALID. SILAKAN LOGIN KEMBALI!"')