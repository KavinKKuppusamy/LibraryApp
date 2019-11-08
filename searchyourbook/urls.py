from django.conf.urls import url
from searchyourbook import views

app_name = "searchyourbook"
urlpatterns = [
    url(r'^$',views.index, name="index"),
]
