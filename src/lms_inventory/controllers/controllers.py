# -*- coding: utf-8 -*-
# from odoo import http


# class LmsInventory(http.Controller):
#     @http.route('/lms_inventory/lms_inventory', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lms_inventory/lms_inventory/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lms_inventory.listing', {
#             'root': '/lms_inventory/lms_inventory',
#             'objects': http.request.env['lms_inventory.lms_inventory'].search([]),
#         })

#     @http.route('/lms_inventory/lms_inventory/objects/<model("lms_inventory.lms_inventory"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lms_inventory.object', {
#             'object': obj
#         })

