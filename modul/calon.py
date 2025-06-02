class CalonManager:
    def __init__(self):
        self.calon_list = []

    def tambah_calon(self, id, nama, visi):
        if any(c['id'] == id for c in self.calon_list):
            raise ValueError(f"ID Calon '{id}' sudah ada!")
        self.calon_list.append({
            "id": id,
            "nama": nama,
            "visi": visi,
            "jumlah_suara": 0
        })

    def validasi_calon(self, id):
        return any(c['id'] == id for c in self.calon_list)

    def tambah_suara(self, id):
        for c in self.calon_list:
            if c['id'] == id:
                c['jumlah_suara'] += 1
                return
        raise ValueError(f"ID Calon '{id}' tidak ditemukan!")

    def tampilkan_semua(self):
        if not self.calon_list:
            print("Belum ada data calon.")
            return
        print("\nData Calon Ketua dan Jumlah Suara:")
        print(f"{'ID':<10} {'Nama':<20} {'Visi':<30} {'Suara':<6}")
        print("-" * 70)
        for c in self.calon_list:
            print(f"{c['id']:<10} {c['nama']:<20} {c['visi']:<30} {c['jumlah_suara']:<6}")
        print("-" * 70)
