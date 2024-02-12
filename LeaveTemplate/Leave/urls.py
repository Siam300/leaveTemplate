from django.urls import path
from .views import LeaveRequestListCreateView, LeaveRequestDetailView

urlpatterns = [
    path('leave-requests/', LeaveRequestListCreateView.as_view(), name='leave-request-list-create'),
    path('leave-requests/<int:pk>/', LeaveRequestDetailView.as_view(), name='leave-request-detail'),
]

