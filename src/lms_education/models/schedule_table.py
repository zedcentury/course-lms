from odoo import models, fields, api


class ScheduleTable(models.Model):
    _name = "le.schedule.table"
    _description = "Schedule Table"

    name = fields.Char(string="Name", required=True)
    group_id = fields.Many2one("le.group", string="Group", required=True)
    schedule_lesson_ids = fields.One2many("le.schedule.lesson", "schedule_table_id", string="Schedule Lessons")

    teacher_id = fields.Many2one("res.users", string="Teacher", required=True)

    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", compute="_compute_end_date")
    weekday_ids = fields.Many2many("common.weekday", string="Weekdays", required=True)
    lesson_start_time = fields.Float(string="Start Time", required=True)
    lesson_end_time = fields.Float(string="End Time", required=True)

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)

        for record in records:
            for lesson in record.group_id.course_id.lesson_ids:
                lesson_date = False

                self.env["le.schedule.lesson"].create({
                    "name": lesson.name,
                    "schedule_table_id": record.id,
                    "lesson_date": lesson_date,
                    "lesson_start_time": record.lesson_start_time,
                    "lesson_end_time": record.lesson_end_time,
                })

        return records

    def _compute_end_date(self):
        for record in self:
            record.end_date = record.schedule_lesson_ids.sorted(lambda x: x.lesson_date)[-1].lesson_date
