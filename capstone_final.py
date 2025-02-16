# Data dibawah ini adalah data siswa penerbang di sekolah A base di Cilacap yang dapat dijelaskan sebagai berikut
# Unique ID menggunakan nama setiap siswa

# Penjelasan Variabel pada dictionary :
# nama = nama siswa itu sendiri
# status = tahapan setiap siswa yang dimulai dari SPL(Modul 1) -> PPL(Modul2) -> CPL(Modul 3)
# ground = jumlah (jam) waktu dihabiskan untuk belajar di dalam kelas
# simulator = jumlah (jam) waktu dihabiskan untuk belajar di dalam FTD(Flight Training Device) /Simulator
# flight = jumlah (jam) waktu dihabiskan untuk belajar di udara (practice)
# base = lokasi training, untuk SPL dan PPL dilakukan di Cilacap, Untuk CPL dilakukan di Semarang

from tabulate import tabulate # Tabulate untuk visual tabel data
from getpass import getpass
# Data menggunakan dict dalam list supaya mudah untuk indexing(list), dan ambil data menggunakan keys
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DICTIONARY DALAM LIST SEBAGAI DATA SET
daftarSiswa = [
     {
        'nama' : 'asep',
        'nim' : '1', 
        'status' : 'spl',
        'ground': 50,
        'simulator' : 15,
        'flight' : 25,
        'base' : 'cilacap'
    },
     {
        'nama' : 'Bambang',
        'nim' : '2', 
        'status' : 'spl',
        'ground': 30,
        'simulator' : 22,
        'flight' : 23,
        'base' : 'cilacap'
    },
     {
        'nama' : 'hanif',
        'nim' : '3', 
        'status' : 'spl',
        'ground': 54,
        'simulator' : 15,
        'flight' : 5,
        'base' : 'cilacap'
    },
    {
        'nama' : 'sarah',
         'nim' : '4', 
        'status' : 'spl',
        'ground': 25,
        'simulator' : 55,
        'flight' : 75,
        'base' : 'cilacap'
    },
     {
        'nama' : 'Ivan',
         'nim' : '56', 
        'status' : 'spl',
        'ground': 55,
        'simulator' : 54,
        'flight' : 53,
        'base' : 'cilacap'
    },
    {
        'nama' : 'siti',
        'nim' : '6', 
        'status' : 'spl',
        'ground': 55,
        'simulator' : 15,
        'flight' : 51,
        'base' : 'cilacap'
    },
    {
        'nama' : 'soleh',
         'nim' : '7', 
        'status' : 'spl',
        'ground': 23,
        'simulator' : 5,
        'flight' : 55,
        'base' : 'cilacap'
    },
    {
        'nama' : 'rizky',
        'nim' : '8', 
        'status' : 'spl',
        'ground': 66,
        'simulator' : 44,
        'flight' : 33,
        'base' : 'cilacap'
    },
     {
        'nama' : 'fatih',
        'nim' : '9', 
        'status' : 'spl',
        'ground': 35,
        'simulator' : 65,
        'flight' : 75,
        'base' : 'cilacap'
    },
     {
        'nama' : 'kio',
        'nim' : '10', 
        'status' : 'spl',
        'ground': 85,
        'simulator' : 35,
        'flight' : 65,
        'base' : 'cilacap'
    }
]
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FITUR READ

