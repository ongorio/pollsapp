from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, FormView, DetailView
from django.db import transaction

from polls.models import Poll, Option, Response
from polls.forms import PollForm

# Create your views here.
class PollListView(ListView):
    model = Poll
    template_name = 'polls/poll_list.html'
    context_object_name = 'polls'


class PollCreateView(FormView):
    form_class = PollForm
    template_name = 'polls/poll_create.html'

    def form_valid(self, form):
        try:
            with transaction.atomic():
                new_poll = Poll(
                    title=form.cleaned_data['title'],
                    description=form.cleaned_data['description']
                )
                new_poll.save()

                poll_options = form.cleaned_data['options'].split('\n')
                options_to_create = []
                for option_value in poll_options:
                    option = Option()
                    option.text = option_value
                    option.poll = new_poll
                    options_to_create.append(option)
                
                Option.objects.bulk_create(options_to_create)

        except Exception as e:
            print(e)

        return redirect(reverse('polls:poll_detail', kwargs={'pk': new_poll.pk}))
    


class PollDetailView(DetailView):
    model = Poll
    context_object_name = 'poll'
    template_name = 'polls/poll_detail.html'
    
