from django.urls import path
from .views import weekly_lead, yearly_lead, quaterly_lead

urlpatterns = [
    path('weekly/', weekly_lead, name="weekly_lead"),
    path('yearly/', yearly_lead, name="yearly_lead"),
    path('quarter/', quaterly_lead, name="quaterly_lead"),
]

    