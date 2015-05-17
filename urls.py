from django.conf.urls import patterns, include, url
from workTome.views import * 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'workTome.views.home', name='home'),
    # url(r'^workTome/', include('workTome.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    #('^main/$',main),
    ('^login/$',login),
    #('^search/$',search),
    ('^log_in/$',log_in),
    ('^index/$',index),
    ('^send_messenge/$',send_messenge),
    ('^profile/$',profile),
    ('^upload/$',upload),
    ('^signup/$',signup),
    ('^join/$',join),
    ('^like/$',like),
    ('^follow/$',follow),
    ('^search/$',search),
    #('^send_comment/$',send_comment),
)
