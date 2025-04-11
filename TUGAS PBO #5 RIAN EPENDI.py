# 1. Polymorphism untuk Kendaraan
from abc import ABC, abstractmethod

class Kendaraan(ABC):
    """Kelas abstrak untuk berbagai jenis kendaraan"""
    
    @abstractmethod
    def move(self):
        """Method abstract yang akan diimplementasikan oleh subclass"""
        pass

class Mobil(Kendaraan):
    def move(self):
        print("Mobil bergerak dengan empat roda di jalan")

class Sepeda(Kendaraan):
    def move(self):
        print("Sepeda bergerak dengan dikayuh di jalanan")

class Perahu(Kendaraan):
    def move(self):
        print("Perahu bergerak dengan mengapung di air")


# 2. Polymorphism untuk Autentikasi Pengguna
class Autentikasi(ABC):
    """Interface untuk berbagai metode autentikasi"""
    
    @abstractmethod
    def login(self, username, credential):
        pass
    
    @abstractmethod
    def get_auth_method(self):
        pass

class EmailPasswordAuth(Autentikasi):
    def login(self, email, password):
        # Logika validasi email dan password
        print(f"Autentikasi dengan email: {email} dan password")
        return True  # Simulasi berhasil login
    
    def get_auth_method(self):
        return "Email dan Password"

class GoogleAuth(Autentikasi):
    def login(self, google_id, token):
        # Logika validasi Google ID
        print(f"Autentikasi dengan Google ID: {google_id}")
        return True  # Simulasi berhasil login
    
    def get_auth_method(self):
        return "Google Authentication"

class FingerprintAuth(Autentikasi):
    def login(self, user_id, fingerprint_data):
        # Logika validasi sidik jari
        print(f"Autentikasi dengan sidik jari untuk user: {user_id}")
        return True  # Simulasi berhasil login
    
    def get_auth_method(self):
        return "Sidik Jari"


# Fungsi untuk demonstrasi polymorphism
def main():
    # Demonstrasi polymorphism pada kendaraan
    print("=== DEMONSTRASI POLYMORPHISM KENDARAAN ===")
    kendaraan_list = [Mobil(), Sepeda(), Perahu()]
    
    for kendaraan in kendaraan_list:
        kendaraan.move()  # Setiap kendaraan memiliki implementasi move() yang berbeda
    
    # Demonstrasi polymorphism pada autentikasi
    print("\n=== DEMONSTRASI POLYMORPHISM AUTENTIKASI ===")
    auth_methods = [
        EmailPasswordAuth(),
        GoogleAuth(),
        FingerprintAuth()
    ]
    
    for auth in auth_methods:
        print(f"Metode: {auth.get_auth_method()}")
        auth.login("user123", "credential123")  # Implementasi login berbeda untuk setiap metode
        print()

if __name__ == "__main__":
    main()