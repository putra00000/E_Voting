class PemilihManager:
    def __init__(self):
        self.pemilih_list = []

    def tambah_pemilih(self, id, nama, jurusan):
        if any(p['id'] == id for p in self.pemilih_list):
            raise ValueError(f"ID Pemilih '{id}' sudah ada!")
        self.pemilih_list.append({
            "id": id,
            "nama": nama,
            "jurusan": jurusan,
            "sudah_memilih": False
        })

    def validasi_pemilih(self, id):
        return any(p['id'] == id for p in self.pemilih_list)

    def sudah_memilih(self, id):
        for p in self.pemilih_list:
            if p['id'] == id:
                return p['sudah_memilih']
        return False

    def set_sudah_memilih(self, id):
        for p in self.pemilih_list:
            if p['id'] == id:
                p['sudah_memilih'] = True
                return
        raise ValueError(f"ID Pemilih '{id}' tidak ditemukan!")
