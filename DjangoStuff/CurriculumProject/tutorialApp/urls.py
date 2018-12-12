from django.urls import path

from . import views

app_name = 'tutorialApp'

urlpatterns = [
    # default url
    path('', views.index, name='index'),

    # /tutorialApp/<int::company_id>/ number is the ID of the company
    path('<int:company_id>/',views.detail,name='detail'),
]
