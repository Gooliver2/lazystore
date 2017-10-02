from django.conf.urls import url

from bucket.views import BucketListView, BucketDetailView

urlpatterns = [
    url(
        regex=r"^$",
        view=BucketListView.as_view(),
        name="bucket_list"
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=BucketDetailView.as_view(),
        name="bucket_detail"
    ),
]
