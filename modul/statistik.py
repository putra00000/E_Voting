class StatistikManager:
    def __init__(self, pemilih_manager, calon_manager):
        self.pm = pemilih_manager
        self.cm = calon_manager

    def total_pemilih(self):
        return len(self.pm.pemilih_list)

    def jumlah_yang_memilih(self):
        return sum(1 for p in self.pm.pemilih_list if p['sudah_memilih'])

    def persentase_partisipasi(self):
        total = self.total_pemilih()
        if total == 0:
            return 0
        return (self.jumlah_yang_memilih() / total) * 100

    def calon_terbanyak(self):
        if not self.cm.calon_list:
            return None
        max_suara = max(c['jumlah_suara'] for c in self.cm.calon_list)
        return [c for c in self.cm.calon_list if c['jumlah_suara'] == max_suara]

    def tampilkan_statistik(self):
        print("\nSTATISTIK PEMILU")
        print(f"Total Pemilih             : {self.total_pemilih()}")
        print(f"Jumlah yang sudah memilih : {self.jumlah_yang_memilih()}")
        print(f"Persentase partisipasi    : {self.persentase_partisipasi():.2f}%")
        pemenang = self.calon_terbanyak()
        if not pemenang:
            print("Belum ada calon yang terdaftar.")
        elif len(pemenang) == 1:
            c = pemenang[0]
            print(f"Calon dengan suara terbanyak: {c['nama']} (ID: {c['id']}) dengan {c['jumlah_suara']} suara.")
        else:
            print("Terdapat beberapa calon dengan jumlah suara terbanyak (seri):")
            for c in pemenang:
                print(f"- {c['nama']} (ID: {c['id']}) dengan {c['jumlah_suara']} suara.")
