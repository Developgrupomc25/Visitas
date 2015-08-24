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
			'name' : fields.char('nombre del servicio', size = 25, help = 'Nombre del servicio', required = True),		
			'empresa' : fields.char('Empresa', size = 25, help = 'Empresa'),	
			'movimiento' : fields.char('Movimiento', size = 25, help = 'Movimiento'),		
			'centrodeservicio' : fields.char('Centro de Servicio', size = 25, help = 'Centro de Servicio'),	
			'datoscentrodeservicio' : fields.char('Datos Centro de Servicio', size = 25, help = 'Datos Centro de Servicio'),		
			'clienteJefe': fields.char('Jefe de Area', size = 30, help = 'Jefe de Area'),		
            'clienteNombre': fields.char('Nombre Jefe de Area', size = 30, help = 'Nombre Jefe de Area'),	
            'clienteCorreo': fields.char('Correo Electronico', size = 30, help = 'Correo Electronico'),		
            'clienteClave': fields.char('Clave', size = 30, help = 'Clave'),
            'clienteEntregaCargo': fields.char('Cargo', size = 30, help = 'Cargo del cliente'),	
            'clienteEntregaNombre': fields.char('Nombre', size = 30, help = 'Nombre'),	
            'clienteEntregaCorreo': fields.char('Correo Electronico', size = 30, help = 'Correo Electronico'),		
            'clienteEntregaClave': fields.char('Clave', size = 30, help = 'Clave'),	
            'empresaEntregaCargo': fields.char('Cargo', size = 30, help = 'Cargo del cliente'),	
            'empresaEntregaNombre': fields.char('Nombre', size = 30, help = 'Nombre'),	
            'empresaEntregaCorreo': fields.char('Correo Electronico', size = 30, help = 'Correo Electronico'),		
            'empresaJefe': fields.char('Jefe de Area', size = 30, help = 'Jefe de Area'),		
            'empresaNombre': fields.char('Nombre Jefe de Area', size = 30, help = 'Nombre Jefe de Area'),		
            'empresaCorreo': fields.char('Correo Electronico', size = 30, help = 'Correo Electronico'),		
            'empresaClave': fields.char('Clave', size = 30, help = 'Clave'),		
			'fecha': fields.date('fecha de alta', required = True),
			'empresaEntregaFecha': fields.date('fecha de alta', required = False),
			'clienteTelefono': fields.integer('Tel Oficina', required = False),
			'folio': fields.char('Folio', required = True),
            'clienteMovil': fields.integer('Movil', required = 	False),
            'clienteEntregaTelefono': fields.integer('Tel Oficina', required = False),
            'clienteEntregaMovil': fields.integer('Movil', required = False),
            'empresaEntregaTelefono': fields.integer('Tel Oficina', required = False),
            'empresaEntregaMovil': fields.integer('Movil', required = False),
            'empresaTelefono': fields.integer('Tel Oficina', required = False),
            'empresaMovil': fields.integer('Movil', required = False),
            'empresaNoEmpleado': fields.integer('Numero de Empleado', required = True),
			'garantia': fields.boolean('Garantia'),
			'nuevoingreso': fields.boolean('Nuevo Ingreso'),
			'enviar': fields.boolean('Enviar'),
			'reparado': fields.boolean('Reparado'),
			'facturado': fields.boolean('Facturado'),
			'internal_notes': fields.text('Internal Notes'),
            'quotation_notes': fields.text('Quotation Notes'),
			'state': fields.selection([('draft','Borrador'),('confirmed','Confirmado'),('cancel','Cancelado')], 'Estado', readonly = True),
			'factura_ids': fields.one2many('mrp_service.lines','factu_id','Facturacion de los servicios'),
	        'modelo_id': fields.many2one('fleet.vehicle','Modelo',required = True),
	        # 'pricelist_id': fields.many2one('product.pricelist', 'Pricelist', help='Pricelist of the selected partner.'),
	           }
	_defaults = {
				#'fecha' : lambda *a: time.strftime('%Y-%m-%d')
				'state'  : 'draft', 
				}

mrp_service_all()

class mrp_service_lines(osv.osv):
	_name = 'mrp_service.lines'
	_description = 'facturas'
	_columns = {
			'factu_id': fields.many2one('mrp_service.all','ID Referencia'),
			'facproducto': fields.many2one('product.product','Producto'),	
            'faccantidad': fields.float('Cantidad',help = 'Cantidad',required=True),		
            'facpreciounitario': fields.float('Precio unitario', help = 'Precio unitario',	required=True),	
            'facimpuestos': fields.many2many('account.tax', 'repair_operation_line_tax', 'repair_operation_line_id', 'tax_id', 'Impuesto'),
            'facafacturar':fields.boolean('A facturar'),
            'facsubtotal':fields.float('Subtotal')
	   }
