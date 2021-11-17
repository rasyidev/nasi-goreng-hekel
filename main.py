import argparse

import nasgor

parser = argparse.ArgumentParser(
  prog = "nasgor",
  description = "Pemesanan Nasi Goreng Hekel",
  usage="Cara penggunaan: nasgor [ARGS][OPTION]",
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
  metavar = "toping", action='store',  
  nargs = '+', 
  type = str,
  choices = nasgor.toppings,
  help =" Pesan nasi goreng dengan toping tertentu")


nasgor_parser.add_argument(
  '--pedas',
  type = int,
  choices = nasgor.pedas,
  default = 10,
  help = "Menentukan tingkat pedas. Default 10."
)

nasgor_parser.add_argument(
  '-j','--jumlah',
  metavar = "jumlah",
  type = int,
  help = "Menentukan jumlah pesanan nasi goreng"
)

args = parser.parse_args()
print("ARGS:", args)

if args.list_menu:
  print(f"""
  LIST PORSI (wajib pilih satu)
  - diet
  - sedang
  - besar
  - hajatan

  LIST LEVEL PEDAS (default 10)
  - 5
  - 10
  - 15
  - 20

  JENIS TOPPING
  - sosis
  - ati ampela
  - telur ceplok
  - telur dadar
  - teri
  - bakso
  - seafood

  SELAMAT BELANJA GEEKS!
  """)
else:
  pesanan = f"Kamu akan memesan {args.jumlah} nasi goreng hekel porsi {args.porsi} dengan toping {', '.join(args.topping)}"
  print(pesanan)
