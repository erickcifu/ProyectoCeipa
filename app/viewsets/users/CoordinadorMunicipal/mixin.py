from django.shortcuts import redirect
from django.contrib.auth import logout

class IsCoordinadorMunicipalMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
            else:
                user = request.user
                if user.user_profile.rol.id == 7 or user.user_profile.rol.id == 8:
                    return super().dispatch(request, *args, **kwargs)
        logout(request)
        return redirect('educacion:login')