from django.urls import include, path
from rest_framework import routers

from .views import UserProfileViewSet, UserViewSet, SpaceViewSet,ReservationViewSet, PaymentView

router = routers.DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'users', UserViewSet)
router.register(r'spaces', SpaceViewSet)
router.register(r'reservations', ReservationViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('process-payment/', PaymentView.as_view(), name='process-payment'),


]

urlpatterns += router.urls