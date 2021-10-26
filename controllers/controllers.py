# -*- coding: utf-8 -*-
# from odoo import http


# class Myoutsource/(http.Controller):
#     @http.route('/myoutsource//myoutsource//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myoutsource//myoutsource//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('myoutsource/.listing', {
#             'root': '/myoutsource//myoutsource/',
#             'objects': http.request.env['myoutsource/.myoutsource/'].search([]),
#         })

#     @http.route('/myoutsource//myoutsource//objects/<model("myoutsource/.myoutsource/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myoutsource/.object', {
#             'object': obj
#         })
