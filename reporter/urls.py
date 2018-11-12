from django.urls import include, path
from reporter.views import HomePageView, county_datasets, point_datasets

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('county_data/', county_datasets, name = 'county'),
	path('incidence_data/', point_datasets, name = 'incidences'),
    
]