from odoo import models, fields


class GroupStudent(models.Model):
    _name = "le.group.student"
    _description = "Group Student"

    group_id = fields.Many2one("le.group", string="Group", required=True)
    student_id = fields.Many2one("res.users", string="Student", required=True)
    status = fields.Selection([
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("frozen", "Frozen")
    ], string="Status", required=True, default="inactive")
