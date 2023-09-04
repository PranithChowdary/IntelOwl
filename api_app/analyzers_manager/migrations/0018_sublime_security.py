# Generated by Django 4.1.7 on 2023-04-11 09:49

from django.db import migrations
from django.db.models.fields.related_descriptors import ManyToManyDescriptor

objects = [
    {
        "model": "analyzers_manager.analyzerconfig",
        "pk": "SublimeSecurity",
        "fields": {
            "python_module": "sublime.Sublime",
            "description": "Analyze email with sublime security",
            "disabled": False,
            "config": {"queue": "default", "soft_time_limit": 60},
            "secrets": {
                "url": {"type": "str", "required": True, "description": ""},
                "api_key": {"type": "str", "required": True, "description": ""},
                "message_source_id": {
                    "type": "str",
                    "required": True,
                    "description": "",
                },
            },
            "params": {},
            "type": "file",
            "docker_based": False,
            "maximum_tlp": "RED",
            "observable_supported": "[]",
            "supported_filetypes": '["message/rfc822", "application/vnd.ms-outlook"]',
            "run_hash": False,
            "run_hash_type": "",
            "not_supported_filetypes": "[]",
            "disabled_in_organizations": [],
        },
    }
]


def migrate(apps, schema_editor):
    for obj in objects:
        python_path = obj["model"]
        Model = apps.get_model(*python_path.split("."))
        no_mtm = {}
        mtm = {}
        for field, value in obj["fields"].items():
            if type(getattr(Model, field)) != ManyToManyDescriptor:
                no_mtm[field] = value
            else:
                mtm[field] = value
        o = Model(**no_mtm, pk=obj["pk"])
        o.full_clean()
        o.save()
        for field, value in mtm.items():
            attribute = getattr(o, field)
            attribute.set(value)


def reverse_migrate(apps, schema_editor):
    for obj in objects:
        python_path = obj["model"]
        Model = apps.get_model(*python_path.split("."))
        Model.objects.get(pk=obj["pk"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        (
            "analyzers_manager",
            "0017_alter_analyzerconfig_not_supported_filetypes_and_more",
        ),
    ]

    operations = [migrations.RunPython(migrate, reverse_migrate)]
