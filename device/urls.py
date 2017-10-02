from django.conf.urls import url

from device.views import DeviceListView, DeviceDetailView

urlpatterns = [
    url(
        regex=r"^$",
        view=DeviceListView.as_view(),
        name="device_list"
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=DeviceDetailView.as_view(),
        name="device_detail"
    ),
]
