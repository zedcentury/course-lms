from odoo import models, fields


class Payment(models.Model):
    _name = "lp.payment"
    _description = "Payment"

    user_id = fields.Many2one("res.users", string="User")
    amount = fields.Float(string="Amount")
    payment_type = fields.Selection([
        ("card", "Card"),
        ("cash", "Cash"),
        ("online", "Online"),
    ], string="Payment Type", required=True, default="card")
    payment_date = fields.Date(string="Payment Date", default=fields.Date.today(), required=True)
