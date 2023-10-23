import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'D:\Tugas Rafi\Kuliah\Tugas\Semester 3\Statistika\M. NAUFAL RAFY GHALY_22081010295_TUGASP3PENGOLAHANDATADANPENYAJIANDATA_STATKOME2324.xlsx', sheet_name='Sort')

# MEAN, MEDIAN, MODUS, VARIANS, STD
print("-----------MEAN, MEDIAN, MODUS-----------")
print("\n")


# Kolom 1
print("Celullar Subscription")

mean1 = df['Cellular Subscription'].mean() # df = DataFrame
print(f"Mean: {mean1}")

median1 = df['Cellular Subscription'].median()
print(f"Median: {median1}")

modus1 = df['Cellular Subscription'].mode().values[0]
print(f"Modus: {modus1}")

varians1 = df['Cellular Subscription'].var()
print(f"Varians: {varians1}")

standardeviasi1 = df['Cellular Subscription'].std()
print(f"Standar Deviasi: {standardeviasi1}")

print('\n')

# Kolom 2
print("Internet USers (%)")
mean2 = df['Internet Users(%)'].mean() # df = DataFrame
print(f"Mean: {mean2}")

median2 = df['Internet Users(%)'].median()
print(f"Median: {median2}")

modus2 = df['Internet Users(%)'].mode().values[0]
print(f"Modus: {modus2}")

varians2 = df['Internet Users(%)'].var()
print(f"Varians: {varians2}")

standardeviasi2 = df['Internet Users(%)'].std()
print(f"Standar Deviasi: {standardeviasi2}")

print('\n')

# Kolom 3
print("No. Of Internet Users")
mean3 = df['No. of Internet Users'].mean() # df = DataFrame
print(f"Mean: {mean3}")

median3 = df['No. of Internet Users'].median()
print(f"Median: {median3}")

modus3 = df['No. of Internet Users'].mode().values[0]
print(f"Modus: {modus3}")

varians3 = df['No. of Internet Users'].var()
print(f"Varians: {varians3}")

standardeviasi3 = df['No. of Internet Users'].std()
print(f"Standar Deviasi: {standardeviasi3}")

print('\n')

# Kolom 4
print("Broadband Subscribption")
mean4 = df['Broadband Subscription'].mean() # df = DataFrame
print(f"Mean: {mean4}")

median4 = df['Broadband Subscription'].median()
print(f"Median: {median4}")

modus4 = df['Broadband Subscription'].mode().values[0]
print(f"Modus: {modus4}")

varians4 = df['Broadband Subscription'].var()
print(f"Varians: {varians4}")

standardeviasi4 = df['Broadband Subscription'].std()
print(f"Standar Deviasi: {standardeviasi4}")

print("\n")
# -------Normalisasi Penyajian Data--------------
df2 = pd.read_excel(r'D:\Tugas Rafi\Kuliah\Tugas\Semester 3\Statistika\M. NAUFAL RAFY GHALY_22081010295_TUGASP3PENGOLAHANDATADANPENYAJIANDATA_STATKOME2324.xlsx', sheet_name='NormalisasiCode')


#Frekuensi
print("-----------FREKUENSI-----------")
print("\n")

batas_atas = [0, 0.2, 0.4, 0.6, 0.8, 1]
rentang = ['0-0.2', '0.21-0.4', '0.41-0.6', '0.61-0.8', '0.81-1']


df2['Celullar Subscription'] = pd.cut(df2['Cellular Subscription'], bins=batas_atas, labels=rentang, right=False) #pd.cut() fungsi untuk mengelompokkan/memontong data menjadi interval tertentu, bins=batas interval/kelompok, labels=untuk memberikan label/nama setiap kelompok atau interval, right = false (batas atas interval tidak masuk ke interval), right = true (batas atas interval masuk ke interval)

frekuensi_data = df2['Celullar Subscription'].value_counts().sort_index() #value_counts untuk menghitung frekuensi
print(f"Frekuensi: {frekuensi_data}")
print("\n")


