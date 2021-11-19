import argparse

import nasgor

parser = argparse.ArgumentParser(
  prog = "nasgor",
  description = "Pemesanan Nasi Goreng Hekel",
  usage="Cara penggunaan: nasgor [ARGS][OPTIONS]",
  epilog= """contoh: python main.py nasgor diet --pedas 15 --topping sosis telur_ceplok --jumlah 2, \nNote: jika ada topping yang terdiri lebih dari satu kata, ganti spasi dengan garis bawah. \nSilahkan periksa menu list (--list-menu). Terima kasih..."""
  )

parser.add_argument(
  '-lm',
  '--list-menu',
  action='store_true',
  help= "Menampilkan list level pedas dan jenis topping"
)

subparser = parser.add_subparsers()
nasgor_parser = subparser.add_parser('nasgor')
nasgor_parser.add_argument(
  'porsi',
  type = str,
  choices = nasgor.porsi,
  help = "Menentukan porsi nasi goreng, wajib ditentukan."
)

nasgor_parser.add_argument(
  '--topping', '-t', 
  type = str,
  action='store',  
  nargs = '+', 
  choices = nasgor.toppings,
  help =" Pesan nasi goreng dengan toping tertentu")


nasgor_parser.add_argument(
  '--pedas',
  type = int,
  action='store',
  # choices = nasgor.pedas,
  default = 10,
  help = "Menentukan tingkat pedas. Default 10."
)

nasgor_parser.add_argument(
  '-j','--jumlah',
  type = int,
  action='store',
  default = 1,
  help = "Menentukan jumlah pesanan nasi goreng"
)

args = parser.parse_args()
# print(args)

if args.list_menu:
  print(f"""
  
  LIST PORSI (wajib pilih satu)
  - diet : 5K
  - sedang : 10K
  - besar : 20K
  - hajatan : 30K

  LEVEL PEDAS (0 - 20, default 10)

  JENIS TOPPING (opsional, maksimal 2)
  - sosis : 1K
  - ati ampela : 2K
  - telur ceplok : 2K
  - telur dadar : 2K
  - teri : 3K
  - bakso : 3K
  - seafood : 4K

  SELAMAT BELANJA GEEKS!
  """)
else:
  ###################################################
  # Tambahan peringatan pedas berlebih
  if args.pedas > 20:
    parser.error("Sayangi Lambung, sayangku. ') ")

  ###################################################

  if args.topping != None and len(args.topping) > 2:
    parser.error("Toping maksimal 2 aja yaa, lagi mahal nih bahan makanan.")

  bayar = 0
  pesanan = ""

  bayar = args.jumlah * nasgor.porsi[args.porsi]

  if args.topping != None:
    for i in args.topping:
      bayar += nasgor.toppings[i]
    pesanan = f"Kamu akan memesan {args.jumlah} nasi goreng hekel porsi {args.porsi} dengan toping {', '.join(args.topping)}, \nHarga yang harus kamu bayar Rp.{bayar} \n"
  else:
    pesanan = f"Kamu akan memesan {args.jumlah} nasi goreng hekel porsi {args.porsi} tanpa toping, \nHarga yang harus kamu bayar Rp.{bayar} \n"
  print(pesanan)

  user_input = input("Tampilkan kwitansi? ")
  if user_input.lower() in ["y", "ya", "yes", "iya"]:
    print("DAFTAR PEMBELIAN: ")
    print("Nasi Goreng " + args.porsi + " : Rp." + str(nasgor.porsi[args.porsi]) + " kali " + str(args.jumlah))
    if args.topping != None:
      print("Topping, ")
      for i in args.topping:
        print(i + " : Rp." + str(nasgor.toppings[i]))
    print("Terima kasih telah memesan. Have a nice day :)")
    