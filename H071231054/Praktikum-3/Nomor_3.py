# Cetak selamat pagi, Selamat Siang, Selamat Sore, Selamat Malam berdasarkan waktunya

derajat = float(input())

total_menit = int( derajat * 240 + 21600 ) % 864000
if total_menit >= (24*3600):
    total_menit = total_menit - 21600
jam = total_menit // 3600
menit = total_menit % 3600 // 60
detik = total_menit % 60

if jam >= 24:
    jam -= 24

waktu = "{:02d}:{:02d}:{:02d}".format(int(jam), int(menit), int(detik))

if jam >= 0 and jam < 6:
    print("Selamat Malam," )
    print(waktu)
elif jam >= 6 and jam < 12:
    print("Selamat Pagi")
    print(waktu)
elif jam >= 12 and jam < 15:
    print("Selamat Siang,")
    print(waktu)
elif jam >= 15 and jam < 18:
    print("Selamat Sore")
    print(waktu)
else:
    print("Selamat Malam,")
    print(waktu)