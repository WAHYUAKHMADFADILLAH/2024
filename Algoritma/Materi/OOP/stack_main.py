from stack_modul import Stack
something = Stack()

something.push('barang')
something.push('sesuatu')
something.push('kacamata')
something.push('makanan')
something.print()
something.pop()
something.print()


print('Apakah kosong : ',something.isEmpty())
print('Data Tertinggi : ',something.peek())
print('Banyaknya something : ',something.size())