df2['Internet Users(%)'] = pd.cut(df2['Internet Users(%)'], bins=batas_atas, labels=rentang, right=False) #pd.cut() fungsi untuk mengelompokkan/memontong data menjadi interval tertentu, bins=batas interval/kelompok, labels=untuk memberikan label/nama setiap kelompok atau interval, right = false (batas atas interval tidak masuk ke interval), right = true (batas atas interval masuk ke interval)

frekuensi_data = df2['Internet Users(%)'].value_counts().sort_index() #value_counts untuk menghitung frekuensi
print(f"Frekuensi: {frekuensi_data}")
print("\n")

df2['No. of Internet Users'] = pd.cut(df2['No. of Internet Users'], bins=batas_atas, labels=rentang, right=False) #pd.cut() fungsi untuk mengelompokkan/memontong data menjadi interval tertentu, bins=batas interval/kelompok, labels=untuk memberikan label/nama setiap kelompok atau interval, right = false (batas atas interval tidak masuk ke interval), right = true (batas atas interval masuk ke interval)

frekuensi_data = df2['No. of Internet Users'].value_counts().sort_index() #value_counts untuk menghitung frekuensi
print(f"Frekuensi: {frekuensi_data}")
print("\n")

df2['Broadband Subscription'] = pd.cut(df2['Broadband Subscription'], bins=batas_atas, labels=rentang, right=False) #pd.cut() fungsi untuk mengelompokkan/memontong data menjadi interval tertentu, bins=batas interval/kelompok, labels=untuk memberikan label/nama setiap kelompok atau interval, right = false (batas atas interval tidak masuk ke interval), right = true (batas atas interval masuk ke interval)

frekuensi_data = df2['Broadband Subscription'].value_counts().sort_index() #value_counts untuk menghitung frekuensi
print(f"Frekuensi: {frekuensi_data}")
print("\n")


# Frekuensi relatif (%)
print("-----------FREKUENSI RELATIF-----------")
print("\n")

frekuensi_data = df2['Celullar Subscription'].value_counts().sort_index() #dipanggil lagi agar tidak tabrakan dengan code frekuensi: broadband subscription 

total_data = len(df2['Celullar Subscription']) # len() Menghitung jumlah total data
frekuensi_relatif = (frekuensi_data / total_data) * 100

print(f"Frekuensi Relatif: {frekuensi_relatif}")
print("\n")

frekuensi_data = df2['Internet Users(%)'].value_counts().sort_index() #dipanggil lagi agar tidak tabrakan dengan code frekuensi: broadband subscription 

total_data = len(df2['Internet Users(%)']) # len() Menghitung jumlah total data
frekuensi_relatif = (frekuensi_data / total_data) * 100

print(f"Frekuensi Relatif: {frekuensi_relatif}")
print("\n")

frekuensi_data = df2['No. of Internet Users'].value_counts().sort_index() #dipanggil lagi agar tidak tabrakan dengan code frekuensi: broadband subscription 

total_data = len(df2['No. of Internet Users']) # len() Menghitung jumlah total data
frekuensi_relatif = (frekuensi_data / total_data) * 100

print(f"Frekuensi Relatif: {frekuensi_relatif}")
print("\n")

frekuensi_data = df2['Broadband Subscription'].value_counts().sort_index() #dipanggil lagi agar tidak tabrakan dengan code frekuensi: broadband subscription 

total_data = len(df2['Broadband Subscription']) # len() Menghitung jumlah total data
frekuensi_relatif = (frekuensi_data / total_data) * 100

print(f"Frekuensi Relatif: {frekuensi_relatif}")
print("\n")

# Frekuensi Kumulatif Kurang Dari
print("-----------FREKUENSI KUMULATIF KURANG DARI-----------")
print("\n")

frekuensi_data = df2['Celullar Subscription'].value_counts().sort_index()
frekuensi_kumulatif_kurang_dari = frekuensi_data.sort_index().cumsum() #cumsum = cumulatif sum (jumlah data kumulatif)

print(f"Frekuensi Kumulatif Kurang Dari: {frekuensi_kumulatif_kurang_dari}")
print("\n")

frekuensi_data = df2['Internet Users(%)'].value_counts().sort_index()
frekuensi_kumulatif_kurang_dari = frekuensi_data.sort_index().cumsum() #cumsum = cumulatif sum (jumlah data kumulatif)

