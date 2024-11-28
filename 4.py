class AkunBank:
    def __init__(self, nomorRekening, saldo):
        # Constructor untuk menginisialisasi atribut
        self.nomorRekening = nomorRekening
        self.__saldo = saldo  # Atribut saldo dibuat private

    # Getter untuk saldo
    def get_saldo(self):
        return self.__saldo

    # Setter untuk saldo
    def set_saldo(self, saldo_baru):
        if saldo_baru >= 0:
            self.__saldo = saldo_baru
        else:
            print("Saldo tidak boleh negatif!")

    # Metode untuk menambahkan saldo
    def tambah_saldo(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Saldo berhasil ditambahkan. Saldo saat ini: {self.__saldo}")
        else:
            print("Jumlah yang ditambahkan harus lebih dari 0!")

    # Metode untuk menarik saldo
    def tarik_saldo(self, jumlah):
        if jumlah > 0 and jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Saldo berhasil ditarik. Saldo saat ini: {self.__saldo}")
        elif jumlah > self.__saldo:
            print("Saldo tidak mencukupi!")
        else:
            print("Jumlah yang ditarik harus lebih dari 0!")

# Contoh penggunaan
akun = AkunBank("1234567890", 100000.0)

# Menampilkan saldo awal
print(f"Saldo awal: {akun.get_saldo()}")

# Menambahkan saldo
akun.tambah_saldo(50000)

# Menarik saldo
akun.tarik_saldo(30000)

# Mengatur saldo baru secara langsung
akun.set_saldo(200000)
print(f"Saldo baru: {akun.get_saldo()}")
