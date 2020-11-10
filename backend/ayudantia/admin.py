from django.contrib import admin
from .models import Estudiantes, Profesores

# Register your models here.

class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','mail')

admin.site.register(Estudiantes,EstudiantesAdmin)

class ProfesoresAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','mail')

admin.site.register(Profesores,ProfesoresAdmin)