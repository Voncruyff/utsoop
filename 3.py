class Laptop:
    def __init__(self, merk, ram, processor):
        # Constructor untuk menginisialisasi atribut
        self.merk = merk
        self.ram = ram
        self.processor = processor
        print(f"Laptop {self.merk} dengan {self.ram}GB RAM dan processor {self.processor} telah dibuat.")
    
    def __del__(self):
        # Destructor untuk mencetak pesan ketika objek dihancurkan
        print(f"Objek Laptop {self.merk} dihancurkan.")

# Membuat objek Laptop
laptop1 = Laptop("Dell", 8, "Intel i7")

# Menghancurkan objek
del laptop1
