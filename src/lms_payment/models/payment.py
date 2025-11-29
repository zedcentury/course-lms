from odoo import models, fields


class Payment(models.Model):
    _name = "lp.payment"
    _description = "Payment"

    user_id = fields.Many2one("res.users", string="User", default=lambda self: self.env.user)
    amount = fields.Float(string="Amount")
    payment_type = fields.Selection([
        ("card", "Card"),
        ("cash", "Cash"),
        ("online", "Online"),
    ], string="Payment Type", required=True, default="card")
    payment_date = fields.Date(string="Payment Date", default=fields.Date.today(), required=True)
    detailed_type = fields.Selection([
        ("top_up_balance", "Top Up Balance"),
        ("refund", "Refund"),
        ("expense", "Expense"),
    ], required=True)
    state = fields.Selection([
        ("draft", "Draft"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ], default="draft", required=True)

    student_id = fields.Many2one("res.users", string="Student")
    teacher_id = fields.Many2one("res.users", string="Teacher")

    def action_confirm(self):
        self.write({"state": "confirmed"})
