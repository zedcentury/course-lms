from odoo import models, fields, api


class ScheduleLesson(models.Model):
    _name = "le.schedule.lesson"
    _description = "Schedule Lesson"

    name = fields.Char(string="Name", required=True)
    schedule_table_id = fields.Many2one("le.schedule.table", string="Schedule", required=True)

    lesson_date = fields.Date(string="Lesson Date", required=True)
    lesson_start_time = fields.Float(string="Start Time", required=True)
    lesson_end_time = fields.Float(string="End Time", required=True)

    def get_lessons(self):
        if not self.id:
            raise ValueError("ABCD")

        self.name = "Asliddin"

    @api.constrains("lesson_start_time", "lesson_end_time", "lesson_date", "teacher_id")
    def _check_conflict(self):
        """
        Joriy dars kuni joriy o'qituvchiga dars vaqti konflikt bo'lib qolmasligi tekshirildi
        """

        for record in self:
            if self.env["le.schedule.lesson"].sudo().search_count([
                "&",
                ("lesson_date", "=", record.lesson_date),
                "&",
                ("teacher_id", "=", record.teacher_id.id),
                "|",
                "&",
                ("lesson_start_time", "<", record.lesson_start_time),
                ("lesson_end_time", ">", record.lesson_start_time),
                "&",
                ("lesson_start_time", "<", record.lesson_end_time),
                ("lesson_end_time", ">", record.lesson_end_time),
            ]) > 0:
                raise ValueError("Lesson Conflict")
