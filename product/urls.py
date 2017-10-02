from django.conf.urls import url

from product.views import ProductListView, ProductDetailView, ProductTypeDetailView, ProductTypeListView

urlpatterns = [
    url(
        regex=r"^$",
        view=ProductListView.as_view(),
        name="product_list"
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=ProductDetailView.as_view(),
        name="product_detail"
    ),

    url(
        regex=r"^types/$",
        view=ProductTypeListView.as_view(),
        name="product_list"
    ),
    url(
        regex=r"^types/(?P<pk>\d+)/$",
        view=ProductTypeDetailView.as_view(),
        name="product_detail"
    ),
]
