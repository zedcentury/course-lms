# -*- coding: utf-8 -*-
# from odoo import http


# class Education(http.Controller):
#     @http.route('/education/education', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/education/education/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('education.listing', {
#             'root': '/education/education',
#             'objects': http.request.env['education.education'].search([]),
#         })

#     @http.route('/education/education/objects/<model("education.education"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('education.object', {
#             'object': obj
#         })

