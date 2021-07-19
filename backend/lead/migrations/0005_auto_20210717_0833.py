# Generated by Django 3.2.5 on 2021-07-17 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('lead', '0004_alter_lead_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='leads', to='team.team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('inprogress', 'In progress'), ('won', 'won'), ('contacted', 'Contacted'), ('lost', 'lost')], default='new', max_length=100),
        ),
    ]
