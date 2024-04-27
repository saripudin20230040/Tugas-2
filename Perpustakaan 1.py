class perpustakaan:
  def _init_(self):
    self .koleksi_buku = []

def tampilkan_buku(self):
 if self.koleksi_buku:
  print("-- Daftar Buku --")
  for buku in self.koleksi_buku:
   print(buku)
  else:
   print("koleksi buku masih kosong.")
def cari_buku(self, judul):
  for buku in self.koleksi_buku:
    if buku.judul.lower() == judul.lower():
     print(buku)
     return
  print(f"Buku dengan judul {judul}' tidak di temukan.")

def pinjam_buku(self, buku, anggota):
  if buku.status == "Tersedia":
    buku.status = "Dipinjam"
    anggota.buku_pinjaman.append(buku)
    print(f"Buku '{buku,judul}' berhasil pinjaman oleh {anggota.nama}.")
  else:
   print(f"Buku '{buku.judul}' tidak tersedia untuk di pinjam.")