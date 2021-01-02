# Generated by Django 3.1.4 on 2021-01-02 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clusterapp', '0001_initial'),
        ('slotapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('hostname', models.CharField(max_length=128)),
                ('ip', models.GenericIPAddressField()),
                ('cluster', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vmclusters', to='clusterapp.cluster')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vmslots', to='slotapp.slot')),
            ],
            options={
                'verbose_name_plural': 'VMs',
            },
        ),
    ]
