from odoo import models, fields


class Payment(models.Model):
    _inherit = "payment.payment"

    course_id = fields.Many2one("education.course")

    def action_view_course(self):
        self.ensure_one()

        return {
            "name": self.course_id.display_name,
            "type": "ir.actions.act_window",
            "res_model": "education.course",
            "res_id": self.course_id.id,
            "view_mode": "form",
            "target": "current"
        }
