from django.contrib import admin
from django.conf.urls import url
from my_app.views import subscribe, home_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^subscribe/', subscribe, name = "subscribe"),
    url(r'^$', home_page, name = "home_page"),
]