def menampilkanData() :
    print() #SUB MENAMPILKAN DATA
    print('Submenu Menampilkan Data')
    print('Aksi yang tersedia :')
    print('1. Lihat semua daftar siswa')
    print('2. cari data siswa berdasarkan NIM')
    print('3. Keluar')
    
    while True : # Handling Error
        aksiMenampiklanData = int(input("Silahkan pilih submenu yang tersedia : "))
        try : 
             aksiMenampiklanData = int(aksiMenampiklanData)
        except ValueError : #JIKA BUKAN INTEGER
             print('Maaf, masukan input angka yang tersedia pada menu')
             continue
        if 0< aksiMenampiklanData < 4: #JIKA DILUAR RANGE1-3
             break 
        else :
             print("Silahkan pilih menu 1 , 2 ataupun 3")


    if aksiMenampiklanData == 1 :#Menampilkan tabel dari list dictionary
            print('             DATA SISWA SEKOLAH PENERBANGAN A BATCH 22')
            print(tabulate(daftarSiswa, headers= 'keys', tablefmt='grid'))
            menampilkanData()
               
    elif aksiMenampiklanData == 2:
        # Menampilkan data personal
        while True: #HANDLING ERROR INPUT
            try:
                nim2 = input('Masukan NIM untuk ditampilkan : ')  # NIM PAKAI STRING SUPAYA TIDAK BISA DI HITUNG (UNIQUE CODE)
                found = False
                for siswa in daftarSiswa:
                    if siswa['nim'] == nim2: #JIKA INPUT NIM ADA, MAKA DILAKUKAN AKSI SELANJUTNNYA
                        found = True
                        personal = [siswa]  # BIKIN LIST BIAR BISA DITAMPILKAN SENDIRI
                        print('             DATA SISWA SEKOLAH PENERBANGAN A BATCH 22')
                        print(tabulate(personal, headers='keys', tablefmt='grid'))
                        break
                if not found:
                    print('Maaf, NIM yang anda masukan tidak tersedia')
                else:
                    break
            except ValueError:
                print('Maaf, NIM yang anda masukan tidak valid')
        menampilkanData()

    else:
        mainMenu() #JIKA EXIT, KEMBALI KE MAIN MENU


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FITUR CREATE

def menambahkanData():
    # Menambah data siswa ke dalam list
    print('Submenu Menambahkan Data Siswa')
    print('Silahkan pilih dari menu berikut : ')
    print('1. Menambahkan data siswa')
    print('2. Keluar')
    print()

    while True:  # Handling Error
        try:
            aksiMenambahkanData = int(input("Silahkan pilih submenu yang tersedia : "))
            if 0 < aksiMenambahkanData < 3:
                break
            else:
                print("Silahkan pilih menu 1 atau 2")
        except ValueError:
            print('Maaf, masukan input angka yang tersedia pada menu')

    if aksiMenambahkanData == 1:
        while True:
            try:
                # Input Nama MENGECEK APAKAH INPUT KOSONG ?
                nama = input('Masukan Nama: ')
                if not nama.strip():  # APAKAH INPUT KOSONG ?
                    raise ValueError("Nama tidak boleh kosong.") #raise menggantikan execpt pada while banyak input
                if not nama.replace(" ", "").isalpha():  # membolehkan input spasi jika nama lebih dari satu kalimat
                    raise ValueError("Nama harus menggunakan huruf.")

                # ada nama di daftar siswa nya ngga ?
                nama_exists = any(siswa['nama'].lower() == nama.lower() for siswa in daftarSiswa) #menghasilkan boolean pada'any',
                if nama_exists:
                    print("Error: Nama sudah ada dalam data siswa.")
                    continue  #Looping di skip kalau hasil true

                # Input NIM (harus string dan ga boleh duplikat)
                nim = input("Masukan NIM: ")
                if not nim.strip():  # mengecek apakah inputan kosng ?

                    raise ValueError("NIM tidak boleh kosong.")
                if not nim.isnumeric():  #cek NIM harus angka
                    raise ValueError("NIM harus menggunakan angka.")
               

                # Check kalau nim sudah ada di list ?
                nim_exists = any(siswa['nim'] == nim for siswa in daftarSiswa)
                if nim_exists:
                    print("Maaf, NIM sudah ada dalam data siswa.")
                    continue  # Loop back to the beginning

                # Input Status Siswa (harus SPL, PPL, or CPL)
                status = input('Masukan Status Siswa (SPL/PPL/CPL): ').upper()
                if status not in ['SPL', 'PPL', 'CPL']:
                    raise ValueError("Status siswa harus SPL, PPL, atau CPL.")

                # Input Jumlah Jam harus positif
                ground = int(input("Masukan Jumlah Jam Belajar di Kelas: "))
                if ground < 0:
                    raise ValueError("Jumlah jam belajar tidak boleh negatif.")

                 # Input Jumlah Jam harus positif
                simulator = int(input("Masukan Jumlah Jam Simulator: "))
                if simulator < 0:
                    raise ValueError("Jumlah jam simulator tidak boleh negatif.")

                 # Input Jumlah Jam harus positif
                flight = int(input("Masukan Jumlah Jam Terbang: "))
                if flight < 0:
                    raise ValueError("Jumlah jam terbang tidak boleh negatif.")

                # Input Base Ops Siswa (harus be CXP or SRG)
                base = input("Masukan Base Ops Siswa (CXP/SRG): ").upper()
                if base not in ['CXP', 'SRG']:
                    raise ValueError("Base ops siswa harus CXP atau SRG.")

                # kalau masukan sudah sesuai, akan dimasukan ke dict baru
                new_siswa = {
                    'nama': nama,
                    'nim': nim,
                    'status': status,
                    'ground': ground,
                    'simulator': simulator,
                    'flight': flight,
                    'base': base
                }
                table_data = [[key, value] for key, value in new_siswa.items()]

                    # Display the data using tabulate
                print(tabulate(table_data, headers=["field",'value'], tablefmt="pretty"))
                print()
                print()

                while True : #Handling Error

                    yakinTambah = input('Apakah anda yakin akan menambahkan data diatas ? y/n').strip().lower()

                    if yakinTambah in ['y','n'] :
                        break
                    else :
                        print('Maaf, masukan hanya opsi y dan n')
                
                if yakinTambah == 'y' :
                    daftarSiswa.append(new_siswa)
                    print("Data siswa berhasil ditambahkan!")
                    print('             DATA SISWA SEKOLAH PENERBANGAN A BATCH 22')
                    print(tabulate(daftarSiswa, headers= 'keys', tablefmt='grid'))
                    menambahkanData()
                else :
                    print ('Data tidak ditambahkan')
                    menambahkanData()
                
                
                break  # kalau udah ditambah, akan balik ke main menu

            except ValueError as e:
                print(f"Error: {e}")
                print("Silakan coba lagi.\n")

    else :
        mainMenu()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FITUR UPDATE
