# Generated by Django 5.0.2 on 2024-02-09 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REST', '0007_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contacts',
            field=models.ManyToManyField(related_name='alert_contatcs', to='REST.contact'),
        ),
    ]