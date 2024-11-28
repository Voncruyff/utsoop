class Mahasiswa:
    def __init__(self, nama, nim, program_studi):
        # Menginisialisasi atribut objek
        self.nama = nama
        self.nim = nim
        self.program_studi = program_studi

    def tampilkan_info(self):
        # Menampilkan informasi mahasiswa
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Program Studi: {self.program_studi}")

# Input data dari pengguna
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
program_studi = input("Masukkan Program Studi: ")

# Membuat objek Mahasiswa dengan data yang dimasukkan
mahasiswa = Mahasiswa(nama, nim, program_studi)

# Menampilkan informasi mahasiswa
mahasiswa.tampilkan_info()
