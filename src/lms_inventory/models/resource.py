from odoo import models, fields


class Resource(models.Model):
    _name = "li.resource"
    _description = "Resource"

    name = fields.Char(string="Name", required=True)
    resource_type = fields.Selection([
        ('equipment', 'Equipment'),
        ('material', 'Material')
    ], string="Resource Type", required=True, default="equipment")
    quantity = fields.Float(string="Quantity", required=True)
    company_id = fields.Many2one("res.company", string="Company", required=True, default=lambda self: self.env.user.company_id)
