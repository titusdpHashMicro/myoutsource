from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class Fasilitas(models.Model):
    _name = 'myoutsource.fasilitas'
    _description = 'Fasilitas dari My Out Source'

    name = fields.Char(string="Nama Fasilitas", required=True)
    deskripsi = fields.Char(string='Deskripsi')
    kode_fasilitas = fields.Char(string='Kode Fasilitas', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    stok = fields.Integer(string='Stok', required=True)
    jumlah_terpinjam = fields.Integer(string='Dipinjam', readonly=True)
    peminjaman_ids = fields.One2many('myoutsource.peminjaman', 'fasilitas_id', string='Data Peminjaman',domain=lambda self:[('state','=','on progress')])

    @api.model
    def create(self,vals):
        if vals.get('kode_fasilitas',_('New')) == _('New'):
                vals['kode_fasilitas'] = self.env['ir.sequence'].next_by_code('myoutsource.fasilitas') or _('New')
        res = super(Fasilitas,self).create(vals)
        return res