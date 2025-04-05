## 1. cara membuat string

'''
    1. String dengan single quot
    2. String dengan double quot
'''

data = 'String dengan single quot'
print(data)
data = "String dengan double quot"
print(data)

## 2. Operasi dan manipulasi string

salam = "hallo bro"
salam = salam.upper()
print(salam)
salam = salam.lower()
print(salam)

## 3. Width and multiline
data_nama = "Fajar Riza Fauzi"
data_umur = 17
data_tinggi = 150

# string standart
data_string = f"nama={data_nama} umur={data_umur} tinggi={data_tinggi}"
print(data_string)

# string multiline
data_strings = f"nama={data_nama} \numur={data_umur} \ntinggi={data_tinggi}"
print(data_strings)
