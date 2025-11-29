from odoo import models, fields


class TeacherInfo(models.AbstractModel):
    _name = "lu.teacher.info"
    _description = "Teacher Info"

    experience_years = fields.Integer()
    worked_places = fields.Text()
