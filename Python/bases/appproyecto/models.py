# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Departamento(models.Model):
    id_departamento = models.FloatField(primary_key=True)
    nombre_departamento = models.CharField(max_length=25)
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region')

    class Meta:
        managed = False
        db_table = 'departamento'


class Eleccion(models.Model):
    id_eleccion = models.FloatField(primary_key=True)
    nombre_eleccion = models.CharField(max_length=25)
    anio = models.CharField(max_length=5)
    analfavetos = models.FloatField()
    alfavetos = models.FloatField()
    primaria = models.FloatField()
    medio = models.FloatField()
    universitario = models.FloatField()
    municipio_id_municipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='municipio_id_municipio')
    partido_id_partido = models.ForeignKey('Partido', models.DO_NOTHING, db_column='partido_id_partido')
    genero_id_genero = models.ForeignKey('Genero', models.DO_NOTHING, db_column='genero_id_genero')
    raza_id_raza = models.ForeignKey('Raza', models.DO_NOTHING, db_column='raza_id_raza')

    class Meta:
        managed = False
        db_table = 'eleccion'


class Genero(models.Model):
    id_genero = models.FloatField(primary_key=True)
    nombre_genero = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'genero'


class Municipio(models.Model):
    id_municipio = models.FloatField(primary_key=True)
    nombre_municipio = models.CharField(max_length=35)
    departamento_id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_id_departamento')

    class Meta:
        managed = False
        db_table = 'municipio'


class Pais(models.Model):
    id_pais = models.FloatField(primary_key=True)
    nombre_pais = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'pais'


class Partido(models.Model):
    id_partido = models.FloatField(primary_key=True)
    iniciales_partido = models.CharField(max_length=10)
    nombre_partido = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'partido'


class Raza(models.Model):
    id_raza = models.FloatField(primary_key=True)
    nombre_raza = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'raza'


class Region(models.Model):
    id_region = models.FloatField(primary_key=True)
    nombre_region = models.CharField(max_length=10)
    pais_id_pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='pais_id_pais')

    class Meta:
        managed = False
        db_table = 'region'


class Temporal(models.Model):
    nom_elec = models.CharField(max_length=25, blank=True, null=True)
    anio = models.CharField(max_length=5, blank=True, null=True)
    pais = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=10, blank=True, null=True)
    depto = models.CharField(max_length=25, blank=True, null=True)
    mun = models.CharField(max_length=35, blank=True, null=True)
    par = models.CharField(max_length=10, blank=True, null=True)
    nompar = models.CharField(max_length=30, blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    raza = models.CharField(max_length=12, blank=True, null=True)
    analfavetos = models.FloatField(blank=True, null=True)
    alfavetos = models.FloatField(blank=True, null=True)
    sexo2 = models.CharField(max_length=10, blank=True, null=True)
    raza2 = models.CharField(max_length=12, blank=True, null=True)
    primaria = models.FloatField(blank=True, null=True)
    medio = models.FloatField(blank=True, null=True)
    univesitarios = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temporal'
