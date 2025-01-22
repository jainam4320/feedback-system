from django.conf.urls import url
from ReviewBeforeYouBuy import views

urlpatterns = [

	url(r'^index/$', views.HomePageView.as_view()),
    
]