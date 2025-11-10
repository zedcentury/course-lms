from odoo import models, fields


class WorkerInfo(models.AbstractModel):
    _name = "lu.worker.info"
    _description = "Worker Info"

    experience_years = fields.Integer()
    worked_places = fields.Text()
