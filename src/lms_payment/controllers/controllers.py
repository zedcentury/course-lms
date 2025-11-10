# -*- coding: utf-8 -*-
# from odoo import http


# class Payment(http.Controller):
#     @http.route('/payment/payment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payment/payment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('payment.listing', {
#             'root': '/payment/payment',
#             'objects': http.request.env['payment.payment'].search([]),
#         })

#     @http.route('/payment/payment/objects/<model("payment.payment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payment.object', {
#             'object': obj
#         })

