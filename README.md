# Program Command Line Interface (CLI) Sederhana: Pemesanan Nasi Goreng Hekel
> Program ini merupakan aplikasi yang berjalan di dalam command line (terminal). Program ini menggunakan *built-in library python* yaitu `argparse` yang dapat menerima parameter saat program ini dijalankan melalui terminal atau CLI.

## Fitur
- Pemesanan Nasi Goreng Hekel dengan beberapa opsi:
  - Jenis Porsi
  - Level Pedas
  - Toping

## Cara Menjalankan Program
1. Clone repository ini
2. Masuk ke dalam folder *nasi-goreng-hekel*
  ```
  # Bash terminal
  cd nasi-goreng-hekel
  ```
3. Jalankan command berikut:
  ```
  # Bash terminal
  python main.py -h
  ```
  Dengan menjalankan command tersebut, tersedia penjelasan terkait cara penggunaan program beserta *argument* dan *option* yang tersedia
  Sample Command:
  ```
  python main.py nasgor hajatan --pedas 5 --topping seafood "telur ceplok"
  ```


## Latihan Kontribusi Open Source
1. Silahkan lakukan **fork** (clone tapi di akun github kamu) *repository* ini, maka di dalam akun github kamu akan tersedia repository yang sama dengan repository ini.
2. Di silahkan buka repository tersebut (di akun github kamu)
3. Clone repository tersebut
4. Lakukan penambahan fitur, perbaiki typo, atau apapun yang menurut kamu layak untuk diajukan sebagai kontribusi.
5. Lakukan **Pull Request** pada opsi **Contribute** -> **Open Pull Request** (di bawah tombol Go to file)