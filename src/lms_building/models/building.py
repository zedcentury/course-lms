from odoo import models, fields


class Building(models.Model):
    _name = "lb.building"
    _description = "Building"

    name = fields.Char(string="Name", required=True)
    company_id = fields.Many2one("res.company", string="Company", required=True, default=lambda self: self.env.user.company_id)
