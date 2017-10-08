from .forms import CompanyForm, ToolForm, ToolEntryForm
from .models import User, Company, ToolCategory, Tool, ToolField, ToolEntry
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404, QueryDict
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

####### COMPANY #######
#Allows an auth user to create a company.
class CompanyCreate(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        return super(CompanyCreate, self).form_valid(form)

    def get_template_names(self):
        if self.request.is_ajax():
            return ['business/company_form.html']
        else:
            raise Http404

#Allows a user to view a published company.
class CompanyDetail(DetailView):
    model = Company
    slug_url_kwarg = 'company'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetail, self).get_context_data(**kwargs)
        company = get_object_or_404(Company, slug=self.kwargs['company'])
        context['tools'] = Tool.objects.filter(company=company.pk)
        return context

#Allows a user to retrieve a list of companies.
class CompanyList(ListView):
    model = Company
    paginate_by = 10
    context_object_name = 'companies'

    def get_queryset(self):
        queryset = Company.objects.all().order_by('-published')
        query = self.request.GET.get("q")
        sort = self.request.GET.get("s")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(author__username__icontains=query)
                ).distinct()
        if sort:
            queryset = queryset.all().order_by(sort)
        return queryset

#Allows a user to retrieve a list of companies for a specific author.
class CompanyAuthorList(ListView):
    model = Company
    paginate_by = 10
    template_name_suffix = '_author'
    context_object_name = 'companies'

    def get_queryset(self):
        author = get_object_or_404(User, username=self.kwargs['user'])
        queryset = Company.objects.filter(author=author).order_by('-published')
        query = self.request.GET.get("q")
        sort = self.request.GET.get("s")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(author__username__icontains=query)
                ).distinct()
        if sort:
            queryset = queryset.all().order_by(sort)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyAuthorList, self).get_context_data(*args, **kwargs)
        context['author'] = get_object_or_404(User, username=self.kwargs['user'])
        return context

#Allows an author to update a company he has created.
class CompanyUpdate(UpdateView):
    model = Company
    form_class = CompanyForm
    slug_url_kwarg = 'company'

    def get_template_names(self):
        if self.request.is_ajax():
            return ['business/company_update_form.html']
        else:
            raise Http404

    def get_queryset(self):
        return Company.objects.filter(author=self.request.user)

#Allows an auth user to delete a company he has created.
class CompanyDelete(DeleteView):
    model = Company
    slug_url_kwarg = 'company'

    def get_template_names(self):
        if self.request.is_ajax():
            return ['business/company_delete.html']
        else:
            raise Http404

    def get_queryset(self):
        return Company.objects.filter(author=self.request.user)

    def get_success_url(self):
        author = self.object.author.username
        return reverse_lazy('business:company_author', kwargs={'user': author})

####### TOOL #######
#Allows a user to view a ToolCategory and its Tools.
class ToolCategoryDetail(ListView):
    model = Tool
    paginate_by = 10
    template_name = 'business/tool_category_detail.html'
    context_object_name = 'tools'

    def get_queryset(self):
        category = get_object_or_404(ToolCategory, slug=self.kwargs['category'])
        queryset = Tool.objects.filter(category=category).order_by('-published')
        query = self.request.GET.get("q")
        sort = self.request.GET.get("s")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(author__username__icontains=query) |
                Q(company__title__icontains=query)
                ).distinct()
        if sort:
            queryset = queryset.all().order_by(sort)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ToolCategoryDetail, self).get_context_data(*args, **kwargs)
        context['category'] = get_object_or_404(ToolCategory, slug=self.kwargs['category'])
        return context

#Allows a user to view a published tool.
class ToolDetail(DetailView):
    model = Tool
    slug_url_kwarg = 'tool'

#Allows a user to retrieve a list of Tools for a specific author.
class ToolAuthorList(ListView):
    model = Tool
    paginate_by = 10
    template_name_suffix = '_author'
    context_object_name = 'tools'

    def get_queryset(self):
        author = get_object_or_404(User, username=self.kwargs['user'])
        category = get_object_or_404(ToolCategory, slug=self.kwargs['category'])
        queryset = Tool.objects.filter(author=author, category=category).order_by('-published')
        query = self.request.GET.get("q")
        sort = self.request.GET.get("s")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(author__username__icontains=query) |
                Q(company__title__icontains=query)
            ).distinct()
        if sort:
            queryset = queryset.all().order_by(sort)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ToolAuthorList, self).get_context_data(*args, **kwargs)
        context['author'] = get_object_or_404(User, username=self.kwargs['user'])
        context['category'] = get_object_or_404(ToolCategory, slug=self.kwargs['category'])
        return context

