# -*- coding: utf-8 -*-
# from odoo import http


# class Encuestas(http.Controller):
#     @http.route('/encuestas/encuestas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/encuestas/encuestas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('encuestas.listing', {
#             'root': '/encuestas/encuestas',
#             'objects': http.request.env['encuestas.encuestas'].search([]),
#         })

#     @http.route('/encuestas/encuestas/objects/<model("encuestas.encuestas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('encuestas.object', {
#             'object': obj
#         })