def mengupdateData():
    print('Selamat Datang di Program Manajemen Siswa Penerbang')
    print('Submenu Update')
    print('Silahkan pilih Menu yang tersedia : ')
    print('''
        1. Update data
        2. Update data tertentu
        3. Keluar
    ''')

    while True:  # Handling Error
        try:
            aksiMengupdateData = int(input("Silahkan pilih submenu yang tersedia : "))
            if 0 < aksiMengupdateData < 4:
                break
            else:
                print("Silahkan pilih menu 1, 2, atau 3")
        except ValueError:
            print('Maaf, masukan input angka yang tersedia pada menu')

    if aksiMengupdateData == 1:
        displayData()  # menampilkan semua data
        nim2 = get_non_empty_input('Masukan NIM siswa yang akan di update : ')  # NIM harus berupa string
        found = False
        for siswa in daftarSiswa:
            if siswa['nim'] == nim2:
                found = True
                print("Data siswa ditemukan:")
                print("\nMasukkan data baru:")
                namaUpdate = get_non_empty_input("Nama: ")
                statusUpdate = get_status_input("Status: ") #status harus ppl,cpl, atau spl
                groundUpdate = get_integer_input("Ground: ")
                simulatorUpdate = get_integer_input("Simulator: ")
                flightUpdate = get_integer_input("Flight: ")
                baseUpdate = get_non_empty_input("Base: ")

                # buat list sementara buat nampung sementara
                temp_siswa = siswa.copy()
                temp_siswa['nama'] = namaUpdate
                temp_siswa['status'] = statusUpdate
                temp_siswa['ground'] = groundUpdate
                temp_siswa['simulator'] = simulatorUpdate
                temp_siswa['flight'] = flightUpdate
                temp_siswa['base'] = baseUpdate

                # menampilkan data yang ter update
                print("\nData yang akan diupdate:")
                print(tabulate([temp_siswa.values()], headers=temp_siswa.keys(), tablefmt="pretty"))
                print()

                yakin = input('Apakah anda yakin ingin mengupdate data diatas (y/n) ? ').lower()
                while yakin not in ['y', 'n']:
                    print("Input tidak valid. Masukkan 'y' atau 'n'.")
                    yakin = input('Apakah anda yakin ingin mengupdate data diatas (y/n) ? ').lower()

                if yakin == 'y':  
                    #memasukan ke list sementara
                    siswa.update(temp_siswa)
                    print()
                    print("Data berhasil diupdate!")
                    print('             DATA SISWA SEKOLAH PENERBANGAN A BATCH 22')
                    print(tabulate(daftarSiswa, headers='keys', tablefmt='grid'))
                    mengupdateData()
                else:
                    print("Update dibatalkan. Data tidak diubah.")
                    mengupdateData()
                break

        if not found:
            print(f"Data dengan NIM {nim2} tidak ditemukan.")
            mengupdateData()
    elif aksiMengupdateData == 2:
        displayData()  #Menampilkan semua data
        nim2 = get_non_empty_input('Masukan NIM siswa yang akan di update : ')  
        found = False
        for siswa in daftarSiswa:
            if siswa['nim'] == nim2:
                found = True
                print("Data siswa ditemukan:")
                # koversi dict ke list
                listBaru = [[key, value] for key, value in siswa.items()]
         
                print(tabulate(listBaru, headers=['Attribute', 'Nilai'], tablefmt="pretty"))
                print(''' 
                    Masukan Data apa yang ingin diubah ? 
                    1. Update data Nama
                    2. Update data NIM
                    3. Update data Status
                    4. Update jam ground
                    5. Update jam Simulator
                    6. Update jam terbang
                    7. Update lokasi base training
                    8. Keluar
                ''')
                dataDiubah = get_integer_input("Pilih data yang ingin diubah: ")
                
              #menyimpan data awal jika user cancel update
                original_data = siswa.copy()
                
                if dataDiubah == 1:
                    siswa['nama'] = get_non_empty_input("Masukan nama baru: ")
                elif dataDiubah == 2:
                    siswa['nim'] = get_non_empty_input("Masukan NIM baru: ")
                elif dataDiubah == 3:
                    siswa['status'] = get_status_input("Masukan status baru: ")
                elif dataDiubah == 4:
                    siswa['ground'] = get_integer_input("Masukan jam ground baru: ")
                elif dataDiubah == 5:
                    siswa['simulator'] = get_integer_input("Masukan jam simulator baru: ")
                elif dataDiubah == 6:
                    siswa['flight'] = get_integer_input("Masukan jam terbang baru: ")
                elif dataDiubah == 7:
                    siswa['base'] = get_non_empty_input("Masukan lokasi base training baru: ")
                elif dataDiubah == 8:
                    print("Keluar dari menu update.")
                    break
                else:
                    print("Pilihan tidak valid.")
                    break
                
                # Display the updated data
                listBaru2 = [[key, value] for key, value in siswa.items()]
                print(tabulate(listBaru2, headers=['Attribute', 'Nilai'], tablefmt="pretty"))
                
                # konfirmasi
                yakin = input('Apakah anda yakin melakukan perubahan ? (y/n) : ').lower()
                while yakin not in ['y', 'n']:
                    print("Input tidak valid. Masukkan 'y' atau 'n'.")
                    yakin = input('Apakah anda yakin melakukan perubahan ? (y/n) : ').lower()

                if yakin == 'y':
                    print("Data berhasil diupdate!")
                    displayData()
                    mengupdateData()  
                else:
                    # balikin ubahan kalau user tiba tiba cancel
                    siswa.update(original_data)
                    print("Update dibatalkan. Data tidak diubah.")
                    mengupdateData()
                
                break
        
        if not found:
            print("Data siswa dengan NIM tersebut tidak ditemukan.")
            mengupdateData()

    elif aksiMengupdateData == 3:
        print("Keluar dari menu update.")
        mainMenu()
        return


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FITUR DELETE

