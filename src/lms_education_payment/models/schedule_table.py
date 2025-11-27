from odoo import models, fields


class ScheduleTable(models.Model):
    _inherit = "le.schedule.table"

    payment_type = fields.Selection(selection=[
        ("per_lesson", "Per Lesson"),
        ("per_month", "Per Month"),
    ], string="Payment Type", required=True)

    price_per_lesson = fields.Float(string="Price per Lesson")
    price_per_month = fields.Float(string="Price per Month")
