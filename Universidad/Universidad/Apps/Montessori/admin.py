
from django.contrib import admin

from Universidad.Apps.Montessori.models import *

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Matricula)
admin.site.register(Carrera)
admin.ChoicesFieldListFilter
class MontessoriAdmin(admin.ModelAdmin):
    list_display = ('estado', '',)
    list_filter = ('genero', 'estado')