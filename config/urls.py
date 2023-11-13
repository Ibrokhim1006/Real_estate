from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView


urlpatterns = [
    path("project/real-estet/api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "project/real-estet/api/token/", jwt_views.TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),
    path(
        "project/real-estet/api/token/refresh/", jwt_views.TokenRefreshView.as_view(),
        name="token_refresh"
    ),
    path("project/real-estet/api/admin/", admin.site.urls),
    path(
        "project/real-estet/api/docs/",
        TemplateView.as_view(
            template_name="doc.html",
            extra_context={"schema_url": "api_schema"}
        ),
        name="swagger-ui",
    ),
    path(
        "project/real-estet/api/password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
    path('project/real-estet/api/admin/', admin.site.urls),
    path('project/real-estet/api/authentication/api/', include('authentications.urls')),
    path('project/real-estet/api/real_estate/api/', include('real_estate.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),
]
