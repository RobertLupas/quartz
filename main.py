import json

from data_adder import process

template_file = "./example-data/template.html"
json_file = "./example-data/data.json"
output_file = "./example-data/output.html"

with open(json_file, 'r') as json_file:
  data = json.load(json_file)

with open(output_file, 'w') as output_file:
  output_file.write(process(template_file, data))
