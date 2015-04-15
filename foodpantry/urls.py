from django.conf.urls import patterns, url

from foodpantry import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'signin/$', views.signin, name='signin'),
    url(r'inventory/$', views.inventory, name='inventory'),
    url(r'editsettings/$', views.editsettings, name='editsettings'),
    url(r'drives/$', views.drives, name='drives'),
    url(r'timetologout/$', views.timetologout, name='timetologout'),
    url(r'adddrive/$', views.adddrive, name='adddrive'),
    url(r'deletedrive/$', views.deletedrive, name='deletedrive'),
    url(r'changesettings/$', views.changesettings, name='changesettings'),
    url(r'addtweettemplate/$', views.addtweettemplate, name='addtweettemplate'),
    url(r'quicktweet/$', views.quicktweet, name='quicktweet'),

    #url(r'^list/$', views.list, name='list'),
    #url(r'^process/$', views.process, name='process'),
)