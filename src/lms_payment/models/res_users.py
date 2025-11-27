from odoo import models, fields


class Users(models.Model):
    _inherit = "res.users"

    payment_ids = fields.One2many("lp.payment", "student_id", string="Payments")
    balance = fields.Float("Balance", compute="_compute_balance")

    def _compute_balance(self):
        for record in self:
            confirmed_payments = record.payment_ids.filtered(lambda x: x.state == "confirmed")
            record.balance = sum([confirmed_payment.amount for confirmed_payment in confirmed_payments])
