from odoo import models, fields


class Users(models.Model):
    _inherit = "res.users"

    user_type = fields.Selection([
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("manager", "Manager"),
    ])
