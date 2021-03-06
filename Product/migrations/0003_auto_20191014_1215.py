# Generated by Django 2.1.5 on 2019-10-14 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_auto_20191014_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete='SET_NULL', related_name='subcategory', to='Product.Category'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='Product.Category'),
        ),
    ]
