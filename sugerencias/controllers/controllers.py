# -*- coding: utf-8 -*-
# from odoo import http


# class Sugerencias(http.Controller):
#     @http.route('/sugerencias/sugerencias', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sugerencias/sugerencias/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sugerencias.listing', {
#             'root': '/sugerencias/sugerencias',
#             'objects': http.request.env['sugerencias.sugerencias'].search([]),
#         })

#     @http.route('/sugerencias/sugerencias/objects/<model("sugerencias.sugerencias"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sugerencias.object', {
#             'object': obj
#         })
