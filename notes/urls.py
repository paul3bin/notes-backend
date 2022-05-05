from django.urls import path

from .views import NotesViewSet

app_name = "notes"

urlpatterns = [
    path(
        "get",
        NotesViewSet.as_view(
            {
                "get": "list",
            }
        ),
        name="get",
    ),
    path(
        "create",
        NotesViewSet.as_view(
            {
                "post": "create",
            }
        ),
        name="create",
    ),
    path(
        "get/<str:pk>",
        NotesViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="retrieve",
    ),
    path(
        "update/<str:pk>",
        NotesViewSet.as_view(
            {
                "put": "update",
            }
        ),
        name="update",
    ),
    path(
        "delete/<str:pk>",
        NotesViewSet.as_view(
            {
                "delete": "destroy",
            }
        ),
        name="delete",
    ),
]
