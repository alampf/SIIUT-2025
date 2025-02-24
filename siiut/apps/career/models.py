from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Quarter(models.Model):
  quarter = models.IntegerField(verbose_name = 'Cuatrimestre No')
  quarter_name = models.CharField(verbose_name = 'Cuatrimestre', max_length = 20)
  
  def __str__(self):
    return self.quarter_name
  
  class Meta:
    verbose_name = 'Cuatrimestre'
    
class Level(models.Model):
  name = models.CharField(max_length = 50, verbose_name = 'Nivel')
  short_name = models.CharField(max_length = 10, verbose_name = 'Abreviatura')
  
  def __str__(self):
    return self.short_name
  
  class Meta: 
    verbose_name = 'Nivele'
    
class Career(models.Model):
  name = models.CharField(max_length = 100, verbose_name = 'Nombre')
  short_name = models.CharField(max_length = 10, verbose_name = 'Abreviatura')
  level = models.ForeignKey(Level, on_delete = models.CASCADE, null = True, blank = True, verbose_name = 'Nivel', related_name = 'careers')
  is_active = models.BooleanField(verbose_name = 'Activa?', default = True)
  principal = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Director de Carrera', related_name = 'careers')
  year = models.CharField(max_length = 4, verbose_name = 'Año')
  
  def __str__(self):
    return f"{self.level} - {self.name}"
  
  class Meta:
    verbose_name = 'Carrera'

class Subject(models.Model):
  career = models.ForeignKey(Career, verbose_name = 'Carrera', on_delete = models.CASCADE, related_name = 'subjects')
  quarter = models.ForeignKey(Quarter, verbose_name = 'Cuatrimestre', on_delete = models.CASCADE , related_name = 'subjects')
  name = models.CharField(max_length = 100, verbose_name = 'Materia')
  total_hours = models.IntegerField(verbose_name = 'Horas totales')
  weekly_hours = models.IntegerField(verbose_name = 'Horas por Semana')
  
  def __str__(self):
    return f"{self.career.short_name} - {self.quarter} -  {self.name}"
  
  class Meta:
    verbose_name = 'Materia'