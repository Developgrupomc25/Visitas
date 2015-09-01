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
   
#    def cambio_facturacion(self, cr, uid, id, facproducto):
 #       """ On change of product it sets product quantity, tax account, name,
  #       uom of product, unit price and price subtotal.
    #     @parametro facproducto: es el nombre del prodyucto que recibe.
     #   """ 
      #  result={'facproducto': 1}
       # return (result)
   
	_columns = {
			'id': fields.integer('ID',required=True),
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
			'facinternas_notas': fields.text('Notas internas'),
            'facpresupuesto_notas': fields.text('Notas Presupuesto'),
			'state': fields.selection([('draft','Borrador'),('confirmed','Confirmado'),('cancel','Cancelado')], 'Estado', readonly = True),
			'factura_ids': fields.one2many('mrp_service.lines','factu_id','Facturacion de los servicios'),
	        'modelo_id': fields.many2one('fleet.vehicle','Modelo',required = True),
	        # 'pricelist_id': fields.many2one('product.pricelist', 'Pricelist', help='Pricelist of the selected partner.'),
	        'produccion_ids': fields.one2many('mrp_service.produccion','produccion_id','Orden de produccion'),
	        'produccion_fecha': fields.date('Fecha de la orden', required = True),
			'produccion_zona': fields.char('Zona', size = 60),
			'produccion_divicion':fields.char('Divicion', size = 60),
			'produccion_area': fields.char('Area', size = 60),
			'produccion_atencion':fields.char('Atencion', size = 60),
			'produccion_cliente': fields.char('Cliente', size = 60, help = 'Cliente al que se le hace el servicio'),
			'produccion_fecha_inicial':  fields.date('Fecha inicial', required = True),
			'produccion_fecha_final':  fields.date('Fecha final', required = True),
			'produccion_notas': fields.text('Notas'),
			'produccion_re_ter_unidad': fields.char('Reporta Terminio de la Unidad', required=True, size = 80),	
	  		'calidad_fecha_inicial':  fields.date('Fecha inicial', required = True),
			'calidad_fecha_final':  fields.date('Fecha final', required = True),
			'calidad_notas': fields.text('Notas'),
			'calidad_re_li_unidad': fields.char('Reporta Terminio de la Unidad', required=True, size = 80),	
			'calidad_fecha_liberacion':  fields.date('Fecha de Liberacion', required = True),
	  		'calidad_pri_inpeccion': fields.boolean('Primera Inspeccion'),
	  		'calidad_liberada': fields.boolean('Liberada')
	  		
	           }
	_defaults = {
				#'fecha' : lambda *a: time.strftime('%Y-%m-%d')
				'state'  : 'draft', 

				}

mrp_service_all()
class ppcambio(object):
	def cambio(self, cr, uid, ids,facproducto):
		resultado = {}
		print facproducto           
		##if not faccantidad:
			##faccantidad = 1
		##resultado['faccantidad'] = faccantidad
		##resultado['facpreciounitario']=17
		##resultado['facsubtotal']= 66
		return {'value': resultado}
	

class mrp_service_lines(osv.osv,ppcambio):
	_name = 'mrp_service.lines'
	_description = 'facturas'


#	def cambio(self, cr, uid, ids,facproducto,faccantidad,facpreciounitario,context=None):
#		vals={}
#		empresa=self.pool.get('product.product').browse(cr,uid,ids,context)
#		print(empresa.address_ids[facproducto].country_id.name)
#		return{'value':vals}
	
	_columns = {
			'factu_id': fields.many2one('mrp_service.all','ID Referencia'),
			'facproducto': fields.many2one('product.product','Producto'),	
            'faccantidad': fields.float('Cantidad',help = 'Cantidad',required=True),		
            'facpreciounitario': fields.float('Precio unitario', help = 'Precio unitario',	required=True),	
            'facimpuestos': fields.many2many('account.tax', 'repair_operation_line_tax', 'repair_operation_line_id', 'tax_id', 'Impuesto'),
            'facafacturar':fields.boolean('A facturar'),
            'facsubtotal':fields.float('Subtotal')
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