print(f"Frekuensi Kumulatif Kurang Dari: {frekuensi_kumulatif_kurang_dari}")
print("\n")

frekuensi_data = df2['No. of Internet Users'].value_counts().sort_index()
frekuensi_kumulatif_kurang_dari = frekuensi_data.sort_index().cumsum() #cumsum = cumulatif sum (jumlah data kumulatif)

print(f"Frekuensi Kumulatif Kurang Dari: {frekuensi_kumulatif_kurang_dari}")
print("\n")

frekuensi_data = df2['Broadband Subscription'].value_counts().sort_index()
frekuensi_kumulatif_kurang_dari = frekuensi_data.sort_index().cumsum() #cumsum = cumulatif sum (jumlah data kumulatif)frekuensi_kumulatif_kurang_dari

print(f"Frekuensi Kumulatif Kurang Dari: {frekuensi_kumulatif_kurang_dari}")
print("\n")

# FREKUENSI RELATIF KOMULATIF KURANG DARI (%)
print("-----------FREKUENSI RELATIF KUMULATIF KURANG DARI-----------")
print("\n")

frekuensi_data = df2['Celullar Subscription'].value_counts().sort_index()
frekuensi_kumulatif_kurang_dari = frekuensi_data.sort_index().cumsum()
total_data = len(df2['Celullar Subscription'])

frekuensi_relatif_kumulatif_kurang_dari = (frekuensi_kumulatif_kurang_dari / total_data) * 100
print(f"Frekuensi Relatif Kumulatif Kurang Dari: {frekuensi_relatif_kumulatif_kurang_dari}")
print("\n")

frekuensi_data = df2['Internet Users(%)'].value_counts().sort_index()
frekuensi_kumulatif_kurang_dari = frekuensi_data.sort_index().cumsum()
total_data = len(df2['Internet Users(%)'])


frekuensi_relatif_kumulatif_kurang_dari = (frekuensi_kumulatif_kurang_dari / total_data) * 100
print(f"Frekuensi Relatif Kumulatif Kurang Dari: {frekuensi_relatif_kumulatif_kurang_dari}")
print("\n")

frekuensi_data = df2['No. of Internet Users'].value_counts().sort_index()
frekuensi_kumulatif_kurang_dari = frekuensi_data.sort_index().cumsum()
total_data = len(df2['No. of Internet Users'])

frekuensi_relatif_kumulatif_kurang_dari = (frekuensi_kumulatif_kurang_dari / total_data) * 100
print(f"Frekuensi Relatif Kumulatif Kurang Dari: {frekuensi_relatif_kumulatif_kurang_dari}")
print("\n")

frekuensi_data = df2['Broadband Subscription'].value_counts().sort_index()
frekuensi_kumulatif_kurang_dari = frekuensi_data.sort_index().cumsum()
total_data = len(df2['Broadband Subscription'])

frekuensi_relatif_kumulatif_kurang_dari = (frekuensi_kumulatif_kurang_dari / total_data) * 100
print(f"Frekuensi Relatif Kumulatif Kurang Dari: {frekuensi_relatif_kumulatif_kurang_dari}")
print("\n")

# Frekuensi kumulatif lebih dari
print("-----------FREKUENSI KUMULATIF LEBIH DARI-----------")
print("\n")

frekuensi_data = df2['Celullar Subscription'].value_counts().sort_index()
frekuensi_kumulatif_lebih_dari = frekuensi_data.sort_index()[::-1].cumsum()[::-1] #[::-1] artinya membalikkan

print(f"Frekuensi Kumulatif Lebih Dari: {frekuensi_kumulatif_lebih_dari}")
print("\n")

frekuensi_data = df2['Internet Users(%)'].value_counts().sort_index()
frekuensi_kumulatif_lebih_dari = frekuensi_data.sort_index()[::-1].cumsum()[::-1] #[::-1] artinya membalikkan

print(f"Frekuensi Kumulatif Lebih Dari: {frekuensi_kumulatif_lebih_dari}")
print("\n")

