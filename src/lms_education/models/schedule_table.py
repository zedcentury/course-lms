from odoo import models, fields


class ScheduleTable(models.Model):
    _name = "le.schedule.table"
    _description = "Schedule Table"

    name = fields.Char(string="Name", required=True)
    group_id = fields.Many2one("le.group", string="Group", required=True)
    schedule_lesson_ids = fields.One2many("le.schedule.lesson", "schedule_table_id", string="Schedule Lessons")

    teacher_id = fields.Many2one("res.users", string="Teacher", required=True)

    start_date = fields.Date(string="Start Date", required=True)
    weekday_ids = fields.Many2many("common.weekday", string="Weekdays", required=True)
    lesson_start_time = fields.Float(string="Start Time", required=True)
    lesson_end_time = fields.Float(string="End Time", required=True)
