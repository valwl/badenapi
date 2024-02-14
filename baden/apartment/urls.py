from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'apartment', views.ApartmentView)
print(router.urls)

urlpatterns = [
    # path('list/', views.ApartmentView.as_view({'get': 'list'})),
    # path('create/', views.ApartmentView.as_view({'post': 'create'})),
    # path('img/', views.ApartmentView.as_view({'get': 'get_img'})),
    path('', include(router.urls)),
    path('location_list/', views.LocationView.as_view()),
]