def menghapusData():
    print('Submenu menghapus data siswa')
    print()
    print('Silahkan pilih Menu yang tersedia : ')
    print('''
        1. hapus data sesuai NIM
        2. keluar
    ''')

    while True:  # Handling Error
        try:
            aksiMenghapusData = int(input("Silahkan pilih submenu yang tersedia : "))
            if 0 < aksiMenghapusData < 3:
                break
            else:
                print("Silahkan pilih menu 1 atau 2")
        except ValueError:
            print('Maaf, masukan input angka yang tersedia pada menu')

    if aksiMenghapusData == 1:
        displayData()  # tampilkan data utk referensi
        while True:
            try:
                nim2 = input('Masukan NIM untuk ditampilkan : ')  # NIM dalam str
                found = False
                for index, siswa in enumerate(daftarSiswa):
                    if siswa['nim'] == nim2:
                        found = True
                        personal = [siswa]  # mengambil data dari nim ke list sementara
                        print('             DATA SISWA SEKOLAH PENERBANGAN A BATCH 22')
                        print(tabulate(personal, headers='keys', tablefmt='grid'))
                        print()
                        yakin = input('Apakah anda yakin ingin menghapus data diatas (y/n) ? ')

                        if yakin.lower() == 'y':  # Check if yakin is 'y' or 'Y'
                            daftarSiswa.pop(index)  #menghapus menggunakan index
                            print("Data berhasil dihapus!")
                            displayData()  # Display updated data
                            menghapusData()
                            break
                        else:
                            menghapusData()
                            break
                if not found:
                    print('Maaf, NIM yang anda masukan tidak tersedia')
                    menghapusData()
                else:
                    break
            except ValueError:
                print('Maaf, NIM yang anda masukan tidak valid')
                menghapusData()
    else :
        mainMenu()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FITUR ESTIMASI BIAYA

