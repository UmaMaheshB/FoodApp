from django.views import generic
from .models import Restaurant, Item
from django.core.urlresolvers import reverse
#from django.urls import reverse_lazy
try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.core.urlresolvers import reverse
    from django.utils.functional import lazy
    reverse_lazy = lambda *args, **kwargs: lazy(reverse, str)(*args, **kwargs)
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import UserForm
from django.contrib.auth import login, authenticate
from django.views.generic import View
from .models import Item
from django.contrib.auth.decorators import login_required
# Create your views here.
# restaurant functions


class RestaurantIndexView(generic.ListView):
    print("restaurant index fun")
    template_name = 'app/restaurant_index.html'

    def get_queryset(self):
        return Restaurant.objects.all()


class RestaurantDetailView(generic.DetailView):
    model = Restaurant
    template_name = 'app/restaurant_detail.html'


class RestaurantCreate(CreateView):
    model = Restaurant
    fields = ['name', 'location', 'email', 'mobile']


class RestaurantUpdate(UpdateView):
    model = Restaurant
    fields = '__all__'


class RestaurantDelete(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('app:restaurant-index')

# item functions


class ItemIndexView(generic.ListView):
    template_name = 'app/item_index.html'
    
    def get_queryset(self):
        return Item.objects.all()


class ItemDetailView(generic.DetailView):
    print("albmu detailview fun")
    model = Item
    template_name = 'app/item_detail.html'


class ItemCreate(CreateView):
    model = Item
    fields = '__all__'


class ItemUpdate(UpdateView):
    model = Item
    fields = '__all__'


class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('app:item-index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'app/registeration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('app:restaurant-index')
        return render(request, self.template_name, {'form': form})

def itemsearch(request):
	item=request.GET['item']
	items=Item.objects.filter(item__contains=item)
	return render(request,'app/item_index.html',{'object_list':items}) 