# Generated by Django 3.0.1 on 2019-12-30 14:21

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publisher', '0001_initial'),
        ('author', '0001_initial'),
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('list_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='List Price')),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Sale Price')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('on_sale', models.BooleanField(default=True, verbose_name='On Sale')),
                ('authors', models.ManyToManyField(to='author.Author', verbose_name='Authors')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'books',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='book.Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='BookMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated at')),
                ('isbn', models.CharField(blank=True, max_length=13, null=True, unique=True, verbose_name='ISBN')),
                ('number_of_pages', models.IntegerField(blank=True, null=True, verbose_name='Number of Pages')),
                ('number_of_prints', models.IntegerField(blank=True, null=True, verbose_name='Number of Prints')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Release Date')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book.Book', verbose_name='Book')),
                ('dimension', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shared.Dimension', verbose_name='Dimension')),
                ('translators', models.ManyToManyField(blank=True, to='author.Translator', verbose_name='Translators')),
            ],
            options={
                'verbose_name': 'Book Meta',
                'verbose_name_plural': 'Book Meta',
                'db_table': 'book_meta',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='book.Category', verbose_name='Categories'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='publisher.Publisher', verbose_name='Publisher'),
        ),
    ]
