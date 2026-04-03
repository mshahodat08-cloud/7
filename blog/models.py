from django.db import models
from django.contrib.auth.models import User


class Kategoriya(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    
class Post(models.Model):
    sarlavha = models.CharField(max_length=200)
    matn = models.TextField()
    muallif = models.ForeignKey(User, on_delete=models.CASCADE)
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)
    yangilangan_sana = models.DateTimeField(auto_now=True)
    nashr_etilgan = models.BooleanField(default=True)
    korildi = models.IntegerField(default=0)
    rasm = models.ImageField(upload_to='postlar/', blank=True, null=True)

    kategoriya = models.ForeignKey(Kategoriya, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha 



class Izoh(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='izohlar')
    muallif = models.ForeignKey(User, on_delete=models.CASCADE)
    matn = models.TextField()
    yaratilgan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.muallif.username} - {self.matn[:20]}"
    

    
