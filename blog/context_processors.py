from .models import Kategoriya

def kategoriyalar(request):
    return {
        'kategoriyalar': Kategoriya.objects.all()
    }