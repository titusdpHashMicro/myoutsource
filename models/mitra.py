from odoo import models, fields, api,_


class Mitra(models.Model):
    _name = 'myoutsource.mitra'
    _description = 'Mitra dari My Out Source'

    name = fields.Char(string="Nama Lengkap")
    alamat = fields.Char(string="Alamat")
    kode_mitra = fields.Char(string="Kode Perusahaan")
    deskripsi = fields.Char(string="Deskripsi")

    email = fields.Char(string="Email")
    no_telp = fields.Char(string="Nomor Telepon")

    total_gaji = fields.Integer(string="Total Gaji")
    poutsource_ids = fields.One2many('myoutsource.pegawai', 'inverse_field_name', string='')

    @api.model
    def generate_kode_mitra(self,vals):
        if vals.get('kode_mitra',_('New')) == _('New'):
            vals['kode_mitra'] = self.env['ir.sequence'].next_by_code('kode.mitra') or _('New')
        res = super(Mitra,self).create(vals)
        return res