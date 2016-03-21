from django.views.generic.detail import DetailView
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Product

# from django.views.generic.list import ListView
# from django.shortcuts import render

# Create your views here.
import random


class ProductDetailView(DetailView):
    model = Product

#     def get_context_data(self, *args, **kwargs):
#         context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
#         instance = self.get_object()
#         # order_by("-title")
#         context["related"] = sorted(Product.objects.get_related(instance)[:6], key=lambda x: random.random())
#         return context


def product_detail_view(request, id):
    # product_instance = Product.objects.get(id=id)

    try:
        product_instance = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    except:
        raise Http404

    template = "products/product_detail.html"
    context = {
        "product": product_instance
    }
    return render(request, template, context)
