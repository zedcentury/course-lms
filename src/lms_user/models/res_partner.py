from odoo import models, fields


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = ["res.partner", "lu.teacher.info", "lu.student.info"]

    user_type = fields.Selection([
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("manager", "Manager"),
    ])
