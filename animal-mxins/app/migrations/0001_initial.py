# Generated by Django 2.0 on 2018-01-19 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('born', models.DateTimeField()),
                ('acquired', models.DateTimeField()),
                ('lays_eggs', models.BooleanField()),
                ('has_feathers', models.BooleanField()),
                ('needs_heat', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete='CASCADE', to='app.Person')),
            ],
        ),
    ]
