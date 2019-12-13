#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:47:11 2019

Clase que contiene los datos de todas las mascotas disponibles en la API Petfinder.

@author: Lidia Sánchez Mérida
"""
import ficha_mascota
from conexion_api_petfinder import ConexionAPIPetfinder

class Mascotas:
    
    def __init__(self):
        """Constructor. En él se genera una variable de instancia en la que 
            se almacena la conexión con la API Petfinder."""
        self.api_petfinder = ConexionAPIPetfinder.conectarConPetfinder()
    
    def variable_correcta(self, variable, tipo):
        """Comprueba el tipo y el valor de una variable."""
        return (variable != None and isinstance(variable, tipo) == True)
    
    def aniadir_nueva_mascota(self, nueva_mascota):
        """Analiza los datos recibidos de una mascota en particular para comprobar
            si existen datos no válidos. En tal caso se sustituirán por el valor 'DNV'.
            Posteriormente se creará un diccionario con solo los datos 
            interesantes para el proyecto y se devolverá como resultado."""
        datos_no_validos = 0
        check_nombre = self.variable_correcta(nueva_mascota.nombre, str)
        if not (check_nombre) :
            nueva_mascota.nombre = "DNV"
            datos_no_validos += 1
        check_tipo_animal = self.variable_correcta(nueva_mascota.tipo_animal, str)
        if not (check_tipo_animal) :
            nueva_mascota.tipo_animal = "DNV"
            datos_no_validos += 1
        check_raza = self.variable_correcta(nueva_mascota.raza, str)
        if not (check_raza) :
            nueva_mascota.raza = "DNV"
            datos_no_validos += 1
        check_tamanio = self.variable_correcta(nueva_mascota.tamanio, str)
        if not (check_tamanio) :
            nueva_mascota.tamanio = "DNV"
            datos_no_validos += 1
        check_genero = self.variable_correcta(nueva_mascota.genero, str)
        if not (check_genero) :
            nueva_mascota.genero = "DNV"
            datos_no_validos += 1
        check_edad = self.variable_correcta(nueva_mascota.edad, str)
        if not (check_edad) :
            nueva_mascota.edad = "DNV"
            datos_no_validos += 1
        check_tipo_pelaje = self.variable_correcta(nueva_mascota.tipo_pelaje, str)
        if not (check_tipo_pelaje) :
            nueva_mascota.tipo_pelaje = "DNV"
            datos_no_validos += 1
        check_estado = self.variable_correcta(nueva_mascota.estado, str)
        if not (check_estado) :
            nueva_mascota.estado = "DNV"
            datos_no_validos += 1
        check_bueno_con_ninios = self.variable_correcta(nueva_mascota.bueno_con_ninios, bool)
        if not (check_bueno_con_ninios) :
            nueva_mascota.bueno_con_ninios = "DNV"
            datos_no_validos += 1
        check_bueno_con_gatos = self.variable_correcta(nueva_mascota.bueno_con_gatos, bool)
        if not (check_bueno_con_gatos) :
            nueva_mascota.bueno_con_gatos = "DNV"
            datos_no_validos += 1
        check_bueno_con_perros = self.variable_correcta(nueva_mascota.bueno_con_perros, bool)
        if not (check_bueno_con_perros) :
            nueva_mascota.bueno_con_perros = "DNV"
            datos_no_validos += 1
        check_ciudad = self.variable_correcta(nueva_mascota.ciudad, str)
        if not (check_ciudad) :
            nueva_mascota.ciudad = "DNV"
            datos_no_validos += 1
        check_pais = self.variable_correcta(nueva_mascota.pais, str)
        if not (check_pais) :
            nueva_mascota.pais = "DNV"
            datos_no_validos += 1
        """Almacenamos los datos de la mascota más relevantes para devolverlos."""
        mascota = {
            'nombre':nueva_mascota.nombre,
            'tipo_animal':nueva_mascota.tipo_animal,
            'raza':nueva_mascota.raza,
            'tamanio':nueva_mascota.tamanio,
            'genero':nueva_mascota.genero,
            'edad':nueva_mascota.edad,
            'tipo_pelaje':nueva_mascota.tipo_pelaje,
            'estado':nueva_mascota.estado,
            'ninios':nueva_mascota.bueno_con_ninios,
            'perros':nueva_mascota.bueno_con_perros,
            'gatos':nueva_mascota.bueno_con_gatos,
            'ciudad':nueva_mascota.ciudad,
            'pais':nueva_mascota.pais
        }
        return mascota

    def descargar_datos_mascotas(self):
        """Método que descarga datos de hasta veinte mascotas. Posteriormente
            examina los valores que son relevantes para el proyecto y si contiene
            valores no válidos se sustituye por 'DNV'."""
        if (self.api_petfinder == None): raise ConnectionError("No hay conexión con la API Petfinder.")
        else:
            id_mascota_validada = 0
            mascotas_validadas = {}
            try:
                mascotas = (self.api_petfinder).animals()
            except:
                raise ConnectionError("Error al intentar descargar los datos de mascotas.")
                
            for mascota in mascotas['animals']:
                nueva_mascota = ficha_mascota.FichaMascota(mascota['name'], mascota['type'], 
                   mascota['breeds']['primary'], mascota['size'], mascota['gender'], mascota['age'],
                   mascota['coat'], mascota['status'], mascota['environment']['children'], 
                   mascota['environment']['cats'], mascota['environment']['dogs'], 
                   mascota['contact']['address']['city'], mascota['contact']['address']['country'])
                mascota_validada = self.aniadir_nueva_mascota(nueva_mascota)
                
                """Devolvemos las mascotas con los datos validados."""
                mascotas_validadas[id_mascota_validada] = mascota_validada
                id_mascota_validada += 1
                
            return mascotas_validadas
    
    def obtener_una_mascota(self, indice, mascotas):
        """Método encargado de devolver los datos de una mascota en particular,
            si el identificador es válido."""
        if indice == None or type(indice) != int or (indice in mascotas) == False:
            raise IndexError("No existe ninguna mascota con el identificador especificado.")

        return mascotas[indice]