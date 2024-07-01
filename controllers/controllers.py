# -*- coding: utf-8 -*-
# from odoo import http


# class Box(http.Controller):
#     @http.route('/box/box', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/box/box/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('box.listing', {
#             'root': '/box/box',
#             'objects': http.request.env['box.box'].search([]),
#         })

#     @http.route('/box/box/objects/<model("box.box"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('box.object', {
#             'object': obj
#         })

from odoo import http
from odoo.http import request

class BoxController(http.Controller):

    @http.route('/box/admin', type='http', auth='user', website=True)
    def admin_page(self, **kwargs):
        return request.render('box.box_admin_form')

    @http.route('/box/operario', type='http', auth='user', website=True)
    def operario_page(self, **kwargs):
        normativas = request.env['box.normativa'].search([])
        return request.render('box.box_user_form', {'normativas': normativas})