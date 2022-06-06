from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic.base import TemplateView

schema_view = get_schema_view(
    openapi.Info(
        title = 'Blog-post API',
        description = 'If you wanna create blog-posts project you can use my API',
        default_version = 'v1',
        terms_of_services = 'https://www.google.com/polices/terms/',
        contact = openapi.Contact(email='sc.newcompany@gmail.com'),
        license = openapi.License(name='Standart License')
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
)

urlpatterns = [
    path('', TemplateView.as_view(template_name='main.html')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('api.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/allauth', include('allauth.urls')),
    path('swagger', schema_view.with_ui(
        'swagger', cache_timeout = 0
    ),
    name = 'schema-swagger-ui'),
    path('redoc', schema_view.with_ui(
        'redoc', cache_timeout = 0
    ), name='schema-redoc')
]
