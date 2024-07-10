class Manusia:
    def __init__(self,Inputhidung,Inputmata,Inputrambut):
        self.hidung = Inputhidung
        self.mata = Inputmata
        self.rambut = Inputrambut

class pacar :
    def __init__(self,nama) :
        self.nama = nama
    def get_pasangan(self):
        return self.nama()

class Kim_Se_jeong(Manusia,pacar):
    def __init__(self,hidung,mata,rambut,nama):
        # super().__init__(hidung,mata,rambut)
        Manusia.__init__(self,hidung,mata,rambut)
        pacar.__init__(self,nama)

        self.kulit = mata

    def information(self):
        return f'Hidung : {self.hidung} Mata : {self.mata} Rambut : {self.rambut} Pacar : {self.nama} '

    def get_mata(self):
        return self.mata

Se_jeong = Kim_Se_jeong('Mancung','blue','gold','Wa-heyou')
print(Se_jeong.information())
print(Se_jeong.get_mata())