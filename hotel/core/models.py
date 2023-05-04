from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel, AbstractUser):
    choice = (('a', 'admin'), ('u', 'user'))
    role = models.CharField(choices=choice, max_length=1, null=True, blank=True, default='u')


class Room(BaseModel):
    room_number = models.PositiveIntegerField(unique=True)
    bed_count = models.PositiveIntegerField()
    bed_price = models.PositiveIntegerField()
    user = models.ManyToManyField(User, through='UserRoom', related_name='user_room')

    def __str__(self):
        return f'room:{self.room_number} - bed:{self.bed_count}'

    @property
    def is_full(self):
        if self.bed_count == 0:
            return True
        return False


class UserRoom(models.Model):
    user_id = models.ForeignKey(User, related_name='user_userroom_id', on_delete=models.PROTECT)
    room_id = models.ForeignKey(Room, related_name='room_userroom_id', on_delete=models.PROTECT)
    enter_date = models.DateTimeField()
    exit_date = models.DateTimeField()