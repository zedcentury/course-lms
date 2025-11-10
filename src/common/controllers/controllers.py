# -*- coding: utf-8 -*-
# from odoo import http


# class LmsCommon(http.Controller):
#     @http.route('/lms_common/lms_common', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lms_common/lms_common/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lms_common.listing', {
#             'root': '/lms_common/lms_common',
#             'objects': http.request.env['lms_common.lms_common'].search([]),
#         })

#     @http.route('/lms_common/lms_common/objects/<model("lms_common.lms_common"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lms_common.object', {
#             'object': obj
#         })

