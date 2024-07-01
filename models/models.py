# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class box(models.Model):
#     _name = 'box.box'
#     _description = 'box.box'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api, exceptions

class BoxNormativa(models.Model):
    _name = 'box.normativa'
    _description = 'Normativa para Easy Box'

    name = fields.Char(string='Nombre de la Normativa', required=True)
    fecha_hora_mezcla = fields.Datetime(string='Fecha de la mezcla', default=fields.Datetime.now, readonly=True)
    temp_min = fields.Float(string='Temperatura Mínima', required=True)
    temp_max = fields.Float(string='Temperatura Máxima', required=True)
    humedad_min = fields.Float(string='Humedad Mínima', required=True)
    humedad_max = fields.Float(string='Humedad Máxima', required=True)
    tiempo_reaccion_min = fields.Float(string='Tiempo de Reacción Minimo', required=True)
    tiempo_reaccion_max = fields.Float(string='Tiempo de Reacción Máximo', required=True)
    proporcion_Base = fields.Float(string='Proporción de la Base', required=True)
    proporcion_Catalizador = fields.Float(string='Proporción del Catalizador', required=True)
    proporcion_Diluyente = fields.Float(string='Proporción del Diluyente', required=True)

#función para actualizar la fecha y hora en la que se modifica la normativa (cualquier registro)
    def write(self, values):
        if 'fecha_hora_mezcla' not in values:
            values['fecha_hora_mezcla'] = fields.Datetime.now()
        return super(BoxNormativa, self).write(values)



class BoxUsuario(models.Model):
    _name = 'box.usuario'
    _description = 'Usuario para Easy Box'

    name = fields.Char(string='Nombre', required=True)
    operario_number = fields.Char(string='Número de Operario', required=True)
    categoria_profesional = fields.Char(string='Categoría Profesional', required=True)
    fecha_hora_mezcla = fields.Datetime(string='Fecha de la mezcla', default=fields.Datetime.now)
    nivel_profesional = fields.Selection([('S', 'Nivel Superior'), ('M', 'Nivel Medio'), ('B', 'Nivel Básico')], string='Nivel de Operario', required=True)                                         
    temp = fields.Float(string='Temperatura', required=True)
    humedad = fields.Float(string='Humedad', required=True)
    tiempo_reaccion = fields.Float(string='Tiempo de Reacción', required=True)
    proporcion_base = fields.Float(string='Proporción de la Base', required=True)
    proporcion_catalizador = fields.Float(string='Proporción del Catalizador', required=True)
    proporcion_diluyente = fields.Float(string='Proporción del diluyente', required=True)

#relación muchos a uno para poder elegir de entre varias normativas creadas
    normativa_id = fields.Many2one('box.normativa', string='Normativa', required=True)

# Campos de referencia de la normativa. Mostrará las medidas estandar que el administrador haya introducido
    name_normativa = fields.Char(string='Nombre de la Normativa', related='normativa_id.name')
    temp_min_normativa = fields.Float(string='Temperatura Mínima', related='normativa_id.temp_min')
    temp_max_normativa = fields.Float(string='Temperatura Máxima', related='normativa_id.temp_max')
    humedad_min_normativa = fields.Float(string='Humedad Mínima', related='normativa_id.humedad_min')
    humedad_max_normativa = fields.Float(string='Humedad Máxima', related='normativa_id.humedad_max')
    tiempo_reaccion_min_normativa = fields.Float(string='Tiempo de Reacción Minimo', related='normativa_id.tiempo_reaccion_min')
    tiempo_reaccion_max_normativa = fields.Float(string='Tiempo de Reacción Máximo', related='normativa_id.tiempo_reaccion_max')
    proporcion_Base_normativa = fields.Float(string='Proporción de la Base', related='normativa_id.proporcion_Base')
    proporcion_Catalizador_normativa = fields.Float(string='Proporción del Catalizador', related='normativa_id.proporcion_Catalizador')
    proporcion_Diluyente_normativa = fields.Float(string='Proporción del Diluyente', related='normativa_id.proporcion_Diluyente')

#función para actualizar la fecha y hora en la que se INTRODUCEN MEDICIONES y/o al modificar cualquier registro
    def write(self, values):
        if 'fecha_hora_mezcla' not in values:
            values['fecha_hora_mezcla'] = fields.Datetime.now()
        return super(BoxUsuario, self).write(values)

#función para la detección de incompatibilidades
    @api.constrains('temp', 'humedad', 'tiempo_reaccion', 'proporcion_base', 'proporcion_catalizador', 'proporcion_diluyente')
    def _check_valores_normativa(self):
        for user in self:
            normativa = user.normativa_id  # Obtiene la normativa seleccionada por el operario
            if normativa:
                if user.temp < normativa.temp_min or user.temp > normativa.temp_max:
                    raise exceptions.ValidationError('La TEMPERARURA no cumple con la normativa\npor favor modifíquela para continuar')
                if user.humedad < normativa.humedad_min or user.humedad > normativa.humedad_max:
                    raise exceptions.ValidationError('La HUMEDAD no cumple con la normativa\npor favor modifíquela para continuar')
                if user.tiempo_reaccion < normativa.tiempo_reaccion_min or user.tiempo_reaccion > normativa.tiempo_reaccion_max:
                    raise exceptions.ValidationError('El TIEMPO DE REACCIÓN no cumple con la normativa\npor favor modifíquelo para continuar')
                if user.proporcion_base < normativa.proporcion_Base or user.proporcion_base > normativa.proporcion_Base:
                    raise exceptions.ValidationError('La proporción de la BASE no coincide con la normativa\npor favor modifíquela para continuar')
                if user.proporcion_catalizador < normativa.proporcion_Catalizador or user.proporcion_catalizador > normativa.proporcion_Catalizador:
                    raise exceptions.ValidationError('La proporción del CATALIZADOR no coincide con la normativa\npor favor modifíquela para continuar')
                if user.proporcion_diluyente < normativa.proporcion_Diluyente or user.proporcion_diluyente > normativa.proporcion_Diluyente:
                    raise exceptions.ValidationError('La proporción del DILUYENTE no coincide con la normativa\npor favor modifíquela para continuar')