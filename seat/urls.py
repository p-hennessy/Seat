from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import redirect

# obliterates user session
def logout(request):
	for key in request.session.keys():
		del request.session[key]
	print "Loging user out"
	request.session.flush() # force this through the db
	return redirect('/login/')

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('login.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^$', lambda request: redirect('/login/')),
    url(r'^logout/$', logout)
)