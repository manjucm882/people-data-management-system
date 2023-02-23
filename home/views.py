from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import People, AgeVariant, GenderVariant, Place, Occupation


# List View
class PeopleListView(ListView):
    model = People
    template_name = 'people_list.html'
    context_object_name = 'people'

# Detail View
class PeopleDetailView(DetailView):
    model = People
    template_name = 'people_detail.html'
    context_object_name = 'person'

# Create View
def create_person(request):
    if request.method == 'POST':
        # get the form data
        name = request.POST.get('name')
        age_id = request.POST.get('age')
        gender_id = request.POST.get('gender')
        place_id = request.POST.get('place')
        occupation_id = request.POST.get('occupation')
        image = request.FILES.get('image')

        # create the person object
        person = People.objects.create(
            name=name,
            age_id=age_id,
            gender_type_id=gender_id,
            places_id=place_id,
            occupation_type_id=occupation_id,
            image=image
        )

        return redirect('people_detail', pk=person.pk)
    else:
        # get the age, gender, place, and occupation objects
        age_variants = AgeVariant.objects.all()
        gender_variants = GenderVariant.objects.all()
        places = Place.objects.all()
        occupations = Occupation.objects.all()

        # render the form template
        return render(request, 'person_form.html', {
            'age_variants': age_variants,
            'gender_variants': gender_variants,
            'places': places,
            'occupations': occupations
        })

# Update View
def update_person(request, pk):
    # get the person object
    person = get_object_or_404(People, pk=pk)

    if request.method == 'POST':
        # get the form data
        person.name = request.POST.get('name')
        person.age_id = request.POST.get('age')
        person.gender_type_id = request.POST.get('gender')
        person.places_id = request.POST.get('place')
        person.occupation_type_id = request.POST.get('occupation')
        person.image = request.FILES.get('image')

        # save the person object
        person.save()

        return redirect('people_detail', pk=person.pk)
    else:
        # get the age, gender, place, and occupation objects
        age_variants = AgeVariant.objects.all()
        gender_variants = GenderVariant.objects.all()
        places = Place.objects.all()
        occupations = Occupation.objects.all()

        # render the form template with the existing data
        return render(request, 'person_form.html', {
            'person': person,
            'age_variants': age_variants,
            'gender_variants': gender_variants,
            'places': places,
            'occupations': occupations
        })

# Delete View
def delete_person(request, pk):
    # get the person object
    person = get_object_or_404(People, pk=pk)

    # delete the person object
    person.delete()

    return redirect('people_list')