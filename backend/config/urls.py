
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/blog/', include('blog.urls')),
    path('api/v1/account/', include('accounts.urls')),
]
