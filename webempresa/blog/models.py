from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User # modelo de usuarios

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Última Actualización")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["-created"]
        
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de Publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE) # si se elimina el autor se eliminan todas las entradas de ese autor
    categories = models.ManyToManyField(Category, verbose_name="Categorías", blank=True, related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Última Actualización")
    
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["-created"]
        
    def __str__(self):
        return self.title
    