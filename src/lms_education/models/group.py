from odoo import models, fields


class Group(models.Model):
    """
    FSWD - 1
    """
    _name = "le.group"
    _description = "Group"

    name = fields.Char(string="Name", required=True)
    course_id = fields.Many2one("le.course", string="Course", required=True)
