from odoo import models, fields


class Lesson(models.Model):
    """
    Print function
    """
    _name = "le.lesson"
    _description = "Lesson"

    name = fields.Char(string="Name", required=True)
    course_id = fields.Many2one("le.course", string="Course", required=True)
    homework_ids = fields.One2many("le.homework", "lesson_id", string="Homeworks")
