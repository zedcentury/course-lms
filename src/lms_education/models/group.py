from odoo import models, fields


class Group(models.Model):
    """
    FSWD - 1
    """
    _name = "le.group"
    _description = "Group"

    name = fields.Char(string="Name", required=True)
    course_id = fields.Many2one("le.course", string="Course", required=True)
    student_ids = fields.One2many("le.group.student", "group_id", string="Students")
    schedule_table_ids = fields.One2many("le.schedule.table", "group_id", string="Schedule Tables")

    def action_view_schedule_lessons(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "le.schedule.lesson",
            "view_mode": "list,form",
            "domain": [
                ("schedule_table_id", "in", self.schedule_table_ids.ids)
            ]
        }
