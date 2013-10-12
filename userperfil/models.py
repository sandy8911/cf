from django.db import models
from django.contrib.auth.models import User
from django.template import defaultfilters

class usuarioPerfil(models.Model):
	def url(self,filename):
		'''Crea la ruta del nuevo archivo'''
		ruta = "uploads/user/%s/%s"%(self.user.username,filename)
		return ruta

	user 		= models.OneToOneField(User)
	slug 		= models.SlugField(blank = True, null = True)
	avatar 		= models.ImageField(upload_to = url)
	direccion 	= models.CharField(verbose_name = 'Direccion', max_length = 50)
	telefono 	= models.CharField(max_length = 30)

	class Meta:
		verbose_name		= u'Perfil'
		verbose_name_plural = u'Perfiles'

	def get_absolute_url(self):
		'''Creamos la url amigable'''
		return '/perfil/'+self.slug+'.html'

	def save(self, *args, **kwargs):
		'''Guardo la url amigable'''
		self.slug = defaultfilters.slugify(self.user.username)
		super(usuarioPerfil, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.user.username