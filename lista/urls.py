from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from core.views import ListaViewSet, ProdutoViewSet, MercadoViewSet, UserViewSet

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


router = DefaultRouter()
router.register(r"listas", ListaViewSet)
router.register(r"produtos", ProdutoViewSet)
router.register(r"mercados", MercadoViewSet)
router.register(r"usuarios", UserViewSet)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    #    path("auth/", include("dj_rest_auth.urls")),
    #     path("auth/registration/", include("dj_rest_auth.registration.urls")),    ...
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
