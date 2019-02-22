from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
import profiles.urls
import accounts.urls
from . import views

# Personalised admin site settings like title and header
admin.site.site_title = "Project PM Site Admin"
admin.site.site_header = "Devise Solutions Administration"

urlpatterns = [
	path("", views.HomePage.as_view(), name="home"), # see views file for more on this
	path("about/", views.AboutPage.as_view(), name="about"), # and this
	path("admin/", admin.site.urls),
	path("users/", include(profiles.urls)),
	path("", include(accounts.urls)),
	# include url patterns to new apps here.
]
	
# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
	import debug_toolbar
	urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]