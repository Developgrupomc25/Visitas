# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from openerp import SUPERUSER_ID
from openerp.osv import fields, osv, orm
from datetime import time, datetime,timedelta
from openerp import tools
from tools.translate import _


class mrp_service_all(osv.osv):
    _name = 'mrp_service.all'
    _description = 'Todas las ordenes de servicio'

    def _get_image(self, cr, uid, ids, name, args, context=None):
        result = dict.fromkeys(ids, False)
        for obj in self.browse(cr, uid, ids, context=context):
            result[obj.id] = tools.image_get_resized_images(obj.image)
        return result
    
    def _set_image(self, cr, uid, id, name, value, args, context=None):
        return self.write(cr, uid, [id], {'image': tools.image_resize_image_big(value)}, context=context)
 
    _columns = {
		'id'          : fields.integer('ID',required=True),
		'name'        : fields.char('Visitante', size = 25, help = 'Nombre del servicio', required = True),		
        'visit'       : fields.many2one('hr.employee', 'Nombre a quien visita', size = 25, required = True),
        'reason'      : fields.char('Razon de la visita', size = 128, required = True),
        'date_out'    : fields.datetime("Hora de salida"),
        'date'        : fields.datetime("Hora de entrada"),
        'equipo'      : fields.char("Equipo o herramienta", size =25),
        #'photo'     : fields.binary('Photo'),
        'image'       : fields.binary("Photo", required = True,
            help="This field holds the image used as photo for the visits, limited to 1024x1024px."),
        'image_medium': fields.function(_get_image, fnct_inv=_set_image,
            string="photo", type="binary", multi="_get_image",
            store = {
                'mrp_service': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Medium-sized photo of the employee. It is automatically "\
                 "resized as a 64x64px image, with aspect ratio preserved. "\
                 "Use this field in form views or some kanban views."),
        'image_small'  : fields.function(_get_image, fnct_inv=_set_image,
            string="Small-sized photo", type="binary", multi="_get_image",
            store = {
                'mrp_service': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Small-sized photo of the employee. It is automatically "\
                 "resized as a 64x64px image, with aspect ratio preserved. "\
                 "Use this field anywhere a small image is required."),
       # 'photo_card': fields.binary('Photo card'),
       'image_card'       : fields.binary("Photo",
            help="This field holds the image_card used as photo for the visits, limited to 1024x1024px."),
        'image_medium': fields.function(_get_image, fnct_inv=_set_image,
            string="Medium-sized photo", type="binary", multi="_get_image",
            store = {
                'mrp_service': (lambda self, cr, uid, ids, c={}: ids, ['image_card'], 10),
            },
            help="Medium-sized photo of the employee. It is automatically "\
                 "resized as a 64x64px image_card, with aspect ratio preserved. "\
                 "Use this field in form views or some kanban views."),
        'image_small'  : fields.function(_get_image, fnct_inv=_set_image,
            string="Small-sized photo", type="binary", multi="_get_image",
            store = {
                'mrp_service': (lambda self, cr, uid, ids, c={}: ids, ['image_card'], 10),
            },
            help="Small-sized photo of the employee. It is automatically "\
                 "resized as a 64x64px image_card, with aspect ratio preserved. "\
                 "Use this field anywhere a small image_card is required."),
       # 'photo_car' : fields.binary('Photo car'),
        'image'       : fields.binary("Photo",
            help="This field holds the image used as photo for the visits, limited to 1024x1024px."),
        'image_medium': fields.function(_get_image, fnct_inv=_set_image,
            string="Medium-sized photo", type="binary", multi="_get_image",
            store = {
                'mrp_service': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Medium-sized photo of the employee. It is automatically "\
                 "resized as a 64x64px image, with aspect ratio preserved. "\
                 "Use this field in form views or some kanban views."),
        'image_small'  : fields.function(_get_image, fnct_inv=_set_image,
            string="Small-sized photo", type="binary", multi="_get_image",
            store = {
                'mrp_service': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Small-sized photo of the employee. It is automatically "\
                 "resized as a 64x64px image, with aspect ratio preserved. "\
                 "Use this field anywhere a small image is required."),
       # 'photo_card': fields.binary('Photo card'),
       'image_car'       : fields.binary("Photo",
            help="This field holds the image_car used as photo for the visits, limited to 1024x1024px."),
        'image_medium': fields.function(_get_image, fnct_inv=_set_image,
            string="Medium-sized photo", type="binary", multi="_get_image",
            store = {
                'mrp_service': (lambda self, cr, uid, ids, c={}: ids, ['image_card'], 10),
            },
            help="Medium-sized photo of the employee. It is automatically "\
                 "resized as a 64x64px image_card, with aspect ratio preserved. "\
                 "Use this field in form views or some kanban views."),
        'image_small'  : fields.function(_get_image, fnct_inv=_set_image,
            string="Small-sized photo", type="binary", multi="_get_image",
            store = {
                'mrp_service': (lambda self, cr, uid, ids, c={}: ids, ['image_car'], 10),
            },
            help="Small-sized photo of the employee. It is automatically "\
                 "resized as a 64x64px image_car, with aspect ratio preserved. "\
                 "Use this field anywhere a small image_car is required.")  

        
    }
mrp_service_all()