from django.conf.urls import url
from . import views
app_name = 'picture'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^single/(\d+)/$', views.SingleView.as_view(), name='single'),
    url(r'^portfolio/$', views.PortfolioView.as_view(), name='portfolio'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^personal/(\d+)/$', views.PersonalView.as_view(), name='personal'),
    # url(r'^checkcount/$', views.CheckCountView.as_view(), name='checkcount'),
    url(r'^personalsingle/(\d+)/(\d+)/$', views.PersonalSingleView.as_view(), name='personalsingle'),
]