# Generated by Django 3.0.1 on 2020-01-02 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated at')),
                ('zip_code', models.CharField(max_length=6, verbose_name='Zip Code')),
                ('description', models.CharField(max_length=160, verbose_name='Description')),
                ('type', models.CharField(choices=[('individual', 'Individual'), ('corporate', 'Corporate')], default='individual', max_length=10, verbose_name='Type')),
                ('tax_room', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tax Room')),
                ('tax_number', models.CharField(blank=True, max_length=11, null=True, verbose_name='Tax Number')),
                ('editable', models.BooleanField(default=True, editable=False, verbose_name='Is Editable')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='location.District', verbose_name='District')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='location.Province', verbose_name='Province')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Address',
                'db_table': 'addresses',
                'ordering': ('-id',),
            },
        ),
    ]