from odoo import models, fields


class Payment(models.Model):
    _inherit = "lp.payment"

    detailed_type = fields.Selection(selection_add=[
        ("lesson_payment", "Lesson Payment"),
    ])
    schedule_student_lesson_id = fields.Many2one("le.schedule.student.lesson", string="ScheduleStudentLesson")
