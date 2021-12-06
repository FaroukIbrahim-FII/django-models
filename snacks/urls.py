from django.urls import path
from .views import (
                    SnackListView,
                    SnacDetailView,
                    )


urlpatterns = [
    path("", SnackListView.as_view(), name='snack_list'),
    path("<int:pk>", SnacDetailView.as_view(), name='snack_detail'),

]