def menghitungData():
    while True:
        print()
        print('Submenu Estimasi Pengeluaran')
        print('Aksi yang tersedia :')
        print('1. Cek estimasi pengeluaran')
        print('2. Keluar')

        try:
            aksiHitung = int(input("Silahkan pilih submenu yang tersedia : "))
            if aksiHitung == 1:
                while True:
                    nim2 = input('Masukan NIM untuk dihitung : ')
                    found = False
                    for siswa in daftarSiswa:
                        if siswa['nim'] == nim2:
                            found = True
                            print('             DATA SISWA SEKOLAH PENERBANGAN A BATCH 22')
                            print(tabulate([siswa], headers='keys', tablefmt='grid'))
                            print()
                            print('Estimasi Pengeluaran siswa/i dengan nama', siswa['nama'],':')
                            groundppl = 80 - siswa['ground']
                            simppl = 5 - siswa['simulator']
                            flightppl = 40 - siswa['flight'] 
                            print('Untuk mendapatkan sertifikasi PPL, ', siswa['nama'],'harus menyelesaikan',groundppl,'jam kelas,',simppl,'jam simulator dan', flightppl,'jam terbang')
                            costground = groundppl * 10
                            costsim = simppl * 100
                            costflight = flightppl * 250
                            costtotal = costground +costsim +costflight
                            print('Dengan estimasi biaya total sekitar $', costtotal)
                            print()
                            print()
                            groundcpl = 80 - siswa['ground']
                            simcpl = 10 - siswa['simulator']
                            flightcpl = 150 - siswa['flight'] 
                            print('Untuk mendapatkan sertifikasi CPL, ', siswa['nama'],'harus menyelesaikan',groundcpl,'jam kelas,',simcpl,'jam simulator dan', flightcpl,'jam terbang')
                            costground = groundcpl * 10
                            costsim = simcpl * 100
                            costflight = flightcpl * 250
                            costtotal = costground +costsim +costflight
                            print('Dengan estimasi biaya total sekitar $', costtotal)
                            menghitungData()


                    
                            break

                    if not found:
                        print('Maaf, NIM yang anda masukan tidak tersedia')
                        menghitungData()
                    else:
                        menghitungData()
                        break
            elif aksiHitung == 2:
                mainMenu()
                break
            else:
                print("Silahkan pilih menu 1 atau 2")
        except ValueError:
            print('Maaf, masukan input angka yang tersedia pada menu')
            menghitungData()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FITUR MAIN MENU

