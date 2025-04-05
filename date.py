import datetime as dt

hari_ini = dt.date.today()
print(f"hari ini adalah hari {hari_ini}")

tanggal = dt.date(2005,10,1)
print(tanggal)

print("silahkan masukan tanggal, bulan dan tahun lahir anda")
tanggal = int(input("masukan tanggal: "))
bulan   = int(input("masukan bulan: "))
tahun = int(input("masukan tahun: "))

print(f"tanggal lahir kamu adalah {tahun}-{bulan}-{tanggal}")
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(tanggal_lahir)
