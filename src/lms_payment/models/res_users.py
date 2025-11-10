from odoo import models, fields


class Users(models.Model):
    _inherit = "res.users"

    payment_ids = fields.One2many("lp.payment", "user_id", string="Payments")
