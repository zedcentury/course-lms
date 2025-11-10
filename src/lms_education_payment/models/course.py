from odoo import models, fields


class Course(models.Model):
    _inherit = "le.course"

    payment_ids = fields.One2many("lp.payment", "course_id")
    payment_count = fields.Integer(compute="_compute_payment_count")

    def _compute_payment_count(self):
        for record in self:
            record.payment_count = len(record.payment_ids)

    def action_view_payments(self):
        self.ensure_one()

        if self.payment_count == 0:
            return

        if self.payment_count == 1:
            payment = self.payment_ids[0]

            return {
                "name": payment.display_name,
                "type": "ir.actions.act_window",
                "res_model": "payment.payment",
                "res_id": payment.id,
                "view_mode": "form",
                "target": "current"
            }

        return {
            "name": "Payments",
            "type": "ir.actions.act_window",
            "res_model": "payment.payment",
            "view_mode": "list,form",
            "target": "current",
            "domain": [("course_id", "=", self.id)],
        }
