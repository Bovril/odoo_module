# -*- coding: utf-8 -*-
from openerp import http

class HrRecruting(http.Controller):
    @http.route('/hr_recruting/hr_recruting/', auth='public')
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/hr_recruting/hr_recruting/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_recruting.listing', {
#             'root': '/hr_recruting/hr_recruting',
#             'objects': http.request.env['hr_recruting.hr_recruting'].search([]),
#         })

#     @http.route('/hr_recruting/hr_recruting/objects/<model("hr_recruting.hr_recruting"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_recruting.object', {
#             'object': obj
#         })