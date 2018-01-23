from django.conf.urls import url
from . import views

urlpatterns = [
				url(r'^add-person/$', views.add_person, name='add-person'),
				url(r'^add-item/$', views.add_item, name='add-item'),
				url(r'^submit-transaction/$', views.submit_transaction, name='submit-transaction'),
				url(r'^make-trade/$', views.make_trade, name='make-trade'),
				]