def mainMenu() : 
    print('Selamat Datang di Program Manajemen Siswa Penerbang')
    print()
    print('Silahkan pilih Menu yang tersedia : ')
    print('''
        1. Tampilkan semua data siswa
        2. Menambahkan data siswa
        3. Mengupdate Data Siswa
        4. Menghapus Data Siswa
        5. Estimasi Biaya Pelatihan
        6. Keluar
        ''')
    
    while True:  # Handling Error
        try:
            aksiMainMenu = int(input("Silahkan pilih submenu yang tersedia : "))
            if 0 < aksiMainMenu < 7:
                break
            else:
                print("Silahkan pilih menu 1 atau 2")
        except ValueError:
            print('Maaf, masukan input angka yang tersedia pada menu')
    
    if aksiMainMenu == 1:
        menampilkanData()
    elif aksiMainMenu == 2 :
        menambahkanData()
    elif aksiMainMenu == 3 :
        mengupdateData() 
    elif aksiMainMenu == 4 :
        menghapusData()
    elif aksiMainMenu == 5 :
        menghitungData() 
    else :
        print('Terima kasih telah menggunakan program manajemen siswa penerbang')
     

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FITUR MENUNJUKAN DATA
def displayData():
    # Convert list of dictionaries to a list of lists for tabulate
    table_data = [[siswa['nama'], siswa['nim'], siswa['status'], siswa['ground'], siswa['simulator'], siswa['flight'], siswa['base']] for siswa in daftarSiswa]
    headers = ["Nama", "NIM", "Status", "Ground", "Simulator", "Flight", "Base"]
    print(tabulate(table_data, headers=headers, tablefmt="pretty"))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FITUR HANDLING ERROR INPUT
# Kalau Input angka
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FITUR HANDLING ERROR INPUT
# Kalau Input alphabet
def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input tidak boleh kosong. Silakan coba lagi.")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FITUR HANDLING ERROR INPUT
# Kalau Input STATUS CPL PPL SPL
def get_status_input(prompt) :
    while True:
        try :
            return (input(prompt)) == 'PPL' or 'CPL' or 'SPL' 
        except ValueError :
            print("Masukan tidak sesuai, mohon dicek kembali masukan anda")






import getpass

def masuk():
    
    username1 = 'admin'
    password1 = 'purwadhika'

    print('SISTEM MANAJEMEN JAM TERBANG SISWA PENERBANG')
    kesempatan = 3

    while kesempatan > 0:
        username2 = input('Masukan Username Anda: ')
        password2 = getpass.getpass('Masukan Password Anda (password disembunyikan): ')

        if username1 == username2 and password1 == password2:
            print('LOGIN BERHASIL! SELAMAT DATANG')
            mainMenu()  
            return True  
        else:
            print('Maaf, username atau password Anda salah. Silakan coba lagi.')
            kesempatan -= 1
            print('Kesempatan Login sisa', kesempatan, 'kali')

    print("Anda telah melebihi batas percobaan login. Silakan coba lagi nanti.")
    return False 

# eksekusi disini
masuk()



    





































# Main Menu --> Daftar perintah yang tersedia
def mainMenu() : 
    print('Selamat Datang di Program Manajemen Siswa Penerbang')
    print()
    print('Silahkan pilih Menu yang tersedia : ')
    print('''
        1. Tampilkan semua data siswa
        2. Menambahkan data siswa
        3. Menghapus data siswa
        4. Mengupdate Data Siswa
        5. Exit
        ''')


#