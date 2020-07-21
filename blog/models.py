from autoslug import AutoSlugField
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.html import format_html


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nombre')
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        ordering = ['name', 'id']
        verbose_name = 'Etiqueta'

    def __str__(self):
        return '{}, {}'.format(self.name, self.slug)

    def get_btn(self):
        return format_html('<a class="button" href="#">Ver</a>')
    get_btn.short_description = 'Ver'

    def get_posts(self):
        return self.post_set.filter(draft=False).count()

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    content = models.TextField(max_length=300, verbose_name='Contenido')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Ultima modificación')
    draft = models.BooleanField(default=True, verbose_name='Borrador')
    publish_date = models.DateField(verbose_name='Fecha de publicación')
    tags = models.ManyToManyField(Tag, verbose_name='Etiquetas')
    slug = AutoSlugField(populate_from='title', unique=True)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog/uploads/')

    class Meta:
        ordering = ['-created_date', 'title']
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'

    def image_preview(self):
        if self.image:
            return format_html('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return ""
    image_preview.short_description = 'Imagen'

    def short_content(self):
        return truncatechars(self.content, 100)
    short_content.short_description = 'Contenido'

    def get_btn(self):
        return format_html('<a class="button" href="#">Ver</a>')
    get_btn.short_description = 'Ver'

    def get_tags(self):
        return ", ".join([p.name for p in self.tags.all()])
    get_tags.short_description = 'Etiquetas'
