from django.urls import path
from modules.vps.views import VPSCreateAPIView, VPSDetailAPIView, VPSListAPIView, VPSStatusUpdateAPIView

urlpatterns = [
    path('vps/', VPSCreateAPIView.as_view(), name='vps-create'),
    path('vps/list/', VPSListAPIView.as_view(), name='vps-list'),  # Перенёс вверх
    path('vps/<str:uid>/status/', VPSStatusUpdateAPIView.as_view(), name='vps-status-update'),
    path('vps/<str:uid>/', VPSDetailAPIView.as_view(), name='vps-detail'),
]

