from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView
# Create your views here.

# class Login(FormView):
#     template_name = 'login.html'
#     form_class = FormLogin
#     success_url = reverse_lazy('home')

#     @method_decorator(csrf_protect)
#     @method_decorator(never_cache)
#     def dispatch(self,request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return super(Login, self).dispatch(request, *args, **kwargs)
    
#     def form_valid(self, form):
#         print('hola1')
#         login(self.request, form.get_user())
#         print('hola')
#         return super(Login, self).form_valid(form)

# def logoutUsuario(request):
#     logout(request)
#     return HttpResponseRedirect('/login')

class Login2(LoginView):
    template_name = 'app/login.html'

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            id_rol = self.request.user.user_profile.rol.id
            if id_rol == 1 or id_rol == 2:
                return redirect('educacion:home_coordinador_general')
            elif id_rol == 3 or id_rol == 4:
                return redirect('educacion:home_director_general')
            elif id_rol == 5:
                return redirect('educacion:home_director_centro')
            elif id_rol == 6:
                return redirect('educacion:home_maestro')
            elif id_rol == 7 or id_rol == 8:
                return redirect('educacion:municipalizacion')
            elif id_rol == 9:
                return redirect('educacion:home_equipo_municipal')
            elif id_rol == 10 or id_rol == 11:
                return redirect('educacion:home_coordinador_socioproductivo')
            elif id_rol == 12:
                return redirect('educacion:home_equipo_socioproductivo')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        id_rol = self.request.user.user_profile.rol.id
        if id_rol == 1 or id_rol == 2:
            return redirect('educacion:home_coordinador_general')
        elif id_rol == 3 or id_rol == 4:
            return redirect('educacion:home_director_general')
        elif id_rol == 5:
            return redirect('educacion:home_director_centro')
        elif id_rol == 6:
            return redirect('educacion:home_maestro')
        elif id_rol == 7 or id_rol == 8:
            return redirect('educacion:municipalizacion')
        elif id_rol == 9:
            return redirect('educacion:home_equipo_municipal')
        elif id_rol == 10 or id_rol == 11:
            return redirect('educacion:home_coordinador_socioproductivo')
        elif id_rol == 12:
            return redirect('educacion:home_equipo_socioproductivo')
    
