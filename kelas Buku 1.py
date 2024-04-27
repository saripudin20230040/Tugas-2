class Buku :
 def __init_(self, judul, penulis, genre, status):
   self.judul = judul
   self.penulis = penulis
   self.genre = genre
   self.status = status

   def _str_(self):
     return f"{self.judul} - {self.penulis} ({genre}) - status: {self.status}"
   