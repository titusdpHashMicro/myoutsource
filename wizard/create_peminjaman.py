from odoo import models, fields, api, _


class CreatePeminjaman(models.TransientModel):
    _name = 'create.peminjaman.wizard'
    _description = 'Create Peminjaman'

    emp_id = fields.Many2one('myoutsource.pegawai', string='Pegawai Internal',required=True,domain="[('is_internal','ilike',True)]")
    flts_id = fields.Many2one('myoutsource.fasilitas', string='Fasilitas',required=True)

    def create_peminjaman_action(self):
        vals = {
            'peminjam_id': self.emp_id.id,
            'fasilitas_id': self.flts_id.id
        }
        self.env['myoutsource.peminjaman'].create(vals)
