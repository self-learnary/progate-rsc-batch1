import time
import mydict
from cek_saldo import cekSaldo
from tarik_saldo import tarikSaldo
from transfer_saldo import transferSaldo
from ganti_pin import gantiPin

print("PROGRAM ATM".center(50, "-"))
print("Created by : Rafli Surya P".center(50))
print(50*"-" + "\n")
print("Masukkan Kartu Anda Disini")
print("Tunggu Sebentar...")
time.sleep(1.5)
print("Kartu berhasil masuk")

# ambil nomor pin dari index atm
pins = []
for no_pin in mydict.atm:
    pins.append(no_pin)

pin = int(input("Masukkan nomor pin (wajib angka) : "))

# cek pin yg dimasukkan benar atau tidak
if pin in pins:
    print("Pilih transaksi yang akan dilakukan : ")
    # atm[pin][0], atm[pin][1]
    transaksi1 = cekSaldo(
        "Cek Saldo", mydict.atm[pin][0], mydict.atm[pin][1], pin)
    transaksi2 = tarikSaldo(
        "Tarik Saldo", mydict.atm[pin][0], mydict.atm[pin][1], pin)
    transaksi3 = transferSaldo(
        "Transfer Saldo", mydict.atm[pin][0], mydict.atm[pin][1], pin)
    transaksi4 = gantiPin(
        "Ganti Pin", mydict.atm[pin][0], mydict.atm[pin][1], pin)

    list_transaksi = [transaksi1, transaksi2, transaksi3, transaksi4]

    index = 0
    for this_transaksi in list_transaksi:
        print(str(index) + '. ' + this_transaksi.info())
        index += 1

    print(20*"-")

    no_transaksi = int(input('Masukkan nomor transaksi: '))
    selected_transaksi = list_transaksi[no_transaksi]

    result = selected_transaksi.isi()

    print(result)
else:
    print("Pin yang anda masukkan salah!, coba lagi")
