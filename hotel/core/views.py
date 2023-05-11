import time

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from .forms import CustomUserCreationForm, ReserveRoomForm, CustomLoginForm, OtpForm
from .models import Room, UserRoom, User
from .tokens import account_activation_token

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


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

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print('form')
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "فعال سازی حساب کاربری"
            context = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            }
            print(current_site, context['uid'], context['token'])
            message = render_to_string('core/acc_activate_email.html', context)
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            print('before send')
            # time.sleep(5)
            email.send()
            print('email send')
            return HttpResponse('برو ایمیلت رو چک کن')
        else:
            form = CustomUserCreationForm(request.POST)
            return render(request, 'core/signup.html', {'form': form})

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'core/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user: User = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('profile')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('لینک منقضی شده')

class Login(generic.View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        form_login = CustomLoginForm(request.POST)
        form_otp = OtpForm(request.POST)

        if form_login.is_valid():
            print('login form')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                import random
                otp_code = random.randint(1111, 9999)
                print(otp_code)
                request.session['abc'] = user.id
                cache.set(user.id, otp_code, CACHE_TTL)
                form = OtpForm(request.POST)
                return render(request, 'core/login.html', {'form': form})

        if form_otp.is_valid():
            user_otp_code = request.POST.get('otp')
            user_id = request.session['abc']
            cache_otp = cache.get(request.session['abc'])
            if int(user_otp_code) == int(cache_otp):
                user = User.objects.get(id=user_id)
                login(request, user)
                return redirect('profile')
            else:
                message = 'وقت تموم شد یا کد اشتباه زدی'
                return render(request, 'core/login.html', {'message': message})

        return render(request, 'core/login.html', {'form': form_login})

    def get(self, request):
        form = CustomLoginForm()
        return render(request, 'core/login.html', {'form': form})


class VerifyLogin(generic.View):
    def post(self, request):
        form = OtpForm(request.POST)
        if form.is_valid():
            pass

@login_required(login_url='login')
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
