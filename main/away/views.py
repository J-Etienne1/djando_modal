from django.shortcuts import render
from django.views.generic import View


class AwayPageView(View):
    template_name = 'away.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
