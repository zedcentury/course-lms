from odoo import models, fields


class Course(models.Model):
    """
    Full Stack Web Development
    """
    _name = "le.course"
    _description = "Course"

    name = fields.Char(string="Name", required=True)
    lesson_ids = fields.One2many("le.lesson", "course_id", string="Lessons")
    subject_ids = fields.Many2many("le.subject", string="Subjects")
