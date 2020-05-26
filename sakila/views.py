from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Customer


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Customer


class IndexView(generic.ListView):
    template_name = 'sakila_list.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Customer.objects.order_by('-last_update')[:100]

    # members_list = Member.objects.all()
    # paginator = Paginator(members_list, 5)
    # page = request.GET.get('page')
    # try:
    #     members = paginator.page(page)
    # except PageNotAnInteger:
    #     members = paginator.page(1)
    # except EmptyPage:
    #     members = paginator.page(paginator.num_pages)
    # return render(request, 'list.html', {'members': members})

# class DetailView(generic.DetailView):
#     model = Customer
#     template_name = 'sakila_detail.html'

class DetailView(generic.edit.UpdateView):
    model = Customer
    fields = '__all__' # ['first_name']
    template_name = 'customer_update_form.html'
    # template_name_suffix = '_update_form'
    # template_name = 'sakila_detail.html'


# class DeleteView(generic.UpdateView):
#     model = Customer
#     template_name_suffix = '_update_form'

class DeleteView(generic.edit.DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('sakila:customer_index')
