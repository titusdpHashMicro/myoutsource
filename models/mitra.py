from odoo import models, fields, api,_


class Mitra(models.Model):
    _name = 'myoutsource.mitra'
    _description = 'Mitra dari My Out Source'

    name = fields.Char(string="Nama Lengkap")
    alamat = fields.Char(string="Alamat")
    kode_mitra = fields.Char(string='Kode Mitra', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    deskripsi = fields.Char(string="Deskripsi")

    email = fields.Char(string="Email")
    no_telp = fields.Char(string="Nomor Telepon")

    total_gaji = fields.Integer(string="Total Gaji")
    poutsource_ids = fields.One2many('myoutsource.pegawai', 'mitra_id', string='Pegawai Outsource')
    supervisor_ids = fields.One2many('myoutsource.supervisor', 'company_id', string='Supervisor')

    @api.model
    def create(self,vals):
        if vals.get('kode_mitra',_('New')) == _('New'):
            vals['kode_mitra'] = self.env['ir.sequence'].next_by_code('myoutsource.mitra') or _('New')
        res = super(Mitra,self).create(vals)
        return res