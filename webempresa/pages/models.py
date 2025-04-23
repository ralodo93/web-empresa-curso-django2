from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    #content = models.TextField(verbose_name="Contenido")
    content = CKEditor5Field(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Última Actualización")
    
    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ["order", "title"]
    
    def __str__(self):
        return self.title