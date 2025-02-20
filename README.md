# Quartz (old prototype)

An old prototype of an HTML templating engine, made in Python. It's just an experiment, not a project I'll be working on.

***

Quartz is a web templating engine built in Python, that generates HTML files as output.

⚠️ This project is unpolished. I don't even recommend forking, if you want to work on something like this, do it from scratch :)

***

## Usage
- Step 1: Provide a template HTML file, with `%value name%` instead of actual values, where you want them to be customizable. Then, provide a JSON file with the value names and their corresponding values.
Example:

  `template.html`
  ```html
  <!DOCTYPE html>
  <html lang="%lang%">
  <head>
    <meta charset="UTF-8">
    <title>%title%</title>
  </head>
  <body>
    <p>Name: %name%</p>
  </body>
  </html>
  ```
  
  `data.json`
  ```json
  {
    "values": {
      "lang":"en",
      "name":"Robert",
      "title":"My Site"
    }
  }
  ```

- Step 2: Run `main.py`

  ```bash
  python main.py
  ```

- The output will be provided in `output.html`
