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
	_columns = {
		'id'        : fields.integer('ID',required=True),
		'name'      : fields.char('nombre de quien visita', size = 25, help = 'Nombre del servicio', required = True),		
        'visit'     : fields.many2one('hr.employee', 'Nombre a quien visita', size = 25, required = True),
        'reason'    : fields.char('Razon de la visita', size = 128, required = True),
        'date'      : fields.datetime("Fecha"),
        'photo'     : fields.binary('Photo'),
        'photo_card': fields.binary('Photo card'),
        'photo_car' : fields.binary('Photo car'),    

    }
mrp_service_all()
