# Generated by Django 5.0.4 on 2024-04-20 18:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_groups_chat_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='chat_room',
            field=models.CharField(default='club_chat_gfg', max_length=10),
        ),
        migrations.AddField(
            model_name='club',
            name='image',
            field=models.FileField(blank=True, default='komyuniti-post-image/avatar_mclyfi.jpg', null=True, upload_to='komyuniti-club-image'),
        ),
        migrations.AddField(
            model_name='club',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='club_members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='club',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]