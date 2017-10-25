from django.conf.urls import url

from product.views import ProductListView, ProductDetailView, ProductTypeDetailView, ProductTypeListView, \
    UploadProductTypeImageView, UploadProductImageView

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
        regex=r"^(?P<pk>\d+)/upload_image/$",
        view=UploadProductImageView.as_view(),
        name="upload_product_image"
    ),

    url(
        regex=r"^types/$",
        view=ProductTypeListView.as_view(),
        name="product_type_list"
    ),
    url(
        regex=r"^types/(?P<pk>\d+)/$",
        view=ProductTypeDetailView.as_view(),
        name="product_type_detail"
    ),
    url(
        regex=r"^types/(?P<pk>\d+)/upload_image/$",
        view=UploadProductTypeImageView.as_view(),
        name="upload_product_type_image"
    ),
]
