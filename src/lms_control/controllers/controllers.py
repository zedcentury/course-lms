# -*- coding: utf-8 -*-
# from odoo import http


# class LmsControl(http.Controller):
#     @http.route('/lms_control/lms_control', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lms_control/lms_control/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lms_control.listing', {
#             'root': '/lms_control/lms_control',
#             'objects': http.request.env['lms_control.lms_control'].search([]),
#         })

#     @http.route('/lms_control/lms_control/objects/<model("lms_control.lms_control"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lms_control.object', {
#             'object': obj
#         })

