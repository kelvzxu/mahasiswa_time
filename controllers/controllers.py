# -*- coding: utf-8 -*-
# from odoo import http


# class MahasiswaTime(http.Controller):
#     @http.route('/mahasiswa_time/mahasiswa_time', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mahasiswa_time/mahasiswa_time/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mahasiswa_time.listing', {
#             'root': '/mahasiswa_time/mahasiswa_time',
#             'objects': http.request.env['mahasiswa_time.mahasiswa_time'].search([]),
#         })

#     @http.route('/mahasiswa_time/mahasiswa_time/objects/<model("mahasiswa_time.mahasiswa_time"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mahasiswa_time.object', {
#             'object': obj
#         })
