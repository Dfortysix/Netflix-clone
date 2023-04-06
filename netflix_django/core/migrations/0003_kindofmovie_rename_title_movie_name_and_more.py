# Generated by Django 4.1.6 on 2023-03-31 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_video_movie_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='KindOfMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='type_of_movie',
            new_name='num_vol',
        ),
        migrations.AddField(
            model_name='movie',
            name='kind',
            field=models.ManyToManyField(to='core.kindofmovie'),
        ),
    ]