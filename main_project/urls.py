"""main_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from webhooks.views import pull
from test_app import urls as test_app_urls
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView
urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"pull/", pull, name='pull'),
    path("", include(test_app_urls), name=""),
    path(r"graphql/", FileUploadGraphQLView.as_view(graphiql=True)),

    # path(r"graphql/", csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True))),
    # path('pgraphql', PrivateGraphQLView.as_view(graphiql=True, schema=Schema)),
    path(r"socialmedia/", include("postApp.urls")),
    path("core/", include("core.urls")),


]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
