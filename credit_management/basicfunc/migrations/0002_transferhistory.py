# Generated by Django 2.1.4 on 2018-12-21 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicfunc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basicfunc.Participant')),
            ],
        ),
    ]
