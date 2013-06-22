from django.conf.urls import patterns, include, url
<<<<<<< HEAD
from views import LandingView, LoginView, CanvasView
=======
from views import LandingView, LoginView, DashboardView
>>>>>>> 9f564308a49f2f3bc77c6620d6672fcc218e1c72

urlpatterns = patterns('',
    url('^$', LandingView.as_view(), name='landing_view'),
    url('^login$', LoginView.as_view(), name='login_view'),
<<<<<<< HEAD
    url('^canvas$', CanvasView.as_view(), name='canvas_view'),
=======
    url('^dashboard$', DashboardView.as_view(), name='dashboard_view'),
>>>>>>> 9f564308a49f2f3bc77c6620d6672fcc218e1c72
)
