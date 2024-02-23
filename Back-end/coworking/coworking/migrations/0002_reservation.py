# Generated by Django 5.0 on 2024-02-22 22:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworking', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('status', models.CharField(choices=[('pagado', 'Pagado'), ('cancelado', 'Cancelado'), ('en espera', 'En espera')], default='en espera', max_length=15)),
                ('cost', models.FloatField(default=0.0)),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='espacio', to='coworking.space')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
