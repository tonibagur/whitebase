from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from chessdb import views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^games$', views.GameList.as_view()),
    url(r'^games/(?P<pk>[0-9]+)$', views.GameDetail.as_view()),
    url(r'^views/(?P<template_name>\w+)$', login_required(views.TemplateChessView.as_view(),login_url='/login/'), name='lchess_view'),
    url(r'^views/(?P<template_name>\w+)/(?P<pk>\d+)$', login_required(views.TemplateChessView.as_view(),login_url='/login/'), name='chess_view'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
