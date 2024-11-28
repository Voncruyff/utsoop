class Hewan:
    def suara(self):
        # Metode default yang akan di-override oleh kelas turunan
        print("Hewan mengeluarkan suara.")

class Kucing(Hewan):
    def suara(self):
        # Override metode suara() untuk Kucing
        print("Meong!")

class Anjing(Hewan):
    def suara(self):
        # Override metode suara() untuk Anjing
        print("Guk-guk!")

# Membuat objek dari masing-masing kelas
hewan1 = Hewan()
kucing1 = Kucing()
anjing1 = Anjing()

# Memanggil metode suara() dari setiap objek
hewan1.suara()   # Output: Hewan mengeluarkan suara.
kucing1.suara()  # Output: Meong!
anjing1.suara()  # Output: Guk-guk!
