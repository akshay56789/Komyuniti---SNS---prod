# Generated by Django 5.0.4 on 2024-04-15 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_comments_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='chat_room',
            field=models.CharField(default='group_chat_gfg', max_length=10),
        ),
    ]