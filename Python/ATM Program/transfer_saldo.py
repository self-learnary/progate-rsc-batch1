from transaksi import Transaksi


class transferSaldo(Transaksi):
    def info(self):
        return self.namatr

    def isi(self):
        norek_penerima = input("Masukkan no rekening penerima : ")
        jml_transfer = int(
            input("Masukkan nominal uang yang akan ditransfer : (Minimal saldo untuk ditransfer Rp. 50000)"))
        sisa_saldo = self.saldo - jml_transfer

        return "Transfer kepada No Rekening " + norek_penerima + " Senilai Rp. " + str(jml_transfer) + " Telah berhasil, sisa saldo anda saat ini Rp. " + str(sisa_saldo)
