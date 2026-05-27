class Kampus :
    def perkenalan(self):
        print("Selamat datang di" , self.nama , "Alamat :" , self.alamat)
        
    
    def greeting(self,nama):
        print("hello",nama ,"welcome to" , self.nama ,"Alamat :" , self.alamat)

class Mahasiswa :
    pass

Kampus1 = Kampus()
Kampus2 = Kampus()

print(Kampus1)
print(Kampus2)

mahasiswa1 = Mahasiswa()
mahasiswa1.nama = "dias"
mahasiswa1.nim  = "462025611054"

mahasiswa2 = Mahasiswa()
mahasiswa2.nama = "rizki"
mahasiswa2.nim  = "462025611055"

print(mahasiswa1.nama)
print(mahasiswa1.nim)

print(mahasiswa2.nama)
print(mahasiswa2.nim) 

kampus_perkenalan = Kampus()
kampus_perkenalan.nama   = "Universitas Darussalam Gontor Kampus A"
kampus_perkenalan.alamat = "Jl.Siman , Demangan , Siman , Ponorogo" 
kampus_perkenalan.perkenalan()

kampus_greeting = Kampus()
kampus_greeting.nama = "Universitas Darussalam Gontor Kampus C"
kampus_greeting.alamat = "dusun demangan, siman, ponorogo, jawa timur"
kampus_greeting.greeting("dias")