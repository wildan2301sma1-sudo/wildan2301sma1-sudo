# definisikan kelas dasar vehicle 
class vehicle:
    def __init__(self, merk, tahun, warna):
        self.merk = merk
        self.tahun = warna
        self.warna = warna
        
    def tampilkan_info(self):
         print(f"Merk: {self.merk}")
         print(f"Tahun: {self.tahun}")
         print(f"Warna: {self.warna}")
         
#Definisikan kelas turunan car yang mewarisi dari vehic;e 
class car(vehicle):
    def __init__(self, merk, tahun, warna, model):
        # Panggil konstruktor kelas dasar 
        super().__init__(merk, tahun, warna)
        self.model = model
        
    def tampilkan_info(self):
        #panggil metode kelas dasar untuk menampilkan info kendaraan
        super().tampilkan_info()
        print(f"model: {self.model}")
        
#program utama 
if __name__ == "__main__":
    car = car("Toyota", 2022, "merah", "camry")
    
    print("info kendaraan:")
    car.tampilkan_info()