frekuensi_data = df2['No. of Internet Users'].value_counts().sort_index()
frekuensi_kumulatif_lebih_dari = frekuensi_data.sort_index()[::-1].cumsum()[::-1] #[::-1] artinya membalikkan

print(f"Frekuensi Kumulatif Lebih Dari: {frekuensi_kumulatif_lebih_dari}")
print("\n")

total_data = len(df2['Broadband Subscription'])
frekuensi_data = df2['Broadband Subscription'].value_counts().sort_index()
frekuensi_kumulatif_lebih_dari = frekuensi_data.sort_index()[::-1].cumsum()[::-1] #[::-1] artinya membalikkan

print(f"Frekuensi Kumulatif Lebih Dari: {frekuensi_kumulatif_lebih_dari}")
print("\n")

# Frekuensi Relatif Kumulatif Lebih Dari (%)
print("-----------FREKUENSI RELATIF KUMULATIF LEBIH DARI DARI-----------")
print("\n")

total_data = len(df2['Celullar Subscription'])
frekuensi_data = df2['Celullar Subscription'].value_counts().sort_index()
frekuensi_kumulatif_lebih_dari = frekuensi_data.sort_index()[::-1].cumsum()[::-1] / total_data * 100

print(f"Frekuensi Relatif Kumulatif Lebih Dari: {frekuensi_kumulatif_lebih_dari}")
print("\n")


total_data = len(df2['Internet Users(%)'])
frekuensi_data = df2['Internet Users(%)'].value_counts().sort_index()
frekuensi_kumulatif_lebih_dari = frekuensi_data.sort_index()[::-1].cumsum()[::-1] / total_data * 100

print(f"Frekuensi Relatif Kumulatif Lebih Dari: {frekuensi_kumulatif_lebih_dari}")
print("\n")


total_data = len(df2['No. of Internet Users'])
frekuensi_data = df2['No. of Internet Users'].value_counts().sort_index()
frekuensi_kumulatif_lebih_dari = frekuensi_data.sort_index()[::-1].cumsum()[::-1] / total_data * 100

print(f"Frekuensi Relatif Kumulatif Lebih Dari: {frekuensi_kumulatif_lebih_dari}")
print("\n")


total_data = len(df2['Broadband Subscription'])
frekuensi_data = df2['Broadband Subscription'].value_counts().sort_index()
frekuensi_kumulatif_lebih_dari = frekuensi_data.sort_index()[::-1].cumsum()[::-1] / total_data * 100


print(f"Frekuensi Relatif Kumulatif Lebih Dari: {frekuensi_kumulatif_lebih_dari}")
print("\n")


 # GRAFIK TABEL #
# Data frekuensi
frekuensi_data1 = df2['Celullar Subscription'].value_counts().sort_index()
frekuensi_data2 = df2['Internet Users(%)'].value_counts().sort_index()
frekuensi_data3 = df2['No. of Internet Users'].value_counts().sort_index()
frekuensi_data4 = df2['Broadband Subscription'].value_counts().sort_index()

# Label untuk sumbu X (misalnya, label interval)
labels1 = frekuensi_data1.index
labels2 = frekuensi_data2.index
labels3 = frekuensi_data3.index
labels4 = frekuensi_data4.index

# Data untuk sumbu Y (frekuensi)
values1 = frekuensi_data1.values
values2 = frekuensi_data2.values
values3 = frekuensi_data3.values
values4 = frekuensi_data4.values

# Membuat subplot dengan 2 baris dan 2 kolom
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.bar(labels1, values1)
plt.title('Grafik Frekuensi Cellular Subscription')
plt.xlabel('Interval')
plt.ylabel('Frekuensi')

plt.subplot(2, 2, 2)
plt.bar(labels2, values2)
plt.title('Grafik Frekuensi Internet Users(%)')
plt.xlabel('Interval')
plt.ylabel('Frekuensi')

plt.subplot(2, 2, 3)
plt.bar(labels3, values3)
plt.title('Grafik Frekuensi No. of Internet Users')
plt.xlabel('Interval')
plt.ylabel('Frekuensi')

