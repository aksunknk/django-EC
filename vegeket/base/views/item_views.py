from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from base.models import Item, Category, Tag


class IndexListView(ListView):
    model = Item
    template_name = 'pages/index.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'pages/item.html'
    paginate = 2
    queryset = Item.objects.fileter(is_published=True)
    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs["pk"])
        return Item.objects.filter(is_published=True, category=self.category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Category #{self.category.name}"
        return context