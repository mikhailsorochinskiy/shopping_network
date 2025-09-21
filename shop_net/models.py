from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class NetworkNode(models.Model):
    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )

    name = models.CharField(max_length=50, verbose_name='Название предприятия')
    email = models.EmailField(max_length=50, verbose_name='email', blank=True, null=True)
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город', blank=True, null=True)
    street = models.CharField(max_length=50, verbose_name='Улица', blank=True, null=True)
    home_number = models.CharField(max_length=50, verbose_name='Номер дома', blank=True, null=True)
    products = models.ManyToManyField(Product, related_name='nodes', verbose_name="Продукты", blank=True, null=True)
    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        verbose_name="Поставщик"
    )
    debt = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        verbose_name="Задолженность перед поставщиком"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"

    @property
    def level(self):
        if self.supplier is None:
            return 0
        return self.supplier.level + 1

    @property
    def level_display(self):
        """
        Возвращает читаемое название для вычисленного уровня.
        Аналог метода get_FOO_display() для полей с choices.
        """
        calculated_level = self.level  # Вычисляем уровень
        return dict(self.LEVEL_CHOICES).get(calculated_level, 'Неизвестный уровень')
