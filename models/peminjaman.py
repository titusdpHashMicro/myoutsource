from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class Peminjaman(models.Model):
    _name = 'myoutsource.peminjaman'
    _description = 'Peminjaman Fasilitas dari pegawai internal My Outsource'
    _inherit =['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Kode Peminjaman', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    tanggal_pinjam = fields.Date(string="Tanggal Pinjam", tracking=True)
    tanggal_kembali = fields.Date(string="Tanggal Dikembalikan", tracking=True)
    peminjam_id = fields.Many2one('myoutsource.pegawai', string='Peminjam',required=True,domain="[('is_internal','ilike',True)]")
    fasilitas_id = fields.Many2one('myoutsource.fasilitas', string='Fasilitas yang Dipinjam', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('on progress', 'On Progress'),
        ('done', 'Done'),
    ], default="draft",string='Status Peminjaman', tracking=True)

    @api.model
    def create(self,vals):
        if vals.get('name',_('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('myoutsource.peminjaman') or _('New')
        res = super(Peminjaman,self).create(vals)
        return res
    
    def set_to_draft(self):
        for rec in self:
            rec['state'] = 'draft'
    
    def set_to_onprogress(self):
        for rec in self:
            if rec['tanggal_pinjam'] :
                if rec['fasilitas_id']['stok'] > rec['fasilitas_id']['jumlah_terpinjam']:
                    rec['fasilitas_id']['jumlah_terpinjam'] += 1
                    rec['state'] = 'on progress'
                else:
                    raise ValidationError("Stok fasilitas sudah habis !")
            else :
                raise ValidationError("Tentukan tanggal peminjaman !")
    
    def set_to_done(self):
        for rec in self:
            if rec['tanggal_kembali'] :
                rec['fasilitas_id']['jumlah_terpinjam'] -= 1
                rec['state'] = 'done'
            else :
                raise ValidationError("Tentukan tanggal pengembalian !")
