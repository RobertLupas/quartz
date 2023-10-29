import json

from data_adder import process

template_file_path = "./example-data/template.html"
json_file = "./example-data/data.json"
output_file = "./example-data/output.html"

with open(json_file, 'r') as json_file:
  data = json.load(json_file)
  json_file.close()

with open(template_file_path, 'r') as template:
  template_contents = template.read()
  template.close()

with open(output_file, 'w') as output_file:
  output_file.write(process(template_contents, data))
  output_file.close()