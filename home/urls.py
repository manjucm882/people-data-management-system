from django.urls import path
from .views import (
    PeopleListView,
    PeopleDetailView,
    create_person,
    update_person,
    delete_person,
)

urlpatterns = [
    path('', PeopleListView.as_view(), name='people_list'),
    path('person/<int:pk>/', PeopleDetailView.as_view(), name='people_detail'),
    path('person/create/', create_person, name='create_person'),
    path('person/<int:pk>/update/', update_person, name='update_person'),
    path('person/<int:pk>/delete/', delete_person, name='delete_person'),
]
