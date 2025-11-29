from odoo import models, fields


class Users(models.Model):
    _inherit = "res.users"

    payment_ids = fields.One2many("lp.payment", "student_id", string="Payments")
    balance = fields.Float("Balance", compute="_compute_balance")

    def _compute_balance(self):
        for record in self:
            payments = self.env["lp.payment"].search([("student_id", "=", record.id), ("state", "=", "confirmed")])

            top_up_amount = 0
            refund_amount = 0

            for payment in payments:
                if payment.detailed_type == "top_up_balance":
                    top_up_amount += payment.amount
                elif payment.detailed_type == "refund":
                    refund_amount += payment.amount

            record.balance = top_up_amount - refund_amount

    def action_view_balance_history(self):
        self.ensure_one()

        return {
            "type": "ir.actions.act_window",
            "res_model": "lp.payment",
            "view_mode": "list,form",
            "domain": [
                ("student_id", "=", self.id),
            ]
        }
