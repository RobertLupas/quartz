import json
import re


def process(template_content, data):

  # Regular expression to find IDs like %ID%
  IDs = re.findall(r'%(\w+)%', template_content)

  # Check if all IDs exist in the JSON data
  for ID in IDs:
    if ID not in data["values"]:
      raise ValueError(f"ID '{ID}' not found in the JSON data.")

  # Replace IDs in the template with data from JSON
  processed_html = template_content
  for ID in IDs:
    processed_html = processed_html.replace(f'%{ID}%', str(data["values"][ID]))

  # Return processed HTML
  return processed_html
