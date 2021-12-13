from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

schema_view = get_schema_view(
    openapi.Info(

        title="Authentication API",
        default_version='v1',
        description='SomeDescription'
    ),
    public=True
)

urlpatterns = [
    path('swagger/', schema_view.with_ui()),
    path('admin/', admin.site.urls),
    path('account/', include('application.acc.urls')),
    path('comment/', include('application.comment.urls')),
    path('post/', include('application.posts.urls')),
    path('chat/', include('application.chat.urls')),

    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

