# SuperCashier: Sebuah Panduan Transaksi yang Mudah dan Mendidik

Hai, rekan belajar! 🙌

Selamat datang di dunia `SuperCashier`, sebuah modul yang menyenangkan dan edukatif tentang pengelolaan transaksi penjualan. Kita akan melihat bagaimana paket ini dengan mudah mengelola barang penjualan, melakukan berbagai modifikasi transaksi, dan menampilkan semua data dengan cara yang rapi dan mudah dimengerti. Siap terjun? Mari kita mulai!

## Latar Belakang

`SuperCashier` adalah sebuah modul Python yang diciptakan untuk memudahkan proses pencatatan dan pengelolaan transaksi penjualan. Dengan menggunakan `SuperCashier`, kita dapat menginput, memodifikasi, hingga menghapus item transaksi dengan mudah dan efisien.

## Requirements / Objectives

Berikut adalah beberapa fitur yang disediakan oleh `SuperCashier`:

- Menambahkan item ke dalam transaksi
- Memeriksa detail transaksi
- Memodifikasi detail item
- Menghapus item dari transaksi
- Mereset transaksi
- Menghitung harga total transaksi
- Menampilkan transaksi

## Alur Program / Flowchart

Secara sederhana, alur dari `SuperCashier` dapat diilustrasikan seperti berikut:

1. Membuat transaksi baru
2. Menambahkan item ke dalam transaksi
3. Memeriksa atau memodifikasi detail item jika perlu
4. Menghitung harga total
5. Menampilkan transaksi

## Fungsi yang Dibutuhkan

Berikut beberapa fungsi penting dalam `SuperCashier`:

- `add_item`: fungsi untuk menambahkan item ke dalam transaksi.
- `check_order`: fungsi untuk memeriksa detail item dalam transaksi.
- `update_item_name`, `update_item_qty`, `update_item_price`: fungsi untuk memodifikasi detail item.
- `delete_item`: fungsi untuk menghapus item dari transaksi.
- `reset_transaction`: fungsi untuk mereset transaksi.
- `total_price`: fungsi untuk menghitung total harga transaksi.
- `display_items`: fungsi untuk menampilkan transaksi.

## Snippet Code dan Penjelasan

Berikut adalah contoh penggunaan fungsi dalam `SuperCashier`:

Tentu! Mari kita bahas satu per satu fungsi penting dalam kode `SuperCashier`.

### Membuat Transaksi Baru

```python
transaksi = Transaction()
```

Ini akan membuat objek transaksi baru. Dalam prosesnya, kita akan diminta untuk memasukkan nama pembeli.

### Menambahkan Item ke Dalam Transaksi

```python
transaksi.add_item()
```

Fungsi `add_item` digunakan untuk menambahkan item ke dalam transaksi. Kita akan diminta untuk memasukkan nama barang, jumlah, dan harganya. Selain itu, ada juga pilihan untuk memeriksa transaksi atau keluar dari loop.

### Memeriksa Detail Transaksi

```python
print(transaksi.check_order())
```

Fungsi `check_order` akan memeriksa detail item dalam transaksi. Jika ada kesalahan input atau tidak ada barang dalam daftar, fungsi ini akan memberikan feedback yang relevan.

### Memodifikasi Detail Item

```python
transaksi.update_item_name()
transaksi.update_item_qty()
transaksi.update_item_price()
```

Kita bisa memodifikasi nama, kuantitas, dan harga barang dengan fungsi `update_item_name`, `update_item_qty`, dan `update_item_price` secara berurutan.

### Menghapus Item dari Transaksi

```python
transaksi.delete_item()
```

Fungsi `delete_item` akan menghapus item dari daftar transaksi. Kita akan diminta untuk memilih item mana yang ingin dihapus.

### Mereset Transaksi

```python
transaksi.reset_transaction()
```

Fungsi `reset_transaction` akan menghapus semua item dalam transaksi, membuat transaksi menjadi kosong seperti baru.

### Menghitung Total Harga

```python
print(transaksi.total_price())
```

Fungsi `total_price` akan menghitung total harga dari semua item dalam transaksi. Diskon akan diterapkan berdasarkan jumlah total.

### Menampilkan Transaksi

```python
print(transaksi.display_items())
```

Fungsi `display_items` akan menampilkan detail transaksi dalam bentuk tabel yang rapi, dengan informasi tentang nama pembeli, item, jumlah, dan total harga.


Demikianlah penjelasan singkat mengenai `SuperCashier`. Selamat mencoba dan belajar! 🎉