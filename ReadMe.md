# Project SuperCashier

Project SuperCashier adalah aplikasi kasir sederhana yang dibuat menggunakan bahasa pemrograman Python. Aplikasi ini dirancang untuk supaya pembeli dapat memasukan transaksi penjualan dengan sendirinya. 

# Tujuan Pengerjaan Project

1. Membuat aplikasi kasir sederhana yang dapat:
    - Menambahkan barang baru ke dalam transaksi.
    - Menghitung total harga barang dalam transaksi.
    - Mengeluarkan struk transaksi.
2. Membuat program dengan bahasa pemrograman Python.

# Deskripsi Task

Modul `transaction.py` berisi kelas `Transaction` yang berfungsi untuk membuat dan mengelola transaksi. Setiap transaksi berisi sejumlah barang dengan harga dan kuantitas masing-masing, yang kemudian akan ditampilkan dalam satu struk transaksi.

## Alur Program / Flowchart

Secara sederhana, alur dari `SuperCashier` dapat diilustrasikan seperti berikut:

![FlowChart](https://github.com/Keembo/SuperCashier/blob/main/Screenshots/Untitled%20Diagram.drawio.png?raw=true)

FlowChart Program SuperCashier

Penjelasan flow:
1. Membuat transaksi baru
2. Menambahkan barang ke dalam transaksi
3. Memeriksa atau memodifikasi detail barang jika perlu
4. Menghitung harga total & Menampilkan transaksi

## Fungsi yang Dibutuhkan

Berikut beberapa fungsi penting dalam `SuperCashier`:

- `add_barang`: fungsi untuk menambahkan barang ke dalam transaksi.
- `check_order`: fungsi untuk memeriksa detail barang dalam transaksi.
- `update_barang_name`, `update_barang_qty`, `update_barang_price`: fungsi untuk memodifikasi detail barang.
- `delete_barang`: fungsi untuk menghapus barang dari transaksi.
- `reset_transaction`: fungsi untuk mereset transaksi.
- `total_price`: fungsi untuk menghitung total harga transaksi.
- `display_items`: fungsi untuk menampilkan transaksi.

## Snippet Code dan Penjelasan

Berikut adalah penjelasan fungsi penting dalam `SuperCashier`.

### Membuat Transaksi Baru

```python
transaksi = Transaction()
```

Ini akan membuat objek transaksi baru. Dalam prosesnya, kita akan diminta untuk memasukkan nama pembeli.

### Menambahkan barang ke Dalam Transaksi

```python
transaksi.add_barang()
```

Fungsi `add_barang` digunakan untuk menambahkan barang ke dalam transaksi. Kita akan diminta untuk memasukkan nama barang, jumlah, dan harganya. Selain itu, ada juga pilihan untuk memeriksa transaksi atau keluar dari proses.

### Memeriksa Detail Transaksi

```python
print(transaksi.check_order())
```

Fungsi `check_order` akan memeriksa detail barang dalam transaksi. Jika ada kesalahan input atau tidak ada barang dalam daftar, fungsi ini akan memberikan feedback.

### Memodifikasi Detail barang

```python
transaksi.update_barang_name()
transaksi.update_barang_qty()
transaksi.update_barang_price()
```

Kita bisa memodifikasi nama, kuantitas, dan harga barang dengan fungsi `update_barang_name`, `update_barang_qty`, dan `update_barang_price` secara berurutan.

### Menghapus barang dari Transaksi

```python
transaksi.delete_barang()
```

Fungsi `delete_barang` akan menghapus barang dari daftar transaksi. Kita akan diminta untuk memilih barang mana yang ingin dihapus.

### Mereset Transaksi

```python
transaksi.reset_transaction()
```

Fungsi `reset_transaction` akan menghapus semua barang dalam transaksi, membuat transaksi menjadi kosong seperti baru.

### Menghitung Total Harga

```python
print(transaksi.total_price())
```

Fungsi `total_price` akan menghitung total harga dari semua barang dalam transaksi. Diskon akan diterapkan berdasarkan jumlah total.

### Menampilkan Transaksi

```python
print(transaksi.display_items())
```

Fungsi `display_items` akan menampilkan detail transaksi dalam bentuk tabel yang rapi, dengan informasi tentang nama pembeli, barang, jumlah, dan total harga.

# Hasil Test Case

### Test Case 1
Input:
```python
transaksi = Transaction()
transaksi.add_barang()
```
```
Nilai yang di input:
Nama barang: Ayam Goreng, Qty: 2, Harga: 20000
Nama barang: Pasta Gigi, Qty: 3, Harga: 15000
```
Output:

![TestCase1](https://github.com/Keembo/SuperCashier/blob/main/Screenshots/Test%201.png?raw=true)

### Test Case 2
Input:
```python
transaksi = Transaction()
transaksi.delete_barang()
```
```
Nilai yang di delete:
Nama barang: Pasta Gigi
```

Output:

![TestCase2](https://github.com/Keembo/SuperCashier/blob/main/Screenshots/Test%202.png?raw=true)

### Test Case 3
Input:
```python
transaksi = Transaction()
transaksi.reset_transaction()
```

Output:

![TestCase3](https://github.com/Keembo/SuperCashier/blob/main/Screenshots/Test%203.png?raw=true)

### Test Case 4
Input:
```python
transaksi = Transaction()
transaksi.total_price()
```

Output:

![TestCase3](https://github.com/Keembo/SuperCashier/blob/main/Screenshots/Test%204.png?raw=true)

# Cara Menggunakan Program

1. Download file `transaction.py`.
2. Buka terminal/Jupyter notebook dan sesuaikan lokasi direktori lokal.
3. Jalankan modul `transaction.py` di terminal untuk memulai aplikasi.

Demikianlah penjelasan singkat mengenai `SuperCashier`
