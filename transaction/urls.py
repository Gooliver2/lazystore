from django.conf.urls import url

from transaction.views import TransactionListView, TransactionDetailView

urlpatterns = [
    url(
        regex=r"^$",
        view=TransactionListView.as_view(),
        name="transaction_list"
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=TransactionDetailView.as_view(),
        name="transaction_detail"
    ),
]
