from odoo import models, fields, api, _


class Supervisor(models.Model):
    _name = 'myoutsource.supervisor'
    _description = 'Supervisor dari mitra'

    name = fields.Char(string="Nama Lengkap")
    nik = fields.Char(string="NIK")
    kode_supervisor = fields.Char(string='Kode Supervisor', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    email = fields.Char(string="Email")
    no_telp = fields.Char(string="Nomor Telepon")
    total_pegawai = fields.Integer(string='Total Pegawai')
    company_id = fields.Many2one('myoutsource.mitra', string='Company', delegate=True)
    pegawai_ids = fields.One2many('myoutsource.pegawai', 'supervisor_id', string='Pegawai Dalam Pengawasan')

    @api.model
    def create(self,vals):
        if vals.get('kode_supervisor',_('New')) == _('New'):
            vals['kode_supervisor'] = self.env['ir.sequence'].next_by_code('myoutsource.supervisor') or _('New')
        res = super(Supervisor,self).create(vals)
        return res
