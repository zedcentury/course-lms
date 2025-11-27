from odoo import models, fields


class ScheduleStudentLesson(models.Model):
    _inherit = "le.schedule.student.lesson"

    payment_ids = fields.One2many("lp.payment", "schedule_student_lesson_id")
