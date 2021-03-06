# Generated by Django 3.0.8 on 2020-10-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, help_text='short description of the blog', max_length=100, null=True, unique=True)),
                ('name', models.CharField(help_text='Blog description', max_length=200, unique=True)),
                ('blogger', models.CharField(help_text='user name of the blogger', max_length=20)),
                ('post', models.TextField(help_text='blof post')),
                ('overview', models.TextField(default='No overview has been entered for this blog', help_text='a brief overview to invoke eager')),
                ('date', models.DateTimeField(auto_now_add=True, help_text='When the blog post was written')),
                ('category', models.CharField(blank=True, help_text='Used for filtering', max_length=50, null=True)),
                ('comments', models.IntegerField(default=0, help_text='No of comments for particular blog')),
                ('likes', models.IntegerField(default=0, help_text='No of likes for particular blog')),
                ('photo', models.ImageField(blank=True, help_text='An Image for the blog', null=True, upload_to='blog/images/')),
            ],
        ),
        migrations.CreateModel(
            name='BlogLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.CharField(help_text='The blog the like is for', max_length=100)),
                ('user', models.CharField(help_text='The user who liked', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.CharField(help_text='The blog the comment is for', max_length=100)),
                ('comment', models.TextField(help_text='The comment')),
                ('user', models.CharField(blank=True, help_text='The user who commented', max_length=100, null=True)),
                ('email', models.EmailField(blank=True, help_text='Mail address of the commenter', max_length=254, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, help_text='When the comment was added')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(help_text='User feedback')),
                ('name', models.CharField(help_text='user name', max_length=50)),
                ('email', models.EmailField(help_text='email of user', max_length=254)),
                ('subject', models.CharField(help_text='Subject of the contact', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, help_text='A short description of the business for urls', max_length=100, null=True, unique=True)),
                ('name', models.CharField(help_text='The name of the business', max_length=200, unique=True)),
                ('address', models.URLField(help_text='The web address of the business')),
                ('location', models.CharField(help_text='A short description of where the business in located', max_length=150)),
                ('overview', models.TextField(help_text='A brief overview of the business')),
                ('logo', models.ImageField(blank=True, help_text='The logo of the business', null=True, upload_to='listing/images/')),
                ('tag', models.CharField(help_text='Helps to categorize the business', max_length=50)),
                ('category', models.CharField(default='Service Business', help_text='simple category for filtering', max_length=30)),
                ('form', models.CharField(default='Cooperative', help_text='for filtering', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetterSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='email of subscriber', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookingFor', models.CharField(help_text='What the user want to be added to listing', max_length=200)),
            ],
        ),
    ]
