# -*- coding: utf-8 -*-

import re
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Pegawai(models.Model):
    _name = 'myoutsource.pegawai'
    _description = 'Pegawai dari My Outsource'
    _inherit =['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Nama Lengkap", required=True)
    nik = fields.Char(string="NIK", required=True)
    kode_pegawai = fields.Char(string='Kode Pegawai', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    umur = fields.Integer(string="Umur")
    role = fields.Char(string="Role", required=True)
    email = fields.Char(string="Email", required=True)
    no_telp = fields.Char(string="Nomor Telepon")
    gaji = fields.Integer(string="Gaji", tracking=True)
    is_internal = fields.Boolean(string='Pegawai Internal')
    is_outsource = fields.Boolean(string='Pegawai Outsource')
    pinjam_ids = fields.One2many('myoutsource.peminjaman', 'peminjam_id', string='Fasilitas Yang Dipinjam', readonly=True)

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

    state = fields.Selection([
        ('waiting', 'Waiting'),
        ('contract', 'Contract'),
        ('on work', 'On Work'),
        ('done', 'Done'),
        ('quit', 'Quit'),
    ], string='Status Contract', default='waiting', tracking=True)
    mitra_id = fields.Many2one('myoutsource.mitra', string='Mitra', tracking=True)
    supervisor_id = fields.Many2one('myoutsource.supervisor', string='Supervisor', tracking=True, domain="[('company_id','=',mitra_id)]")

    def set_to_draft(self):
        for rec in self:
            rec['state'] = 'waiting'
    
    def set_to_contract(self):
        for rec in self:
            if rec['mitra_id'] :
                rec['state'] = 'contract'
                print(rec['mitra_id'])
                print(rec['supervisor_id']['company_id'])
            else :
                raise ValidationError("Tentukan Perusahaan Mitra !")
    
    def set_to_onwork(self):
        for rec in self:
            if rec['supervisor_id']:
                if rec['gaji'] > 0:
                    rec['state'] = 'on work'
                else:
                    raise ValidationError("Tentukan Gaji !")
            else :
                raise ValidationError("Tentukan Supervisor !")

    def set_to_done(self):
        for rec in self:
            rec['state'] = 'done'
            rec['supervisor_id'] =None
            rec['mitra_id'] = None
    
    def set_to_quit(self):
        for rec in self:
            rec['state'] = 'quit'
            rec['supervisor_id'] =None
            rec['mitra_id'] = None

    