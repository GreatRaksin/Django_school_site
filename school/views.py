from django.shortcuts import render
from .models import Tutor, Features
from .forms import TutorSelectForm


# Create your views here.
def index(request):
    features = Features.objects.filter(is_active=True)
    return render(request, 'index.html', {'title': 'Занятия по школьной программе в 100 баллов',
                                          'features': features})


def tutors(request):
    form = TutorSelectForm()
    town = request.GET.get('office')
    predm = request.GET.get('subject')

    if town and predm:
        tutors = Tutor.objects.filter(office=town, subject=predm, school=True)
    else:
        tutors = Tutor.objects.filter(school=True)

    return render(request, 'tutors.html', {'form': form,
                                           'tutors': tutors})
