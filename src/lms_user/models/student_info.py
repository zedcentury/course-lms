from odoo import models, fields


class StudentInfo(models.AbstractModel):
    _name = "lu.student.info"
    _description = "Student Info"

    student_number = fields.Char()
