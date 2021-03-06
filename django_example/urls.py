"""django_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from graphene.contrib.django.views import GraphQLView
from . import schema

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^estore/', include('estore.urls')),
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(schema=schema.schema))),
    url(r'^graphiql', include('django_graphiql.urls')),
]
