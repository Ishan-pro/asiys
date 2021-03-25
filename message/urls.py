from django.urls import path
from django.views.generic import TemplateView
from .views import home_view, dashboard_view, bookclass_view, addcomment_view
urlpatterns =[
    path('', home_view, name="home"),
    path('dashboard/', dashboard_view),
    path('bookclass/', bookclass_view),
    path('comment/', addcomment_view),
    path('aboutus/', TemplateView.as_view(template_name='aboutus.html'))
]