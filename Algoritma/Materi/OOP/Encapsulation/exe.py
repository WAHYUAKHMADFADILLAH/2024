class book:
    def __init__(self,judul,penulis,tahun):
        self.__judul = judul
        self.__penulis = penulis
        self.__tahun = tahun
    def set_judul(self,judul):
        self.__judul = judul
    def get_judul(self):
        return self.__judul
    def set_penulis(self,penulis):
        self.__penulis = penulis
    def get_penulis(self):
        return self.__penulis
    def set_tahun(self,tahun):
        self.__tahun = tahun
    def get_tahun(self):
        return self.__tahun
    def display(self):
        print("Judul : ",self.__judul)
        print("Penulis : ",self.__penulis)
        print("Tahun : ",self.__tahun)
class ebook:
    def __init__(self,book,ukuran_file):
        super().__init__(self,ukuran_file)
        self.__ukuran_file = ukuran_file
    def information(self):
    def set_ukuran(self,ukuran_file):
        self.__set_ukuran = ukuran_file
    