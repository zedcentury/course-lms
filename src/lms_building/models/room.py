from odoo import models, fields


class Room(models.Model):
    _name = "lb.room"
    _description = "Room"

    name = fields.Char(string="Name", required=True)
    building_id = fields.Many2one("lb.building", string="Building", required=True)
    floor_id = fields.Many2one("lb.floor", string="Floor", required=True)
