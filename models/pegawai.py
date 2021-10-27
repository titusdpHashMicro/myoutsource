# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Pegawai(models.Model):
    _name = 'myoutsource.pegawai'
    _description = 'Pegawai dari My Outsource'

    name = fields.Char(string="Nama Lengkap")
    nik = fields.Char(string="NIK")
    kode_pegawai = fields.Char(string='Kode Pegawai', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    umur = fields.Integer(string="Umur")
    role = fields.Char(string="Role")
    email = fields.Char(string="Email")
    no_telp = fields.Char(string="Nomor Telepon")
    gaji = fields.Integer(string="Gaji")
    is_internal = fields.Boolean(string='Pegawai Internal')
    is_outsource = fields.Boolean(string='Pegawai Outsource')
    pinjam_ids = fields.One2many('myoutsource.peminjaman', 'peminjam_id', string='Fasilitas Yang Dipinjam')

    @api.model
    def create(self,vals):
        if vals.get('is_internal') and vals.get('is_outsource') :
            raise ValidationError ("Tidak Boleh Memilih Lebih Satu Jenis Pegawai !")
        else:
            if vals.get('is_internal') :
                if vals.get('kode_pegawai',_('New')) == _('New'):
                    vals['kode_pegawai'] = self.env['ir.sequence'].next_by_code('myoutsource.pegawai.internal') or _('New')
            elif vals.get('is_outsource'):
                if vals.get('kode_pegawai',_('New')) == _('New'):
                    vals['kode_pegawai'] = self.env['ir.sequence'].next_by_code('myoutsource.pegawai.outsource') or _('New')
            else:
                raise ValidationError ("Pilih Salah Satu Jenis Pegawai !")
        res = super(Pegawai,self).create(vals)
        return res

class PegawaiOutsource(models.Model):
    _description = 'Pegawai Outsource dari My Outsource'
    _inherit = 'myoutsource.pegawai'

    status_contract = fields.Selection([
        ('waiting', 'Waiting'),
        ('contract', 'Contract'),
        ('on work', 'On Work'),
        ('done', 'Done'),
        ('quit', 'Quit'),
    ], string='Status Contract')
    mitra_id = fields.Many2one('myoutsource.mitra', string='Mitra', delegate=True)
    supervisor_id = fields.Many2one('myoutsource.supervisor', string='Supervisor', delegate=True)
    