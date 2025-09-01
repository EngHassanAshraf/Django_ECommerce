from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(_("category"), max_length=50)

    def __str__(self):
        self.name


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("uesrs")

    def __str__(self):
        return f"{self.first_name} {self.last_name}" if self.first_name else self.email


class Product(models.Model):
    name = models.CharField(_("Name"), max_length=1000)
    price = models.DecimalField(_("Price"), default=0.0, max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)
    description = models.TextField(_("Description"), blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to="products/%Y/%M/%d")

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(
        "Product",
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
    )
    customer = models.ForeignKey(
        "User",
        verbose_name=_("Customer"),
        on_delete=models.CASCADE,
    )

    quantity = models.SmallIntegerField(_("Quantity"), default=1)
    shipping_to = models.CharField(
        _("Shipping To"),
        max_length=250,
        default="",
        null=True,
        blank=True,
    )
    phone = models.CharField(_("Phone Number"), max_length=15, default="", blank=True)
    date = models.DateField(default=datetime.today)
    created_at = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(_("Status"), default=False)

    def __str__(self):
        return f"{self.product}"
