# -*- coding: utf-8 -*-

from odoo import models, fields, api

class entradas(models.Model):
    _name = 'gastos.entradas'

    name = fields.Char(string='Name', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    descripcion = fields.Char(string='Descripción', required=True)
    importe_anual= fields.Integer(string='Importe', required=True)
    categoria = fields.Selection([('alimentacion', 'Alimentación'),('transporte', 'Transporte'),('alojamiento', 'Alojamiento'),('otros', 'Otros')], string='Categoría', required=True)
    #responsable = fields.Many2one('res.partner', string='Responsable')
    importe_semanal=fields.Integer(compute='campo_calculado', store=True)

    def campo_calculado(self):
        for record in self:
            record.importe_anual = record.importe_anual/12/4


class salidas(models.Model):
    _name = 'gastos.salidas'

    name = fields.Char(string='Name', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    descripcion = fields.Char(string='Descripción', required=True)
    importe = fields.Integer(string='Importe', required=True)
    categoria = fields.Selection([('alimentacion', 'Alimentación'),('transporte', 'Transporte'),('alojamiento', 'Alojamiento'),('otros', 'Otros')], string='Categoría', required=True)
    #responsable = fields.Many2one('res.partner', string='Responsable')
