from odoo import models, fields


class Subject(models.Model):
    """
    Python, Django
    """
    _name = "le.subject"
    _description = "Subject"

    name = fields.Char(string="Name", required=True)
