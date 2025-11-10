from odoo import models, fields


class ScheduleLesson(models.Model):
    _name = "le.schedule.lesson"
    _description = "Schedule Lesson"

    name = fields.Char(string="Name", required=True)
    schedule_table_id = fields.Many2one("le.schedule.table", string="Schedule", required=True)

    lesson_date = fields.Date(string="Lesson Date", required=True)
    lesson_start_time = fields.Float(string="Start Time", required=True)
    lesson_end_time = fields.Float(string="End Time", required=True)
