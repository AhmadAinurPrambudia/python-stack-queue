stack=0

def tambah barang(stack, barang baru); stack.append(barang baru) print(" (barang baru) berhasil ditambahkan ke dalam stack.")

def hapus_barang terakhir(stack): if len(stack) 0:

print("Stack kosong, tidak ada barang yang dapat dihapus.")

else:

barang terakhir-stack.pop()

print(" (barang terakhir) berhasil dihapus dari stack.")

def tampilkan barang teratas(stack); if len(stack)==0:

print("Stack kosong, tidak ada barang yang dapat ditampilkan.")

else:

barang teratas stack[-1] print("Barang teratas di dalam stack adalah (barang teratas).")

while True:

print("\nGudang saat ini:", stack)

print("Menu:") print("1. Tambah Barang")

print("2. Hapus Barang Terakhir")

print("3. Tampilkan Barang Teratas")

print("4. Keluar")

pilihan-input("Masukkan pilihan Anda (1/2/3/4);")

if pilihan == "1":

barang baru = input("Masukkan nama barang yang akan ditambahkan: ") tambah barang(stack, barang baru)

elif pilihan "2": I hapus_barang terakhir(stack)

elif pilihan "3": tampilkan barang teratas(stack)

elif pilihan print("Terima kasih telah menggunakan program ini.")

break

else: print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
