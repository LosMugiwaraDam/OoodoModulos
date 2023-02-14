# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ventas(models.Model):
    _name = 'tienda.ventas'
    _inherit='gastos.entradas'

    #name = fields.Char(string='Name', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    descripcion = fields.Char(string='Descripción', required=True)


class compras(models.Model):
    _name = 'tienda.compras'
    _inherit='gastos.salidas'

    #name = fields.Char(string='Name', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    descripcion = fields.Char(string='Descripción', required=True)

class productos(models.Model):
    _name = 'tienda.productos'
    _inherit = 'inventario.productos'

    #name=fields.Char()
    descripcion=fields.Text()
    tipo_producto=fields.Selection([('1','Almacenable'),('2','Consumible'),('3','Servicio'),('4','Otro')])
    precio_venta=fields.Float()
    id_interno=fields.Char()
    codigo_barras=fields.Char()
    peso=fields.Float()
    volumen=fields.Float()
    plazo=fields.Float()
    imagen=fields.Image()


class cliente(models.Model):
     _name = 'res.partner'
     _inherit='res.partner'
     #_description = 'pruebaherencias.pruebaherencias'

     #name = fields.Char()
     birth_year=fields.Integer()
     #dni=fields.Char()
