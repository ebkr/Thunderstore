from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from repository.models import Package
from repository.models import PackageVersion
from repository.ziptools import PackageVersionForm

from django.shortcuts import redirect


class PackageListView(ListView):
    model = Package
    template_name = "repository/package_list.html"
    paginate_by = 50

    def get_context_date(self, **kwargs):
        context = super(PackageListView, self).get_context_date(**kwargs)
        return context


class PackageDetailView(DetailView):
    model = Package
    template_name = "repository/package_detail.html"


class PackageCreateView(CreateView):
    model = PackageVersion
    form_class = PackageVersionForm
    template_name = "repository/package_create.html"

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PackageCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect(form.instance)