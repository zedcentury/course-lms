# -*- coding: utf-8 -*-
# from odoo import http


# class LmsBuilding(http.Controller):
#     @http.route('/lms_building/lms_building', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lms_building/lms_building/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lms_building.listing', {
#             'root': '/lms_building/lms_building',
#             'objects': http.request.env['lms_building.lms_building'].search([]),
#         })

#     @http.route('/lms_building/lms_building/objects/<model("lms_building.lms_building"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lms_building.object', {
#             'object': obj
#         })

