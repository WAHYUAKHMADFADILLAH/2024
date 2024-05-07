nama_tuples = ('wahyu', 'wildan', 'dede', 'dila', 'bima', 'siti', 
               'shasa', 'slamet', 'rayan', 'fadil', 'dion', 'david', 
               'saif', 'putra', 'putri', 'akhmad', 'lala', 'Hannah', 
               'rehan', 'dodo')

nama_list = ['wahyu', 'wildan', 'dede', 'dila', 'bima', 'siti', 
               'shasa', 'slamet', 'rayan', 'fadil', 'dion', 'david', 
               'saif', 'putra', 'putri', 'akhmad', 'lala', 'Hannah', 
               'rehan', 'dodo']

nama_set = {'wahyu', 'wildan', 'dede', 'dila', 'bima', 'siti', 
               'shasa', 'slamet', 'rayan', 'fadil', 'dion', 'david', 
               'saif', 'putra', 'putri', 'akhmad', 'lala', 'Hannah', 
               'rehan', 'dodo'}

nama_baru = ['lala', 'lolo', 'lili', 'lele', 'bani']

nama_tuples += tuple(nama_baru)

nama_list.extend(nama_baru)

nama_set.update(nama_baru)

print("Tuples setelah tambahan nama baru:")
print(nama_tuples)

print("\nList setelah tambahan nama baru:")
print(nama_list)

print("\nSet setelah tambahan nama baru:")
print(nama_set)
