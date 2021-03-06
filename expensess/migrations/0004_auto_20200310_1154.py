# Generated by Django 3.0.2 on 2020-03-10 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expensess', '0003_expensess_memo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='expensess',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expensess.Category'),
        ),
    ]
