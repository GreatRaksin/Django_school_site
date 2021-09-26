from django.shortcuts import render
from .models import Tutor, Features, Offices, Lessons
from .forms import TutorSelectForm


# Create your views here.
def index(request):
    features = Features.objects.filter(is_active=True).order_by('order')
    return render(request, 'index.html', {'title': 'Занятия по школьной программе в 100 баллов',
                                          'features': features})


def tutors(request):
    form = TutorSelectForm()
    town = request.GET.get('office',)
    office_name = Offices.objects.filter(id=town)
    

    if town:
        tutors = Tutor.objects.filter(office=town, school=True)
        
    else:
        tutors = Tutor.objects.filter(school=True)

    return render(request, 'tutors.html', {'form': form,
                                           'tutors': tutors,
        'office': office_name,
    })
    
def extra_lessons(request):
    lessons_5 = Lessons.objects.filter(is_active=True, forms=1)
    lessons_6 = Lessons.objects.filter(is_active=True, forms=2)
    lessons_7 = Lessons.objects.filter(is_active=True, forms=3)
    lessons_8 = Lessons.objects.filter(is_active=True, forms=4)
    lessons_9 = Lessons.objects.filter(is_active=True, forms=5)
    lessons_10 = Lessons.objects.filter(is_active=True, forms=6)
    lessons_11 = Lessons.objects.filter(is_active=True, forms=7)

    return render(request, 'lessons.html', {'l_5': lessons_5,
                                            'l_6': lessons_6,
                                            'l_7': lessons_7,
                                            'l_8': lessons_8,
                                            'l_9': lessons_9,
                                            'l_10': lessons_10,
                                            'l_11': lessons_11,
                                            })
