from django.conf.urls import url
from basicfunc import views
from basicfunc.models import Participant
import re


# def check_in_list(lst, regx):
# 	for i in lst:


# Links to each user's custom page is in a list below
links = [Participant.objects.all()[x].link for x in range(Participant.objects.count())]

# urlpatterns for all

urlpatterns = [
	url(r'^$', views.HomeView.as_view(), name='index'),
	url(r'^show_users/$', views.disp_users, name='viewUser'),
	url(r'^show_users/%s' % links, views.single_user, name='dhaval'),
	url(r'^display/$', views.display_table, name='showcase'),
	url(r'^history/$', views.history_table,name='history')
]
