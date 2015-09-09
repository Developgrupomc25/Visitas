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
		'id': fields.integer('ID',required=True),
		'name' : fields.char('nombre del servicio', size = 25, help = 'Nombre del servicio', required = True),		
		'empresa' : fields.many2one('res.partner','Empresa empresa', required= True),	
		'movimiento' : fields.char('Movimiento', size = 25, help = 'Movimiento'),		
		'centrodeservicio' : fields.char('Centro de Servicio', size = 25, help = 'Centro de Servicio'),	
		'datoscentrodeservicio' : fields.char('Datos Centro de Servicio', size = 25, help = 'Datos Centro de Servicio'),		
		'clienteJefe': fields.char('Jefe de Area', size = 30, help = 'Jefe de Area'),		
        'clienteNombre': fields.char('Nombre', size = 30, help = 'Nombre Jefe de Area'),	
        'clienteCorreo': fields.char('Correo Electronico', size = 30, help = 'Correo Electronico'),		
        'clienteClave': fields.char('Clave', size = 30, help = 'Clave'),
        'clienteEntregaCargo': fields.char('Cargo', size = 30, help = 'Cargo del cliente'),	
        'clienteEntregaNombre': fields.char('Nombre', size = 30, help = 'Nombre'),	
        'clienteEntregaCorreo': fields.char('Correo Electronico', size = 30, help = 'Correo Electronico'),		
        'clienteEntregaClave': fields.char('Clave', size = 30, help = 'Clave'),	
        'empresaEntregaCargo': fields.char('Cargo', size = 30, help = 'Cargo del cliente'),	
        'empresaEntregaNombre': fields.many2one('hr.employee','Nombre'),	
        'empresaEntregaCorreo': fields.char('Correo Electronico', size = 30, help = 'Correo Electronico'),		
        'empresaJefe': fields.char('Jefe de Area', size = 30, help = 'Jefe de Area'),		
        'empresaNombre': fields.many2one('hr.employee','Nombre Jefe de Area'),		
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
		'facinternas_notas': fields.text('Notas internas'),
        'facpresupuesto_notas': fields.text('Notas Presupuesto'),
		'factura_ids': fields.one2many('mrp_service.lines','factu_id','Facturacion de los servicios'),
	    'modelo_id': fields.many2one('fleet.vehicle','Modelo',required = True),
	    # 'pricelist_id': fields.many2one('product.pricelist', 'Pricelist', help='Pricelist of the selected partner.'),
	    'produccion_ids': fields.one2many('mrp_service.produccion','produccion_id','Orden de produccion'),
	    'produccion_fecha': fields.date('Fecha de la orden', required = True),
		'produccion_zona': fields.char('Zona', size = 60),
		'produccion_divicion':fields.char('Divicion', size = 60),
		'produccion_area': fields.char('Area', size = 60),
		'produccion_atencion':fields.char('Atencion', size = 60),
		'produccion_cliente': fields.many2one('res.partner','Cliente',required= True, help = 'Cliente al que se le hace el servicio'),
		'produccion_fecha_inicial':  fields.date('Fecha inicial', required = True),
		'produccion_fecha_final':  fields.date('Fecha final', required = True),
		'produccion_notas': fields.text('Notas'),
		'produccion_re_ter_unidad': fields.many2one('hr.employee','Reporta Terminio de la Unidad', required=True),	
	  	'calidad_fecha_inicial':  fields.date('Fecha inicial', required = True),
		'calidad_fecha_final':  fields.date('Fecha final', required = True),
		'calidad_notas': fields.text('Notas'),
		'calidad_re_li_unidad': fields.many2one('hr.employee','Reporta Terminio de la Unidad', required=True),	
		'calidad_fecha_liberacion':  fields.date('Fecha de Liberacion', required = True),
	  	'calidad_pri_inpeccion': fields.boolean('Primera Inspeccion'),
		'state': fields.selection([('one','Borrador'),('two','Inspeccion'),('three','Facturacion'),('four','Autorizada'),('five','Orden de trabajo'),('six','Orden de calidad'),('final','Cancelado')], 'Estado', readonly = True),
	  	'calidad_liberada': fields.boolean('Liberada'),
        'pricelist_id': fields.many2one('product.pricelist', 'Pricelist', help='Pricelist of the selected partner.'),
	        
        
	  	
	  	 }
	_defaults = {
		#'fecha' : lambda *a: time.strftime('%Y-%m-%d')
		'state'  : 'one',
   		'pricelist_id': lambda self, cr, uid,context : self.pool.get('product.pricelist').search(cr, uid, [('type','=','sale')])[0]
		}
	def one(self, cr, uid, ids,context=None):
		self.write(cr, uid, ids, {'state':'one'},context=None)
		return True
	def two(self, cr, uid, ids,context=None):
		self.write(cr, uid, ids, {'state':'two'},context=None)
		return True
	def three(self, cr, uid, ids,context=None):
		self.write(cr, uid, ids, {'state':'three'},context=None)
		return True
	def four(self, cr, uid, ids,context=None):
		self.write(cr, uid, ids, {'state':'four'},context=None)
		return True
	def five(self, cr, uid, ids,context=None):
		self.write(cr, uid, ids, {'state':'five'},context=None)
		return True
	def six(self, cr, uid, ids,context=None):
		self.write(cr, uid, ids, {'state':'six'},context=None)
		return True
	def final(self, cr, uid, ids,context=None):
		self.write(cr, uid, ids, {'state':'final'},context=None)
		return True
mrp_service_all()



class ppcambio(object):
    def cambio(self, cr, uid, ids,pricelist,facproducto,faccantidad=0,total=0,partner_id=False,uom=False):
        resultado = {}
        print 'holallll'
        print facproducto
       	print faccantidad
        print pricelist
        print total
        print 'esto es todo lo que impŕimo'
        #print faccantidad
        if not total:
        	total = 0          
        if not faccantidad:
            faccantidad = 1
        resultado['faccantidad'] = faccantidad
        if facproducto:
           product_obj = self.pool.get('product.product').browse(cr, uid, facproducto)
           print product_obj
        price = self.pool.get('product.pricelist').price_get(cr, uid, [pricelist],
                           facproducto, faccantidad, partner_id, )[pricelist]
        resultado.update({'facpreciounitario': price, 'facsubtotal': price*faccantidad})
        
        resultado['total'] = resultado['facsubtotal'] + total
        print resultado['total']
        return {'value': resultado}
ppcambio()

class mrp_service_lines(osv.osv,ppcambio):
	_name = 'mrp_service.lines'
	_description = 'facturas'
	_columns = {
		'factu_id': fields.many2one('mrp_service.all','ID Referencia',select=True),
		'facproducto': fields.many2one('product.product','Producto'),	
        'faccantidad': fields.float('Cantidad',help = 'Cantidad',required=True),		
        'facpreciounitario': fields.float('Precio unitario', help = 'Precio unitario',	required=True),	
        'facimpuestos': fields.many2many('account.tax', 'repair_operation_line_tax', 'repair_operation_line_id', 'tax_id', 'Impuesto'),
        'facafacturar':fields.boolean('A facturar'),
        'facsubtotal':fields.float('Subtotal'),
        'total': fields.float('Total')        
        }
   
mrp_service_lines()

class mrp_service_produccion(osv.osv):
	_name = 'mrp_service.produccion'
	_description = 'Orden de produccion'
	_columns = {
		'produccion_id': fields.many2one('mrp_service.all','ID Referencia'),
		'produccion_catalogo': fields.many2one('product.product','Producto'),
        }
mrp_service_produccion()