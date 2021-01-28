from django.contrib.auth.models import Group, Permission, User
from django.db import models, migrations
import logging
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


logger = logging.getLogger(__name__)

def add_group_permissions(apps, schema_editor):
    content_type = ContentType.objects.get_for_model(User)
    groups = {
        "patient": [
            "can_book_appointment",
            "can_view_appointments",
        ],
        "doctor": [
            "can_view_appointments",
            "can_block_off",
        ],
    }
    
    for group_name, perms in groups.items():
        group, created = Group.objects.get_or_create(name=group_name) 
        if created:
            logger.info(f'{group_name} Group created')
            for perm in perms:
                _perm, created = Permission.objects.get_or_create(codename=perm, name=perm, content_type=content_type) 
                group.permissions.add(_perm)
                logger.info(f'{perm} added to {group_name}')
                group.save()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(add_group_permissions),
    ]
