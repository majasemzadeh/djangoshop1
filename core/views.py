from django.shortcuts import render

# Create your views here.
from django.views import View


class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            return render(request, 'index.html', {'user': user})
        else:
            return render(request, 'index.html')