from django.shortcuts import render
from .models import Tutor
from .forms import TutorSelectForm


# Create your views here.
def index(request):
    return render(request, 'index.html', {'title': 'Z'})


def tutors(request):
    form = TutorSelectForm()
    town = request.GET.get('city')
    predm = request.GET.get('subject')

    if town and predm:
        tutors = Tutor.objects.filter(city=town, subject=predm, school=True)
    else:
        tutors = Tutor.objects.filter(school=True)

    return render(request, 'tutors.html', {'form': form,
                                           'tutors': tutors})
