# -*- coding: utf-8 -*-

from odoo import models, fields, api
import secrets
import re
import logging
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class empleado(models.Model):
    _name='empleados.empleado'
    #_inherit='res.partner'

    name=fields.Char(required=True)
    apellidos=fields.Char(required=True)
    fechanacimiento=fields.Datetime()
    lugarnacimiento=fields.Text()
    puesto=fields.Text()
    telefono=fields.Char()
    correo=fields.Char()
    direccion=fields.Text()
    dni=fields.Char()
    idioma=fields.Selection([('1','Español'),('2','Ingles'),('3','Italiano'),('4','Otro')])
    Estadocivil=fields.Selection([('1','Soltero(a)'),('2','Casado(a)'),('3','Viudo(a)'),('4','Divorciado(a)')])
    nivelcertificado=fields.Selection([('1','Licenciado'),('2','Graduado'),('3','Maestro'),('4','Doctor'),('5','Otro')])
    campoestudio=fields.Text()
    escuela=fields.Char()
    nacionalidad=fields.Char()
    genero=fields.Selection([('1','Masculino'),('2','Femenino'),('3','Otro')])
    nhijos=fields.Integer(default='0')
    imagen=fields.Image(max_width=200, max_height=200)
    departamento=fields.Selection([('1','Marketing'),('2','Barra'),('3','Cocina'),('4','Otro')])
    ingresos_anuales = fields.Integer()
    ingresos_mensuales = fields.Integer(compute='campo_calculado')


    def name_get(self):
        result = []
        for record in self:
            name = f'{record.name} {record.apellidos}'
            result.append((record.name, name))
        return result

    def campo_calculado(self):
        for record in self:
            record.ingresos_mensuales = record.ingresos_anuales / 12
    
    @api.constrains('dni')
    def _check_dni(self):
        regex = re.compile('[0-9]{8}[-][A-Z]{1}', re.IGNORECASE)
        for s in self:
            if regex.match(s.dni):
                _logger.info('El dni es correcto')
            else:
                raise ValidationError('El dni es incorrecto')

    _sql_constraints = [('dni_uniq','unique(dni)','el dni no se puede repetir')]

    @api.constrains('telefono')
    def _check_telefono(self):
        regex = re.compile('[0-9]{9}', re.IGNORECASE)
        for s in self:
            if regex.match(s.telefono):
                _logger.info('El telefono es correcto')
            else:
                raise ValidationError('El telefono es incorrecto')

    _sql_constraints = [('telefono_uniq','unique(telefono)','el telefono no se puede repetir')]
