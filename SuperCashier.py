"""
Module SuperCashier ini digunakan untuk mencatat penjualan barang, dan juga dapat memodifikasi isi transaksi,
Anda dapat melakukan import SuperCashier dan kemudian menjalankan fungsinya sesuai dengan petunjuk.
"""

# Import tabulate untuk memperindah hasil transaksi
from tabulate import tabulate

# Menciptakan class untuk menampung method dan kalkulasi transaksi
class Transaction:
    def __init__(self):
        self.buyer = input("Masukkan nama pembeli: ") # Nama pembeli perlu di input
        self.items = []

# Menambahkan barang dalam transaksi
    def add_item(self):
        """
        Menambahkan input pilihan untuk memudahkan proses penambahan barang dan menentukan proses transaksi
        """
        while True:
            print("1. Tambah barang\n2. Periksa Transaksi\n3. Keluar") # Memberi pilihan untuk menambah barang atau memeriksa transaksi
            selection = input("Pilih no: ")
            try:
                if selection == '1': # Opsi menambahkan barang
                    item_name = input("Masukkan nama barang: ")
                    if not item_name:
                        raise ValueError("Nama Barang tidak boleh kosong.")
                    item_qty = float(input("Masukkan jumlah barang: "))
                    if item_qty <= 0:
                        raise ValueError("Jumlah barang tidak boleh negatif.")
                    item_price = float(input("Masukkan harga barang: "))
                    if item_price <= 0:
                        raise ValueError("Harga barang tidak boleh negatif.")
                    
                     # Memasukan barang kedalam list
                    self.items.append([item_name, item_qty, item_price])

                elif selection == '2': # Opsi memeriksa transaksi
                    # Menjalan check_order untuk memeriksa transaksi
                    check_result = self.check_order()
                    print(check_result)
                    
                    # Menampilkan hasil pemeriksaan dan menawarkan untuk menunjukan hasil
                    if check_result == "Pemesanan sudah benar":
                        if not self.items:
                            print("Tidak ada barang dalam daftar.")
                        else:
                            display_selection = input("Apakah ingin menampilkan hasil? (y/n): ")
                            if display_selection.lower() == 'y':
                                print(self.display_items())
                            break

                elif selection == '3':  # Opsi Keluar
                    break

                else:
                    print("Kesalahan Input, pilih 1, 2 atau 3.")
            except ValueError as e:
                print("Mohon coba kembali:", e)

# Memodifikasi nama barang dalam transaksi
    def update_item_name(self):
        try:
            if not self.items:
                print("Tidak ada barang.")
                return
            print("Pilih barang :")
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item[0]}")
            item_index = int(input("Masukan no barang yang akan di perbaharui: ")) - 1
            new_name = input("Masukkan nama baru :")
            self.items[item_index][0] = new_name
        except Exception as e:
            print("Terjadi kesalahan:", e)

# Memodifikasi jumlah barang dalam transaksi
    def update_item_qty(self):
        try:
            if not self.items:
                print("Tidak ada barang.")
                return
            print("Pilih barang :")
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item[0]}")
            item_index = int(input("Masukan no barang yang akan di perbaharui: ")) - 1
            new_qty = float(input("Masukkan jumlah baru : "))
            if new_qty <= 0: # Memastikan nilai baru tidak negatif
                raise ValueError("Jumlah barang tidak boleh negatif atau nol.")
            self.items[item_index][1] = new_qty
        except ValueError as e:
            print("Terjadi kesalahan:", e)
        except Exception as e:
            print("Terjadi kesalahan:", e)

# Memodifikasi harga barang dalam transaksi
    def update_item_price(self):
        try:
            if not self.items:
                print("Tidak ada barang.")
                return
            print("Pilih barang :")
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item[0]}")
            item_index = int(input("Masukan no barang yang akan di perbaharui: ")) - 1
            new_price = float(input("Masukkan harga baru :"))
            if new_price <= 0: # Memastikan nilai baru tidak negatif
                raise ValueError("Harga barang tidak boleh negatif atau nol.")
            self.items[item_index][2] = new_price
        except ValueError as e:
            print("Terjadi kesalahan:", e)
        except Exception as e:
            print("Terjadi kesalahan:", e)

# Menghapus salah satu barang dalam transaksi
    def delete_item(self):
        try:
            if not self.items:
                print("Tidak ada barang.")
                return
            print("Pilih barang :")
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item[0]}")
            item_index = int(input("Masukan no barang yang akan di hapus: ")) - 1
            self.items.pop(item_index)
        except Exception as e:
            print("Terjadi kesalahan:", e)

# Menghapus seluruh transaksi
    def reset_transaction(self):
        self.items = []
        print("Transaksi sudah di reset.")

# Memerikan transaksi
    def check_order(self):
        if not self.items:
            return "Tidak ada barang dalam daftar."
        for item in self.items:
            if item[0] == "" or item[1] <= 0 or item[2] <= 0:
                return "Terdapat kesalahan input data"
        return "Pemesanan sudah benar"

# Menghitung harga total / barang
    def total_price(self):
        total = 0.0
        discount = 0.0
        for item in self.items:
            total += item[1] * item[2]

        # Menghitung diskon yang didapatkan
        """
        Menghitung diskon yang didapatkan berdasarkan total harga transaksi
        """       
        if total > 500000.0:
            discount = total * 0.1
            total = total * 0.9
        elif total > 300000.0:
            discount = total * 0.08
            total = total * 0.92
        elif total > 200000.0:
            discount = total * 0.05
            total = total * 0.95
        return total, discount

# Menampilkan hasil transaksi
    def display_items(self):
        table = []
        total_price = 0.0

        # Menampilkan nama pembeli
        table.append(["Nama Pembeli", self.buyer, "", "", ""])

        # Menambahkan nama collumn
        table.append(["No", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"])

        # Mengisi tabel dengan barang transaksi
        for i, item in enumerate(self.items):
            nama_item, jumlah_item, harga_per_item = item
            total_harga = jumlah_item * harga_per_item
            total_price += total_harga
            table.append([i+1, nama_item, jumlah_item, harga_per_item, total_harga])

        # Memnghitung total akhir setelah diskon
        final_total, discount = self.total_price()

        # Menampilan perhitungan total akhir dan menunjukan diskon
        table.append(["", "", "", "Total", total_price])
        table.append(["", "", "", "Diskon", discount])
        table.append(["", "", "", "Total Akhir", final_total])

        return tabulate(table, headers="firstrow", tablefmt='fancy_grid')
