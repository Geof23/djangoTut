from django.shortcuts import render, redirect
from tabination.views import TabView
from django.contrib.auth.decorators import login_required
from django.utils import decorators
from django import forms
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User


from .forms import RegForm
from .models import Regs


# Create your views here.
class BaseTab(TabView):
    tab_group = 'main_navigation'
    tab_classes = ['main-navigation-tab']

    @property
    def tab_classes(self):
        classes = super(BaseTab, self).tab_classes[:]
        if self.current_tab.request.user.is_authenticated():
            classes += ['logged_in_only']
        return classes
    
class MainTab(BaseTab):
    _is_tab = True
    tab_id = 'main'
    tab_label = 'Home'
    template_name = 'base/tabs/main_tab.html'

class AttendTab(BaseTab):
    _is_tab = True
    tab_id = 'attend'
    tab_label = 'Attendees'
    template_name = 'base/tabs/attend_tab.html'
    def get(self, request):
        regs = Regs.objects.all()
        ctxt = super(AttendTab, self).get_context_data()
        return render(request, self.template_name,
                      {'regs': regs, 'tabs':
                       ctxt['tabs']})
    # def get_context_data(self, **kwargs):
    #     context = super(AttendTab, self).get_context_data(**kwargs)
    #     context
    # ctxt = super(RegTab, self).get_context_data()
    # try:
    #     regs = Regs.objects.get()
    # except Regs.DoesNotExist:
    #     pass
    # return render(request, template_name,
    #               {'regs': regs,
    #                'tabs': ctxt['tabs']})

class FeedbTab(BaseTab):
    _is_tab = True
    tab_id = 'feedb'
    tab_label = 'Feedback'
    template_name = 'base/tabs/feedb_tab.html'
    tab_rel = 'nofollow,noindex'

    @decorators.method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FeedbTab, self).dispatch(*args, **kwargs)

    @property
    def tab_visible(self):
        return self.current_tab.request.user.is_authenticated()
    
class OrgTab(BaseTab):
    _is_tab = True
    tab_id = 'org'
    tab_label = 'Organizers'
    template_name = 'base/tabs/organizers_tab.html'
    
class RegTab(BaseTab):
    _is_tab = True
    tab_id = 'reg'
    tab_label = 'Registration'
    template_name = 'base/tabs/reg_tab.html'
    tab_rel = 'nofollow,noindex'

    @decorators.method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RegTab, self).dispatch(*args, **kwargs)

    @property
    def tab_visible(self):
        return self.current_tab.request.user.is_authenticated()
    
    def get(self, request):
        try:
            reg = Regs.objects.get(pk=request.user)
            form = RegForm(instance=reg)
        except Regs.DoesNotExist:
            form = RegForm()
        ctxt = super(RegTab, self).get_context_data()
        return render(request, 'base/tabs/reg_tab.html',
                       {'form': form, 'tabs':
                           ctxt['tabs']})#, 'tabs': tabs})

    def post(self, request):
        form = RegForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auth = request.user
            post.save()
            ctxt = super(RegTab, self).get_context_data()
        return render(request, 'base/tabs/reg_tab.html',
                      {'form': form,
                       'tabs': ctxt['tabs']
                      })
            
            #return redirect('reg_detail', pk=post.pk)

    def form_valid(self, form):
        return super(RegTab, self).form_valid(form)

class VenueTab(BaseTab):
    _is_tab = True
    tab_id = 'venue'
    tab_label = 'Venue'
    template_name = 'base/tabs/venue_tab.html'
    
