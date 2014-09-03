from django.conf.urls import patterns, url
from product.views import create
urlpatterns = patterns('',
                       url(r'^create/', create)
                        )
