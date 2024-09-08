from django.db import models


class Kitchen(models.Model):

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Кухня'
        verbose_name_plural = 'Кухни'
        ordering = ('ordering',)

    name = models.CharField(max_length=150, verbose_name="Наименование", blank=False, null=False)
    description = models.TextField(verbose_name="Описание", null=False, blank=False)
    price = models.FloatField(null=False, blank=False, verbose_name="Цена")
    ordering = models.SmallIntegerField(null=False, blank=False, verbose_name="Порядок сортировки")
    show_on_site = models.BooleanField(default=True, null=False, blank=False, verbose_name="Отображать на сайте")
    photo_1 = models.ImageField(verbose_name="Изображение №1", blank=True, null=True, upload_to="media/kitchen")
    photo_2 = models.ImageField(verbose_name="Изображение №2", blank=True, null=True, upload_to="media/kitchen")
    photo_3 = models.ImageField(verbose_name="Изображение №3", blank=True, null=True, upload_to="media/kitchen")
    photo_4 = models.ImageField(verbose_name="Изображение №4", blank=True, null=True, upload_to="media/kitchen")


class Grill(models.Model):

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Гриль'
        verbose_name_plural = 'Грили'
        ordering = ('ordering',)

    name = models.CharField(max_length=150, verbose_name="Наименование", blank=False, null=False)
    description = models.TextField(verbose_name="Описание", null=False, blank=False)
    price = models.FloatField(null=False, blank=False, verbose_name="Цена")
    show_on_site = models.BooleanField(default=True, null=False, blank=False, verbose_name="Отображать на сайте")
    ordering = models.SmallIntegerField(null=False, blank=False, verbose_name="Порядок сортировки", default=1)
    photo_1 = models.ImageField(verbose_name="Изображение №1", blank=True, null=True, upload_to="media/grill")


class Contact(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    phone = models.CharField(max_length=150, verbose_name="Телефон", blank=False, null=False)
    whatsapp = models.CharField(max_length=150, verbose_name="Телефон для whatsApp", blank=False, null=False)
    telegram = models.CharField(max_length=150, verbose_name="Для telegram", blank=False, null=False)
    email = models.CharField(max_length=150, verbose_name="Email", blank=False, null=False)
    address = models.TextField(verbose_name="Адрес", blank=False, null=False)
