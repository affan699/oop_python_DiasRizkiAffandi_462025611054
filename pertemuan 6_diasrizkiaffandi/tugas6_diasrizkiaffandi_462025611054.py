
class Mahasiswa:
    def __init__(self, name, Role, Tingkat):
        self.name = name
        self.Role = Role
        self.Tingkat = Tingkat

    def info(self):
        print(f"Mahasiswa {self.name} Jurusan {self.Role} semester {self.Tingkat}.")
    
    def Belajar(self):
        print(f"{self.name} belajar teori.")
    
    def Tugas(self):
        print(f"{self.name} membuat tugas.")
    

class MahasiswaTeknik(Mahasiswa):
    def jenis_teknik(self):
        print("Jurusan Teknik Informatika.")
    
    def dari_parent(self):
        super().Tugas()
    
    def cek_diamond_problem(self):
        print("Cek diamond problem di kelas MahasiswaTeknik.")
        

class MahasiswaSeni(Mahasiswa):
    def jenis_seni(self):
        print("Jurusan Seni Rupa.")
    
    def dari_parent(self):
        super().Belajar()
    
    def cek_diamond_problem(self):
        print("Cek diamond problem di kelas MahasiswaSeni."
              )

class MahasiswaHybrid(MahasiswaTeknik, MahasiswaSeni):
    def info_neutral(self):
        print("Mahasiswa dengan dua kemampuan.")



if __name__ == "__main__":
    # Multiple Inheritance (Diamond Problem)
    print("=== MAHASISWA HYBRID ===")
    mhs1 = MahasiswaHybrid("Andi", "Teknik & Seni", "5")
    mhs1.info()
    mhs1.jenis_teknik()
    mhs1.jenis_seni()
    mhs1.cek_diamond_problem()
    
    # Single Inheritance
    print("\n=== MAHASISWA SENI ===")
    mhs2 = MahasiswaSeni("Budi", "Seni Rupa", "3")
    mhs2.info()
    mhs2.jenis_seni()
    mhs2.cek_diamond_problem()
    mhs2.dari_parent()
    mhs2.Tugas()
    
    print("\n=== MAHASISWA TEKNIK ===")
    mhs3 = MahasiswaTeknik("Cici", "Teknik Informatika", "1")
    mhs3.info()
    mhs3.jenis_teknik()
    mhs3.cek_diamond_problem()
    mhs3.dari_parent()
    mhs3.Belajar()
    
    # MRO
    print("\n=== MRO MahasiswaHybrid ===")
    print([c.__name__ for c in MahasiswaHybrid.__mro__])