plt.subplot(2, 2, 4)
plt.bar(labels4, values4)
plt.title('Grafik Frekuensi Broadband Subscription')
plt.xlabel('Interval')
plt.ylabel('Frekuensi')

plt.tight_layout()

# Menampilkan subplot
plt.show()

 ######## GRAFIK ORGILE (FREKUENSI KUMULATIF) ########

# Hitung frekuensi kumulatif kurang dari
frekuensi_kumulatif_kurang_dari1 = frekuensi_data1.cumsum()
frekuensi_kumulatif_kurang_dari2 = frekuensi_data2.cumsum()
frekuensi_kumulatif_kurang_dari3 = frekuensi_data3.cumsum()
frekuensi_kumulatif_kurang_dari4 = frekuensi_data4.cumsum()

# Hitung frekuensi kumulatif lebih dari 
frekuensi_kumulatif_lebih_dari1 = frekuensi_data1.sort_index()[::-1].cumsum()[::-1]
frekuensi_kumulatif_lebih_dari2 = frekuensi_data2.sort_index()[::-1].cumsum()[::-1] 
frekuensi_kumulatif_lebih_dari3 = frekuensi_data3.sort_index()[::-1].cumsum()[::-1] 
frekuensi_kumulatif_lebih_dari4 = frekuensi_data4.sort_index()[::-1].cumsum()[::-1] 

# Membuat plot ogive
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(frekuensi_kumulatif_kurang_dari1.index, frekuensi_kumulatif_kurang_dari1, marker='o', linestyle='-', label='Kumulatif Kurang Dari')
plt.plot(frekuensi_kumulatif_lebih_dari1.index, frekuensi_kumulatif_lebih_dari1, marker='o', linestyle='-', label='Kumulatif Lebih Dari')

plt.title('Celullar Subscription')
plt.xlabel('Interval')
plt.ylabel('Data')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(frekuensi_kumulatif_kurang_dari2.index, frekuensi_kumulatif_kurang_dari2, marker='o', linestyle='-', label='Kumulatif Kurang Dari')
plt.plot(frekuensi_kumulatif_lebih_dari2.index, frekuensi_kumulatif_lebih_dari2, marker='o', linestyle='-', label='Kumulatif Lebih Dari')

plt.title('Internet Users(%)')
plt.xlabel('Interval')
plt.ylabel('Data')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(frekuensi_kumulatif_kurang_dari3.index, frekuensi_kumulatif_kurang_dari3, marker='o', linestyle='-', label='Kumulatif Kurang Dari')
plt.plot(frekuensi_kumulatif_lebih_dari3.index, frekuensi_kumulatif_lebih_dari3, marker='o', linestyle='-', label='Kumulatif Lebih Dari')

plt.title('No. of Internet Users')
plt.xlabel('Interval')
plt.ylabel('Data')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(frekuensi_kumulatif_kurang_dari4.index, frekuensi_kumulatif_kurang_dari4, marker='o', linestyle='-', label='Kumulatif Kurang Dari')
plt.plot(frekuensi_kumulatif_lebih_dari4.index, frekuensi_kumulatif_lebih_dari4, marker='o', linestyle='-', label='Kumulatif Lebih Dari')

plt.title('Broadband Subscription')
plt.xlabel('Interval')
plt.ylabel('Data')
plt.legend()
plt.grid(True)

# Menampilkan subplot
plt.tight_layout()
plt.show()

 ######## GRAFIK ORGILE (FREKUENSI RELATIF KUMULATIF) ########

# Menghitun total Data
total_data1 = len(df2['Celullar Subscription'])
total_data2 = len(df2['Internet Users(%)'])
total_data3 = len(df2['No. of Internet Users'])
total_data4 = len(df2['Broadband Subscription'])


# Hitung frekuensi kumulatif kurang dari
frekuensi_kumulatif_kurang_dari1 = frekuensi_data1.cumsum()
frekuensi_kumulatif_kurang_dari2 = frekuensi_data2.cumsum()
frekuensi_kumulatif_kurang_dari3 = frekuensi_data3.cumsum()
frekuensi_kumulatif_kurang_dari4 = frekuensi_data4.cumsum()

