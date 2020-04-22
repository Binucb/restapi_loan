from django.urls import path,include
from rest_framework.routers import DefaultRouter
from loan_app import views

router = DefaultRouter()
router.register('approval',views.ApprovalViewSet)

urlpatterns = [
    path('',include(router.urls)),
    
]