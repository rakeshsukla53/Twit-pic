from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',   #urls pattern are designed here
    # Examples:
    url(r'^$', 'twitter.views.home', name='home'),  #url design kar sakte hain
    # url(r'^blog/', include('blog.urls')),  #when you click on browser it will come to URL patters and scan everything

    url(r'^admin/', include(admin.site.urls)),  #it is pointing to http://127.0.0.1:8000/admin/ url
)


#url(r'^$', 'twitter.views.home', name='home') it is looking for an folder in twitter -->views jo present nahi hain

