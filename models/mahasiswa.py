from odoo import models, fields, api


class Mahasiswa(models.Model):
    _name = 'res.mahasiswa'
    _description = 'Data Mahasiswa'

    name = fields.Char()
    nim = fields.Char()
    address_home_id = fields.Many2one('res.partner', string="Address")
    description = fields.Text() 



#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
