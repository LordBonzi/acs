import uuid
from django.db import models
from django.utils.translation import gettext as _
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Door(models.Model):

    """
    Door model
    """

    DoorName = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    CreatedOn = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Door")
        verbose_name_plural = _("Doors")

    def __str__(self):
        return self.DoorName

    def get_absolute_url(self):
        return reverse("Door_detail", kwargs={"pk": self.pk})


class Reader(models.Model):

    """
    Reader Model
    """

    ReaderLocation = models.CharField(max_length=100)
    ReaderDoor = models.ForeignKey(Door, on_delete=models.CASCADE)
    ReaderModel = models.CharField(max_length=100)
    ReaderType = models.CharField(max_length=100)
    ReaderAddedBy = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Linked to User ID
    CreatedOn = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Reader")
        verbose_name_plural = _("Readers")

    def __str__(self):
        return self.ReaderDoor

    def get_absolute_url(self):
        return reverse("Reader_detail", kwargs={"pk": self.pk})


class Card(models.Model):

    """
    Card Model
    """

    CardID = models.CharField(max_length=100)
    CardUser = models.ForeignKey(User, on_delete=models.CASCADE)  # Linked to User ID
    CreatedOn = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Card")
        verbose_name_plural = _("Cards")

    def __str__(self):
        return self.CardUser

    def get_absolute_url(self):
        return reverse("Card_detail", kwargs={"pk": self.pk})


class Guest(models.Model):

    """
    Guest Model
    """

    GuestFirstName = models.CharField(max_length=100)  #
    GuestLastName = models.CharField(max_length=100)  #
    GuestID = models.CharField(
        max_length=8,
        default=None
    )
    GuestCode = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )  # UUID Used for QR
    GuestEmail = models.EmailField(editable=True, default=None)
    GuestCard = models.ForeignKey(
        Card, on_delete=models.CASCADE, blank=True, null=True
    )  # Guests may be issued with card, linkable, but nullable by default
    GuestAddedBy = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Linked to User ID
    CreatedOn = models.DateTimeField(auto_now_add=True)

    GuestAccessStart = models.DateTimeField(null=False, blank=False,auto_now_add=True)
    GuestAccessEnd = models.DateTimeField(null=False, blank=False,auto_now_add=True)

    class Meta:
        verbose_name = _("Guest")
        verbose_name_plural = _("Guests")

    def __str__(self):
        return self.GuestFirstName + " " + self.GuestLastName

    def get_absolute_url(self):
        return reverse("Guests_detail", kwargs={"pk": self.pk})


class Access(models.Model):

    """
    Access Model
    """

    AccessedBy = models.ForeignKey(User, on_delete=models.CASCADE)  # User
    AccessLocation = models.CharField(max_length=100)
    AccessReader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    AccessedOn = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Access")
        verbose_name_plural = _("Accesses")

    def __str__(self):
        return self.AccessReader + " " + self.AccessedBy

    def get_absolute_url(self):
        return reverse("Access_detail", kwargs={"pk": self.pk})
