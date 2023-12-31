# Generated by Django 4.2.4 on 2023-08-17 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0002_categories_image_items_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Categorie'},
        ),
        migrations.AlterModelOptions(
            name='items',
            options={'verbose_name': 'Item'},
        ),
        migrations.AddField(
            model_name='items',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category'),
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='item_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='adminside.items')),
            ],
            options={
                'verbose_name': 'Item Image',
            },
        ),
    ]
