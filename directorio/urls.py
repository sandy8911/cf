from django.conf.urls import patterns, url, include

urlpatterns = patterns('directorio.views',
	url(r'^$','inicio', name = 'inicio')
)