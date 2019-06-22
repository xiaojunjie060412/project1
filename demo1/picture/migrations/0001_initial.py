# Generated by Django 2.2.2 on 2019-06-19 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('headimage', models.ImageField(upload_to='media')),
                ('dictum', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=20)),
                ('info', models.CharField(default=None, max_length=200)),
                ('headimage', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='MyPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='media')),
                ('intro', models.CharField(max_length=200)),
                ('belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picture.Photographer')),
                ('classify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picture.Classify')),
            ],
        ),
        migrations.AddField(
            model_name='classify',
            name='photographer',
            field=models.ManyToManyField(to='picture.Photographer'),
        ),
    ]
