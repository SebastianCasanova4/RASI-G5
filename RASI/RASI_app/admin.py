from django.contrib import admin
from .models import Paciente, Usuarios
# Register your models here.
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'cedula', 'edad', 'telefono', 'direccion', 'correo', 'grupo_sanguineo', 'nombre_eps', 'fecha_nacimiento', 'dependecia']
    search_fields = ['cedula']
    list_filter = ['nombre_eps', 'dependecia']
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'cedula', 'edad', 'telefono', 'direccion', 'correo', 'grupo_sanguineo', 'nombre_eps', 'fecha_nacimiento', 'imagen_diagnostico', 'frecuencia_cardiaca', 'presion', 'temperatura', 'oxigeno', 'frecuencia_respiratoria']
    search_fields = ['cedula']
    list_filter = ['nombre_eps', 'grupo_sanguineo']
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Usuarios, UsuariosAdmin)