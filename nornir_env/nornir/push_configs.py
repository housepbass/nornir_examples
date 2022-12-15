import logging
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from nornir_napalm.plugins.tasks import napalm_configure

nr = InitNornir(config_file="config.yaml")

def generate_config_and_push(task):
    """Render unique device configuration and push to device"""
    rendered_config = task.run(task=template_file, template=f"{task.host.platform}", path="templates/").result
    configure_devices = task.run(task=napalm_configure, dry_run=True, configuration=rendered_config)

results = nr.run(task=generate_config_and_push)
print_result(results)