from django.shortcuts import redirect
from django.contrib.auth import logout

class RolesCooEducacionDirectorCentroMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
            else:
                user = request.user.user_profile.rol.id
                if user == 5 or user == 1 or user == 2:
                    return super().dispatch(request, *args, **kwargs)
        logout(request)
        return redirect('educacion:login')