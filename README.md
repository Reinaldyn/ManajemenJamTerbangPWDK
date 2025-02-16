# ManajemenJamTerbangPWDK
Capstone Project 1
Readme  : Manajemen Jam Terbang Siswa Sekolah Penerbangan
Adalah suatu program sederhana untuk mencatat total jam terbang / jam kelas pada sebuah flying school yang sangat diperlukan oleh seorang scheduler 
1.	Fitur Menampilkan Data
Data pada Manajemen JamTerbang Siswa Sekolah Penerbangan meliputi,
-	Nama : Nama Panjang dari siswa
-	NIM : Nomor induk siswa yang tidak bisa terduplikat
-	Status : SPL (Student Pilot Licensed), PPL (Private Pilot Licensed), dan CPL (Commercial Pilot Licensed)
-	Ground : Jam terpakai digunakan untuk belajar di kelas
-	Simulator : Jam terpakai untuk belajar di FTD (Flight Training Device)
-	Flight : Jam terpakai untuk Latihan terbang
Data diatas bisa ditampilkan secara keseluruhan, ataupun dicari berdasarkan NIM.

2.	Fitur Menambah Data
Semua data yang sudah ditampilkan pada fitur menampilkan data, dapat ditambah dengan fitur menambahkan data dengan format sesuai table siswa yang tertampil.

3.	Fitur Mengubah Data
Semua Data yang tertampil dapat diubah sebagai penyesuaian data agar tetap valid, perubahan dapat diilakukan sekaligus maupun terpisah.

4.	Fitur Menghapus Data
Data yang ditampilkan dapat dihapus dengan memasukan NIM sebagai unique key.

5.	Fitur Estimasi Pengeluaran
Dalam studi pada sekolah penerbangan, factor biaya adalah hal paling krusial selain skill dan pengetahuan. Program ini ditujukan untuk melakukan estimasi biaya yang akan dikeluarkan para siswa menuju ke kelulusan atau final exam dengan logic journey sebagai berikut,

NO MIN REQUIRED  GET SPL LICENSED

GROUND CLASS (80 HRS)  SIMULATOR (5 HRS)  FLIGHT HOUR (40 HRS)  GET PPL LICENSED

SIMULATOR (10 HRS)  FLIGHT HOUR (150 HRS)  GET CPL LICENSED

Detail Biaya yang harus dikeluar kan :
-	Ground Class = $10/Jam
-	Simulator = $100/Jam
-	Flight Hour = $250/Jam
Sehingga dari semua ketentuan diatas, siswa bisa memperkirakan berapa biaya yang diperlukan untuk mencapai target kelulusan


