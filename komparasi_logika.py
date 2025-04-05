#latihan logika dan komparasi
inputUser = float(input("masukan angka yang bernilai :"))

#(komparasi) memriksa angka lebih kecil dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 = ", isKurangDari)

#(komparasi)  memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 = ", isLebihDari)

#operator logika
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan", isCorrect)

#operator logika
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukan", isCorrect)