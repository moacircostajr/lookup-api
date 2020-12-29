# Generated by Django 3.0.7 on 2020-07-02 13:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('day', models.DateField()),
                ('income', models.FloatField()),
                ('expense', models.FloatField()),
                ('cash', models.FloatField()),
                ('accumulated', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('id_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.Company')),
            ],
        ),
    ]
