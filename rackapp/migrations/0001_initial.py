# Generated by Django 3.1.4 on 2021-01-01 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('siteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('ip', models.GenericIPAddressField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='racks', to='siteapp.site')),
            ],
            options={
                'verbose_name_plural': 'Racks',
            },
        ),
    ]
