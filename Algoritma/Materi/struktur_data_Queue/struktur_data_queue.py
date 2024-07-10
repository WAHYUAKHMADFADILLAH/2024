queue = []

# Tambah data queue
def enqueue(item):
    queue.append(item)
# Hapus data pertama
def dequeue():
    queue.pop(0)

# Mengecek data atau element pertama
def front():
    if len(queue) < 1 :
        return 'Data kosong'
    else:
        return queue[0]
# Mengecek element terakhir
def tail():
    return queue[-1]

def isEmpty():
    if len (queue) == 0 :
        return 'Queue kosong'
    else:
        return 'Queue ada data'
    
def size():
    len(queue) 
# Panggil fungsi dan menambah data
enqueue('udin')
enqueue('dimas')
enqueue('ukin')

print(queue)
dequeue()
print(queue)

print(f'Data pertama : {front()}')
print(f'Data Terakhir : {front()}')
print(f'Apakah Queue kosong : {isEmpty()}')
print(f'Jumlah Queue : {size()}')
