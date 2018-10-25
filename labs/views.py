from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import WasteForm
from .models import MyUser, Waste


@login_required
def user_home(request):
    return render(request, 'labs/home.html')


@login_required
def user_data(request):
    data = {'this_user': MyUser.objects.get(user=request.user)}

    return render(request, 'labs/data.html', data)


@login_required
def user_stats(request):
    data = {}
    return render(request, 'labs/stats.html', data)


@login_required
def user_wastes(request):
    # TODO: Modificar para pegar apenas do meu usuário - filter(user = ...)
    data = {'my_wastes': Waste.objects.filter(generator__user=request.user)}

    return render(request, 'labs/wastes.html', data)


@login_required
def user_wastes_create(request):
    form = WasteForm(request.POST or None)

    if form.is_valid():
        waste = form.save(commit=False)
        waste.generator = MyUser.objects.get(user=request.user)
        waste.save()
        return redirect('user_wastes')

    return render(request, 'labs/waste_form.html', {'waste_form': form})


def user_wastes_update(request, waste_id):
    waste = get_object_or_404(Waste, pk=waste_id)
    form = WasteForm(request.POST or None, instance=waste)

    if form.is_valid():
        waste = form.save(commit=False)
        waste.generator = MyUser.objects.get(user=request.user)
        waste.save()
        return redirect('user_wastes')

    return render(request, 'labs/waste_form.html', {'waste_form': form})


def user_wastes_delete(request, waste_id):
    waste = get_object_or_404(Waste, pk=waste_id)

    if request.method == 'POST':
        waste.delete()
        return redirect('user_wastes')

    return render(request, 'labs/waste_delete.html', {'this_waste': waste})
