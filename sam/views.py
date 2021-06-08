from django.shortcuts import render, redirect
from .models import data


# Create your views here.
def test(request):
    try:
        obj = data.objects.all()
        return render(request, 'about.html', {'object': obj})
    except:
        return render(request, 'about.html')


def search(request):
    d = request.GET['search']
    objects = data.objects.filter(heading=d)
    return render(request, 'search.html', {'obj': objects})


def delete(request, id):
    data.objects.get(id=id).delete()
    return redirect('about')


def detail(request, id):
    obj = data.objects.get(id=id)
    return render(request, 'detail.html', {'obj': obj})


def update(request, id):
    if request.method == 'POST':
        h = request.POST['form_head']
        d = request.POST['form_des']
        data.objects.filter(id=id).update(heading=h, designation=d)
        return redirect('detail', id=id)

    else:
        obj = data.objects.get(id=id)
        return render(request, 'update.html', {'obj': obj})
