from odoo import models, fields, api,_


class Peminjaman(models.Model):
    _name = 'myoutsource.peminjaman'
    _description = 'Peminjaman Fasilitas dari pegawai internal My Outsource'

    name = fields.Char(string='Kode Peminjaman', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    tanggal_pinjam = fields.Date(string="Tanggal Pinjam")
    tanggal_kembali = fields.Date(string="Tanggal Dikembalikan")
    peminjam_id = fields.Many2one('myoutsource.pegawai', string='Peminjam',required=True,domain="[('is_internal','ilike',True)]")
    fasilitas_id = fields.Many2one('myoutsource.fasilitas', string='Fasilitas yang Dipinjam', required=True)
    status_pinjam = fields.Selection([
        ('draft', 'Draft'),
        ('on progress', 'On Progress'),
        ('done', 'Done'),
    ], default="draft",string='Status Peminjaman')

    @api.model
    def create(self,vals):
        if vals.get('name',_('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('myoutsource.peminjaman') or _('New')
        res = super(Peminjaman,self).create(vals)
        return res