#Allows an auth user to create a Tool.
class ToolCreate(LoginRequiredMixin, CreateView):
    model = Tool
    form_class = ToolForm

    def get_context_data(self, **kwargs):
        context = super(ToolCreate, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(Company, slug=self.kwargs['company'])
        context['category'] = get_object_or_404(ToolCategory, slug=self.kwargs['category'])
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        category = get_object_or_404(ToolCategory, slug=self.kwargs['category'])
        instance.category = category
        company = get_object_or_404(Company, slug=self.kwargs['company'])
        instance.company = company
        return super(ToolCreate, self).form_valid(form)

    def get_template_names(self):
        if self.request.is_ajax():
            return ['business/tool_form.html']
        else:
            raise Http404

#Allows an author to update a Tool he created.
class ToolUpdate(UpdateView):
    model = Tool
    form_class = ToolForm
    slug_url_kwarg = 'tool'

    def get_context_data(self, **kwargs):
        context = super(ToolUpdate, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(Company, slug=self.kwargs['company'])
        context['category'] = get_object_or_404(ToolCategory, slug=self.kwargs['category'])
        context['tool'] = get_object_or_404(Tool, slug=self.kwargs['tool'])
        return context

    def get_queryset(self):
        return Tool.objects.filter(author=self.request.user)

    def get_template_names(self):
        if self.request.is_ajax():
            return ['business/tool_update_form.html']
        else:
            raise Http404

#Allows an auth user to delete a Tool he created.
class ToolDelete(DeleteView):
    model = Tool
    slug_url_kwarg = 'tool'

    def get_template_names(self):
        if self.request.is_ajax():
            return ['business/tool_delete.html']
        else:
            raise Http404

    def get_success_url(self):
        company = self.object.company.slug
        return reverse_lazy('business:company_detail', kwargs={'company': company})

#Allows an auth user to create a ToolEntry.
class ToolEntryCreate(LoginRequiredMixin, CreateView):
    model = ToolEntry
    form_class = ToolEntryForm

    def get_context_data(self, **kwargs):
        context = super(ToolEntryCreate, self).get_context_data(**kwargs)
        context['category'] = get_object_or_404(ToolCategory, slug=self.kwargs['category'])
        context['tool'] = get_object_or_404(Tool, slug=self.kwargs['tool'])
        context['field'] = get_object_or_404(ToolField, pk=self.kwargs['field_pk'])
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        field = get_object_or_404(ToolField, pk=self.kwargs['field_pk'])
        instance.field = field
        instance.author = self.request.user
        tool = get_object_or_404(Tool, slug=self.kwargs['tool'])
        instance.tool = tool
        category = get_object_or_404(ToolCategory, slug=self.kwargs['category'])
        instance.category = category
        return super(ToolEntryCreate, self).form_valid(form)

    def get_template_names(self):
        if self.request.is_ajax():
            return ['business/tool_entry_form.html']
        else:
            raise Http404

#Allows an author to update a ToolEntry he created.
class ToolEntryUpdate(UpdateView):
    model = ToolEntry
    form_class = ToolEntryForm
    pk_url_kwarg = 'entry_pk'

    def get_context_data(self, **kwargs):
        context = super(ToolEntryUpdate, self).get_context_data(**kwargs)
        context['category'] = get_object_or_404(ToolCategory, slug=self.kwargs['category'])
        context['tool'] = get_object_or_404(Tool, slug=self.kwargs['tool'])
        context['field'] = get_object_or_404(ToolField, pk=self.kwargs['field_pk'])
        context['entry'] = get_object_or_404(ToolEntry, pk=self.kwargs['entry_pk'])
        return context

    def get_queryset(self):
        return ToolEntry.objects.filter(author=self.request.user)

    def get_template_names(self):
        if self.request.is_ajax():
            return ['business/tool_entry_update_form.html']
        else:
            raise Http404

#Allows an auth user to delete a ToolEntry he created.
class ToolEntryDelete(DeleteView):
    model = ToolEntry
    pk_url_kwarg = 'entry_pk'

    def get_template_names(self):
        if self.request.is_ajax():
            return ['business/tool_entry_delete.html']
        else:
            raise Http404

    def get_success_url(self):
        tool = self.object.tool
        return reverse_lazy('business:tool_detail', kwargs={'company': tool.company.slug, 'category': tool.category.slug, "tool": tool.slug,})
