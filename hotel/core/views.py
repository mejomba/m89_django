from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from .forms import CustomUserCreationForm, ReserveRoomForm
from .models import Room, UserRoom


class Home(generic.ListView):
    template_name = 'core/home.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        rooms = Room.objects.filter(bed_count__gt=0)
        return rooms


class RoomDetail(generic.DetailView):
    model = Room
    template_name = 'core/room_detail.html'
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReserveRoomForm()
        return context


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'core/signup.html'


def profile(request):
    user_room = UserRoom.objects.filter(user_id=request.user)
    print(user_room)
    for item in user_room:
        print(item.room_id.room_number)
    context = {'user_room': user_room}

    return render(request, 'core/profile.html', context)


@login_required(login_url='login')
def reserve_room(request):

    return render(request, 'core/reserve.html', {})
