# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cuestionario(models.Model):
    _name = 'encuestas.cuestionario'

    name = fields.Char(string='Name', required=True)
    tipo=fields.Selection([('1','Para la empresa'),('2','Para los trabajadores'),('3','Para todos'),('4','Otro')])
    pregunta=fields.One2many('encuestas.pregunta','cuestionario')
    #pregunta=fields.Many2one('encuestas.pregunta')

class pregunta(models.Model):
    _name = 'encuestas.pregunta'

    cuestionario=fields.Many2one('encuestas.cuestionario')
    votos=fields.Selection([('1','1'),('2','Muy Malo'),('3','Malo'),('4','Normal'),('5','Buena'),('6','Muy buena')])
    #cuestionario=fields.One2many('encuestas.cuestionario','pregunta')
    text = fields.Text(string='texto de la pregunta', required=True)
    respuesta=fields.One2many('encuestas.respuesta','pregunta')
    #respuesta = fields.One2many('encuestas.respuesta','pregunta')

class respuesta(models.Model):
    _name = 'encuestas.respuesta'

    votos=fields.Selection([('1','1'),('2','Muy Malo'),('3','Malo'),('4','Normal'),('5','Buena'),('6','Muy buena')])
    #pregunta= fields.Many2one(comodel_name='encuestas.pregunta', string='pregunta')
    text = fields.Char(string='texto respuesta', required=True)
    pregunta=fields.Many2one('encuestas.pregunta')
