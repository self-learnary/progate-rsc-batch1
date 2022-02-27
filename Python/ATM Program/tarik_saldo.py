from transaksi import Transaksi


class tarikSaldo(Transaksi):
    def info(self):
        return self.namatr

    def isi(self):
        tarik = input(
            "Masukkan Nominal yang akan ditarik : (minimal penarikan Rp. 50000)")
        sisa_saldo = self.saldo - int(tarik)

        return "Saldo Rp. " + tarik + " berhasil ditarik, sisa saldo anda saat ini Rp. " + str(sisa_saldo)
