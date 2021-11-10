from django.shortcuts import redirect
from django.contrib.auth import logout

class IsCoordinadorSocioProductivoMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
            else:
                user = request.user
                if user.user_profile.rol.id == 10 or user.user_profile.rol.id == 11:
                    return super().dispatch(request, *args, **kwargs)
        logout(request)
        return redirect('educacion:login')