# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.float_utils import float_round
from odoo.tools.translate import _
from odoo.exceptions import UserError

class idea(models.Model):
    _name = 'sugerencias.idea'
    _description = 'clase idea para almacenar las ideas de los empleados'

    titulo = fields.Char(required=True)
    fecha_creacion = fields.Datetime(default=lambda self: fields.Datetime.now())
    fecha_final = fields.Date()
    descripcion = fields.Text()
    tipo_idea = fields.Selection([('1','Para mejorar la empresa'),('2','Para mejorar el compañerismo'),('3','Para mejorar las condiciones laborales'),('4','OTRO')])
    votos=fields.Selection([('1','1'),('2','Muy Malo'),('3','Malo'),('4','Normal'),('5','Buena'),('6','Muy buena')])
    
    empleado=fields.Many2one('empleados.empleado')
    inspiracion=fields.Text()

class empleado(models.Model):
    _name='sugerencias.empleado'
    _inherit='empleados.empleado'

    #name=fields.Char(required=True)
    apellidos=fields.Char(required=True)
    fechanacimiento=fields.Datetime()
    idea=fields.One2many('sugerencias.idea','empleado')
