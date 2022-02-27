from transaksi import Transaksi


class cekSaldo(Transaksi):

    def info(self):
        return self.namatr

    def isi(self):
        return "Hai " + self.nama + " Jumlah saldo anda saat ini Rp." + str(self.saldo)
