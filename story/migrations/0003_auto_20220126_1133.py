# Generated by Django 3.1.6 on 2022-01-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_alter_comment_author_alter_comment_story_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='result',
            new_name='likes',
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='story',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
