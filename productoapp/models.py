from django.db import models

class Categoria(models.Model):
    descripcion = models.CharField(max_length=64)
    class Meta:
        verbose_name = ('Categoria')
        verbose_name_plural = ('Categorias')

    def __str__(self):
        return f"{self.descripcion}"

class Producto(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='producto/')
    contenido = models.TextField(max_length=2000)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ('Producto')
        verbose_name_plural = ('Productos')

    def __unicode__(self):
        return self.titulo
