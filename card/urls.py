from django.conf.urls import url

from card.views import CardListView, CardDetailView
from device.views import DeviceListView, DeviceDetailView

urlpatterns = [
    url(
        regex=r"^$",
        view=CardListView.as_view(),
        name="card_list"
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=CardDetailView.as_view(),
        name="card_detail"
    ),
]
