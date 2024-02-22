# Challenge Pertama
print('bilangan genap >= 10 dan <= 20 dan juga bilangan ganjil >=90 dan <= 100 : ')
data1 = [ i for i in range (10, 21) if i % 2 == 0]
data2 = [ i for i in range (90, 100) if i % 2 == 1]
data1.extend(data2)
print(data1)

# Challenge Kedua

data = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti']
print('Data sebelum :')
print(data)
data.remove('Re')
data.append('Re')
data.remove('Mi')
data.insert(0, 'Mi')
print('Data sesudah :')
print(data)

# Challenge Ketiga

data3 = "IgNatIus"
hasil = []
for i in data3:
    if i.isupper():
        hasil.append(i)
print("Hasil:", hasil)