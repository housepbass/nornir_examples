from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file

nr = InitNornir(config_file="config.yaml")

def generate_config(task):
    task.run(task=template_file, template=f"{task.host.platform}", path="templates/")

results = nr.run(task=generate_config)
print_result(results)