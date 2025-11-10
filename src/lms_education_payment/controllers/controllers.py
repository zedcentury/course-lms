# -*- coding: utf-8 -*-
# from odoo import http


# class EducationPayment(http.Controller):
#     @http.route('/education_payment/education_payment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/education_payment/education_payment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('education_payment.listing', {
#             'root': '/education_payment/education_payment',
#             'objects': http.request.env['education_payment.education_payment'].search([]),
#         })

#     @http.route('/education_payment/education_payment/objects/<model("education_payment.education_payment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('education_payment.object', {
#             'object': obj
#         })

