from .models import categoria,subCategoria,estadoPais,zonaCiudad,ciudad,formaPago,etiquetas,negocio,comentarioNegocio
from django.contrib import admin

admin.site.register(categoria)
admin.site.register(subCategoria)
admin.site.register(estadoPais)
admin.site.register(zonaCiudad)
admin.site.register(ciudad)
admin.site.register(formaPago)
admin.site.register(etiquetas)
admin.site.register(negocio)
admin.site.register(comentarioNegocio)