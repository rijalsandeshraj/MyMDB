# Generated by Django 2.2.3 on 2019-07-04 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190704_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Person')),
            ],
            options={
                'unique_together': {('movie', 'person', 'name')},
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, related_name='acting_credits', through='core.Role', to='core.Person'),
        ),
    ]
