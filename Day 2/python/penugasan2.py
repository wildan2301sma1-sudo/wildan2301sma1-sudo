# Definisikan kelas Contact 
class Contact:
    def __init__(self, nama, nomor_telepon, email):
        self.nama = nama 
        self.nomor_telepon = nomor_telepon 
        self.email = email 
        
    def tampilkan_info(self):
        print(f"nama: {self.nama}")
        print(f"nomor telepon: {self.nomor_telepon}")
        print(f"email: {self.email}")
        print()
        
# Definisikan kelas addressbook untuk mengelola daftar kontak 
class AddressBook:
    def __init__(self):
        self.daftar_kontak = []
         
    def tambah_kontak(self, kontak):
        self.daftar_kontak.append(kontak)
        
    def tampilkan_semua_kontak(self):
        print("Daftar Kontak:")
        for kontak in self.daftar_kontak:
            kontak.tampilkan_info()
              
# Program Uwkqkqqk
if __name__ == "__main__":
    address_book = AddressBook()
    
    while True:
        print("Menu")
        print("1. Tambah Kontak")
        print("2. Tampilan semua kontak")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")  
        
        if pilihan == "1":
            nama = input("nama: ")
            nomor_telepon = input("Nomor Telepon: ")
            email = input("email: ")
            kontak_baru = Contact(nama, nomor_telepon, email)     
            address_book.tambah_kontak(kontak_baru)
        elif pilihan == "2":
            address_book.tampilkan_semua_kontak()               
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silahkan Pilih Menu yang benar.")