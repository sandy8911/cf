from django.db import models
from django.contrib.auth.models import User

class categoria(models.Model):
	"""Control de categorias"""
	nombre 		= models.CharField(max_length = 50, verbose_name = 'Nombre')
	descripcion = models.TextField(verbose_name = 'Descripcion', blank = True, null = True)
	icono 		= models.ImageFile(upload_to = 'uploads/iconos/', blank = True, null = True)
	slug 		= models.slugField(max_length = 100, blank = True, null = True)
	class Meta:
		verbose_name 		= u'Categorias'
		verbose_name_plural = u'Categorias' 

	def get_absolute_url(self):
		'''Creamos la url amigable'''
		return '/categoria/'+self.slug+'.html'

	def save(self, *args, **kwargs):
		'''Guardo la url amigable'''
		self.slug = defaultfilters.slugify(self.nombre)
		super(categoria, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre

class subCategoria(models.Model):
	"""Control de sub Categorias"""
	categoria 	= ForeignKey(categoria)
	nombre 		= models.CharField(max_length = 50, verbose_name = 'Nombre')
	descripcion = models.TextField(verbose_name = 'Descripcion', blank = True, null = True)
	icono 		= models.ImageFile(upload_to = 'uploads/iconos/', black = True, null = True)
	slug 		= models.slugField(max_length = 100, default = '', blank = True, null = True)
	class Meta:
		verbose_name 		= u'Sub-categoria'
		verbose_name_plural = u'Sub-categoria'

	def get_absolute_url(self):
		'''Creamos la url amigable'''
		return '/subcat/'+self.slug+'.html'

	def save(self, *args, **kwargs):
		'''Guardo la url amigable'''
		self.slug = defaultfilters.slugify(self.nombre)
		super(subCategoria, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre

class estadoPais(models.Model):
	"""Control de estados del Pais"""
	nombre = models.CharField(max_length = 50, verbose_name = 'Nombre')
	slug   = models.slugField(max_length = 100, default = '', blank = True, null = True)
	class Meta:
		verbose_name 		= u'Estado del Pais'
		verbose_name_plural = u'Estados del Pais'
	def get_absolute_url(self):
		'''Creamos la url amigable'''
		return '/edo/'+self.slug+'.html'

	def save(self, *args, **kwargs):
		'''Guardo la url amigable'''
		self.slug = defaultfilters.slugify(self.nombre)
		super(estadoPais, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre	

class zonaCiudad(models.Model):
	"""Control de zonas, las ciudades que pertencen a la zona"""
	nombre 		= models.CharField(max_length = 50, verbose_name = 'Nombre de la zona')
	slug 		= models.slugField(max_length = 100, blank = True, null = True)
	descripcion = models.TextField(verbose_name = 'Descripcion')
	icono 		= models.ImageFile(upload_to = 'uploads/iconos/', blank = True, null = True)
	class Meta:
		verbose_name 		= u'Zona'
		verbose_name_plural = u'Zonas'

	def get_absolute_url(self):
		'''Creamos la url amigable'''
		return '/zona/'+self.slug+'.html'

	def save(self, *args, **kwargs):
		'''Guardo la url amigable'''
		self.slug = defaultfilters.slugify(self.nombre)
		super(zonaCiudad, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre
		
		
class ciudad(models.Model):
	"""Control de ciudades"""
	estadoPais 		= models.ForeignKey(estadosPais, verbose_name = 'Estado')
	zona 			= models.ForeignKey(zonaCiudad, verbose_name = 'Zona')
	nombre 		 	= models.CharField(max_length = 50, verbose_name = 'Nombre')
	imgDescritiva 	= models.ImageFile(upload_to = 'uploads/img/', blank = True, null = True, verbose_name = 'Emblema')
	slug   			= models.slugField(max_length = 100, default = '', blank = True, null = True)
	class Meta:
		verbose_name 		= u'Ciudad'
		verbose_name_plural = u'Ciudades'

	def get_absolute_url(self):
		'''Creamos la url amigable'''
		return '/ciudad/'+self.slug+'.html'

	def save(self, *args, **kwargs):
		'''Guardo la url amigable'''
		self.slug = defaultfilters.slugify(self.nombre)
		super(ciudad, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre

class negocio(models.Model):
	"""Control del negocio"""
	usuario 		= models.ForeignKey(User)
	subCategoria 	= models.ForeignKey(subCategoria, verbose_name = 'Categoria')
	nombreEmpresa 	= models.CharField(max_length = 100, verbose_name = 'Nombre del la empresa')
	slug 			= models.slugField(max_length = 200, default = '', blank = True, null = True)
	descripcion 	= models.TextField(verbose_name = 'Descripcion de la empresa')
	direccion 	  	= models.CharField(max_length = 100, verbose_name = 'Direccion')
	colonia			= models.CharField(max_length = 100, verbose_name = 'Colonia')
	ciudad 			= models.ForeignKey(ciudad, verbose_name = 'Ciudad')
	telefonos 		= models.TextField()
	horario			= models.TextField(verbose_name = 'Horarios de atencion')
	logotipo 		= models.ImageFile(upload_to = 'uploads/logotipos/', verbose_name = 'Logotipo')
	imgDescritiva	= models.ImageFile(upload_to = 'uploads/img/', verbose_name = 'Imagen descritiva')
	paginaWeb		= models.UrlField(max_length = 200, verbose_name = 'Pagina web', blank = True, null = True)
	tags			= models.CharField(max_length = 300, verbose_name = 'Etiquetas')
	mapa			= models.TextField(verbose_name = 'Mapa de ubicacion')
	fechRegistro 	= models.DateTimeField(auto_now = True)
	fechVence 		= models.DateTimeField(verbose_name = 'Fecha de venciemto', auto_now = False)
	prioridadZona	= models.IntegerField(verbose_name = 'Prioridad por zona', default = 200)
	prioridadCate	= models.IntegerField(verbose_name = 'Prioridad por categoria', default = 200)
	activo 			= models.BooleanField(verbose_name = 'Activo')
	votos			= models.IntegerField(blank = True, default = 0)
	class Meta:
		verbose_name 		= u'Negocio'
		verbose_name_plural = u'Negocios'

	def get_absolute_url(self):
		'''Creamos la url amigable'''
		return '/negocio/'+self.slug+'.html'

	def save(self, *args, **kwargs):
		'''Guardo la url amigable'''
		self.slug = defaultfilters.slugify(self.nombreEmpresa)
		super(negocio, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombreEmpresa