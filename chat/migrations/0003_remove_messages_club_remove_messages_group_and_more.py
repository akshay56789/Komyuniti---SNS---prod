# Generated by Django 5.0.4 on 2024-05-16 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_messages_club'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='club',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='group',
        ),
        migrations.AddField(
            model_name='messages',
            name='room_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]