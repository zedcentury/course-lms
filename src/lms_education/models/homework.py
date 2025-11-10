from odoo import models, fields


class Homework(models.Model):
    _name = "le.homework"
    _description = "Homework"

    name = fields.Char(string="Name", required=True)
    lesson_id = fields.Many2one("le.lesson", string="Lesson", required=True)
