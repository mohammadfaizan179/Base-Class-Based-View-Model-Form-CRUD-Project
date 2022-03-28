from django.urls import path
from django.views.generic.base import View
from enroll import views

urlpatterns = [
    path("", views.UserAddShowView.as_view(), name="home"),

    path("delete/<int:id>/", views.UserDeleteView.as_view(), name="delete"),

    path("update/<int:id>/", views.UserUpdateView.as_view(), name = "update"),
    # path("update/<int:id>/", views.update, name="update")    
]