# Hitung frekuensi kumulatif lebih dari 
frekuensi_kumulatif_lebih_dari1 = frekuensi_data1.sort_index()[::-1].cumsum()[::-1]
frekuensi_kumulatif_lebih_dari2 = frekuensi_data2.sort_index()[::-1].cumsum()[::-1] 
frekuensi_kumulatif_lebih_dari3 = frekuensi_data3.sort_index()[::-1].cumsum()[::-1] 
frekuensi_kumulatif_lebih_dari4 = frekuensi_data4.sort_index()[::-1].cumsum()[::-1] 

# Hitung frekuensi relatif kumulatif kurang dari
frekuensi_relatif_kumulatif_kurang_dari1 = (frekuensi_kumulatif_kurang_dari1 / total_data1) * 100
frekuensi_relatif_kumulatif_kurang_dari2 = (frekuensi_kumulatif_kurang_dari2 / total_data2) * 100
frekuensi_relatif_kumulatif_kurang_dari3 = (frekuensi_kumulatif_kurang_dari3 / total_data3) * 100
frekuensi_relatif_kumulatif_kurang_dari4 = (frekuensi_kumulatif_kurang_dari4 / total_data4) * 100

# Hitung frekuensi relatif kumulatif lebih dari
frekuensi_relatif_kumulatif_lebih_dari1 = (frekuensi_kumulatif_lebih_dari1 / total_data1) * 100
frekuensi_relatif_kumulatif_lebih_dari2 = (frekuensi_kumulatif_lebih_dari2 / total_data2) * 100
frekuensi_relatif_kumulatif_lebih_dari3 = (frekuensi_kumulatif_lebih_dari3 / total_data3) * 100
frekuensi_relatif_kumulatif_lebih_dari4 = (frekuensi_kumulatif_lebih_dari4 / total_data4) * 100

# Membuat plot ogive
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(frekuensi_relatif_kumulatif_kurang_dari1.index, frekuensi_relatif_kumulatif_kurang_dari1, marker='o', linestyle='-', label='Relatif Kumulatif Kurang Dari')
plt.plot(frekuensi_relatif_kumulatif_lebih_dari1.index, frekuensi_relatif_kumulatif_lebih_dari1, marker='o', linestyle='-', label='Relatif Kumulatif Lebih Dari')

plt.title('Celullar Subscription')
plt.xlabel('Interval')
plt.ylabel('Data')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(frekuensi_relatif_kumulatif_kurang_dari2.index, frekuensi_relatif_kumulatif_kurang_dari2, marker='o', linestyle='-', label='Relatif Kumulatif Kurang Dari')
plt.plot(frekuensi_relatif_kumulatif_lebih_dari2.index, frekuensi_relatif_kumulatif_lebih_dari2, marker='o', linestyle='-', label=' Relatif Kumulatif Lebih Dari')

plt.title('Internet Users(%)')
plt.xlabel('Interval')
plt.ylabel('Data')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(frekuensi_relatif_kumulatif_kurang_dari3.index, frekuensi_relatif_kumulatif_kurang_dari3, marker='o', linestyle='-', label='Relatif Kumulatif Kurang Dari')
plt.plot(frekuensi_relatif_kumulatif_lebih_dari3.index, frekuensi_relatif_kumulatif_lebih_dari3, marker='o', linestyle='-', label='Relatif Kumulatif Lebih Dari')

plt.title('No. of Internet Users')
plt.xlabel('Interval')
plt.ylabel('Data')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(frekuensi_relatif_kumulatif_kurang_dari4.index, frekuensi_relatif_kumulatif_kurang_dari4, marker='o', linestyle='-', label='Relatif Kumulatif Kurang Dari')
plt.plot(frekuensi_relatif_kumulatif_lebih_dari4.index, frekuensi_relatif_kumulatif_lebih_dari4, marker='o', linestyle='-', label=' Relatif Kumulatif Lebih Dari')

plt.title('Broadband Subscription')
plt.xlabel('Interval')
plt.ylabel('Data')
plt.legend()
plt.grid(True)

# Menampilkan subplot
plt.tight_layout()
plt.show()
