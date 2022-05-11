from odoo import models,fields
class PtdYearFormat(models.Model):
    _inherit = 'res.lang'
    year = fields.Char(string="Year", require = True)
    month= fields.Char(string="Month", require = True)