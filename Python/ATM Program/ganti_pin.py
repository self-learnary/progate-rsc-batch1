from transaksi import Transaksi
import mydict


class gantiPin(Transaksi):
    def info(self):
        return self.namatr

    def isi(self):
        pin_baru = int(input("Masukkan Nomor Pin Baru : "))
        mydict.atm.pop(self.pin)
        mydict.atm = {pin_baru: [self.nama, str(self.saldo)]}
        return "Nomor Pin dengan nama " + mydict.atm[pin_baru][0] + " Berhasil Diubah ke " + str(pin_baru)
