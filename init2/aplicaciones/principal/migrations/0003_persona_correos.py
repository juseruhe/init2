# Generated by Django 3.1.6 on 2021-08-07 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_remove_persona_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='correos',
            field=models.EmailField(default=5, max_length=200),
            preserve_default=False,
        ),
    ]