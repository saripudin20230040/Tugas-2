def main ():
    # Buat bebrapa buku
    buku1 = Buku("Bumi", "Tere Liye", "Fiksi", "Tersedia")
    buku2 = Buku("Laskar pelangi"," Andrea  Hirata", "Fiksi", "Tersedia")
    buku3 = Buku("Filosofi Terbang", "dewi Lestari", "Fiksi", "Dipinjam")

    # Buat Perpustakaan dan anggota
    perpustakaan = perpustakaan()
    perpustakaan.koleksi_buku.extend([buku1, buku2, buku3]) 

    anggota1 = Anggota("Andi", 12345)
    anggota2 = Anggota("Budi", 56789)

    # Jalankan Program
    print("\n-- Menu Perpustakaan --")
    print("1. Tampilkan Daftar Buku")
    print("2. Cari Buku")
    print("3. Pinjam Buku")
    print("4. Kembalikan")
    angka=int(input("pilih menu :_"))

    if angka == 1:
        perpustakaan.tampilkan_buku();
    elif angka == 2:
        perpustakaan.cari_buku(judul);
    elif angka== 3:
        buku=input("buku ysng di pinjam:")
        anggota =input("input nam anggota :")
        perpustakaan.pinjam_buku(buku, anggota)
    else:
        print("anda salah pilih")
        
    if _name_=="_main_":
        main();
 