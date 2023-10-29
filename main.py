import json

from data_adder import process

template_file_path = "./example-data/template.html"
json_file_path = "./example-data/data.json"
output_file_path = "./example-data/output.html"

with open(json_file_path, 'r') as json_file:
  data = json.load(json_file)
  json_file.close()

with open(template_file_path, 'r') as template_file:
  template_contents = template_file.read()
  template_file.close()

with open(output_file_path, 'w') as output_file:
  output_file.write(process(template_contents, data))
  output_file.close()
