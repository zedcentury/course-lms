from odoo import models, fields


class ScheduleStudentLesson(models.Model):
    _name = "le.schedule.student.lesson"
    _description = "ScheduleStudentLesson"

    schedule_lesson_id = fields.Many2one("le.schedule.lesson", string="Schedule")
    student_id = fields.Many2one("res.users", string="Student")
    participated = fields.Boolean(string="Participated", default=False)
