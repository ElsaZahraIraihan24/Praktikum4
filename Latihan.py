# Membuat list dengan 5 elemen
my_list = [22, 23, 24, 25, 26]

# Mengakses dan menampilkan elemen ke-3
elemen_ke_3 = my_list[2]
print("Elemen ke-3:", elemen_ke_3)

# Mengambil nilai elemen ke-2 sampai elemen ke-4
nilai_elemen_2_ke_4 = my_list[1:4]
print("Nilai elemen ke-2 sampai elemen ke-4:", nilai_elemen_2_ke_4)

# Mengambil elemen terakhir
elemen_terakhir = my_list[-1]
print("Elemen terakhir:", elemen_terakhir)

# Membuat list dengan 5 elemen
my_list = [22, 23, 24, 25, 26]

# Ubah elemen ke-4 dengan nilai lainnya
my_list[3] = 45

# Ubah elemen ke-4 sampai dengan elemen terakhir
my_list[3:] = [31, 32, 33]

# Menampilkan list setelah perubahan
print("List setelah perubahan:", my_list)

# Membuat list dengan 5 elemen
my_list = [22, 23, 24, 25, 26]

# Ambil 2 bagian dari list pertama (A) dan jadikan list ke-2 (B)
list_A = my_list[:2]
list_B = list_A.copy()

# Tambahkan list B dengan nilai string
list_B.append("Hello")

# Tambahkan list B dengan 3 nilai
list_B.extend([1, 2, 3])

# Gabungkan list B dengan list A
list_A_and_B = list_B + list_A

# Menampilkan hasil akhir
print("List A setelah perubahan:", list_A)
print("List B setelah perubahan:", list_B)
print("Hasil gabungan list B dan A:", list_A_and_B)