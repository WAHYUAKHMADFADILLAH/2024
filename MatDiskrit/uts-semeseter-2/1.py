mahasiswa_tuple = ("GERALDI","BANU","NUNIK","MUHAMMAD","DINDA","RENDI","ALIFIA","WILDAN","BIMA","FADILLAH","RENDI",
                   "AINUR","RIFKY","NABILA","HILMY","DION","MUH","SALSABILA","AHMAD","PUTRA")
mahasiswa_list = ["GERALDI","BANU","NUNIK","MUHAMMAD","DINDA","RENDI","ALIFIA","WILDAN","BIMA","FADILLAH","RENDI",
                  "AINUR","RIFKY","NABILA","HILMY","DION","MUH","SALSABILA","AHMAD","PUTRA"]
maba = ["ANDI", "LISA", "RAHMA", "FARHAN", "SITI"]
mahasiswa_tuple = mahasiswa_tuple + tuple(maba)
mahasiswa_list.extend(maba)
print(mahasiswa_tuple)
print(mahasiswa_list)
