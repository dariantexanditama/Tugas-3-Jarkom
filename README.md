# Tugas-3-Jarkom

Kelompok I1

Anggota:

- Darian Texanditama (1806205275)
- Faza Aulia Aryoga (1806173525)
- Ahmad Haulian Yoga Pratama (1806133824)

## Persiapan
1. Edit security group untuk instance yang ingin digunakan di Amazon AWS
2. Pilih Edit inbound rules
3. Pilih type "All TCP", sisanya default settings
4. Simpan pengaturan

## Memulai program
### Sisi worker
1. Connect ke VM EC2 dengan PuTTY. IP address yang digunakan adalah public IPv4 address dari instance EC2. Jangan lupa pakai file key .ppk
2. Setelah itu install python di instance EC2 dengan command sudo yum install python3
3. Setelah itu buka text editor nano di instance EC2 dengan command nano
4. Copy paste script worker.py ke dalam text editornya
5. Ctrl + O untuk me-write filenya dengan nama worker.py
6. Jalankan file pythonnya dengan command python3 worker.py [Private IP address EC2] [Port]
Scriptnya akan me-listen untuk koneksi dari master

### Sisi master tanpa script
1. Connect ke VM EC2 dengan PuTTY. IP address yang diisi adalah public IPv4 address milik instance EC2. Tidak perlu mengisi ec2-user sebelum IP address.
Port sama dengan port yang digunakan untuk script worker
2. Pilih setting Raw. Tidak perlu menggunakan file private key .ppk untuk log in ke EC2
3. Worker akan meminta autentikasi
4. Jika autentikasi sukses maka kita sudah bisa mengirim job
5. Masukan perintah Exit untuk menutup koneksi

### Sisi master dengan script
1. Jalankan script master.py dengan argumen python master.py [IP worker] [Port worker]
2. Worker akan meminta autentikasi
3. Jika autentikasi sukses maka kita sudah bisa mengirim job
4. Masukan perintah Exit untuk menutup koneksi
