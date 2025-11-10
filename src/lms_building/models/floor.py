from odoo import models, fields


class Floor(models.Model):
    _name = "lb.floor"
    _description = "Floor"

    name = fields.Char(string="Number", required=True)
    building_id = fields.Many2one("lb.building", string="Building", required=True)
