# -*- coding: utf-8 -*-

from odoo import models, fields, api


class productos(models.Model):
    _name = 'inventario.productos'

    name=fields.Char()
    descripcion=fields.Text()
    tipo_producto=fields.Selection([('1','Almacenable'),('2','Consumible'),('3','Servicio'),('4','Otro')])
    precio_venta=fields.Float()
    id_interno=fields.Char()
    codigo_barras=fields.Char()
    peso=fields.Float()
    volumen=fields.Float()
    plazo=fields.Float()
    imagen=fields.Image()
