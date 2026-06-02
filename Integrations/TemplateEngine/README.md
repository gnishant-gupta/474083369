
# TemplateEngine

Template Engine integration provides the ability to render templates using Jinja2. Jinja2 provide fast and flexible ways to create rich templates. These templates can be used in entity insights, emails, ticketing systems, or any action that can take in a text string.
Jinja2 documentation can be found at https://jinja.palletsprojects.com/en/2.11.x/ 

Python Version - 3


#### Dependencies
| |
|-|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|six-1.17.0-py2.py3-none-any.whl|
|json2table-1.1.5-py2.py3-none-any.whl|
|json2html-1.3.0.tar.gz|
|setuptools-80.9.0-py3-none-any.whl|
|jinja2-3.1.5-py3-none-any.whl|
|MarkupSafe-3.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|


## Actions
#### Render Template
This action will render a Jinja2 template using a JSON input.  
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|JSON Object|The raw JSON object that will be used to render the template. This value is available as the variable input_json in the Jinja template.|False|Content|{}|
|Jinja|The Jinja template code to be rendered.  Will override Template parameter. Append |safe to disable HTML encoding.|False|Code||
|Include Case Data|When enabled, entity attributes and event data are available under the variables input_json['SiemplifyEvents'] and input_json['SiemplifyEntities']|False|Boolean|false|
|Template|The Jinja2 template to be rendered.  Can be a HTML template from "Settings->Environment" or added in content box.|False|Email Content||



##### JSON Results
```json
{"html_output": "<h1>Hello World!</h1>"}
```



#### Render Template from Array
Render Template, but for lists.  Loops through a list and applies the Jinja template to each list item.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Array input|Point to output from a previous Action that outputs an Array|False|Content|[]|
|Jinja|The Jinja template code to be rendered.  Will override Template parameter. Append |safe to disable HTML encoding.|False|Code|Start
{{ row.name }}
End|
|join|JOIN character between loops to join together|False|String|,|
|prefix|Prefix string before output|False|String|None|
|suffix|Suffix string after output|False|String|None|



##### JSON Results
```json
{"html_output": "<h1>Hello World!</h1>"}
```



#### Ping
Check connectivity
Timeout - 600 Seconds



##### JSON Results
```json
{}
```



#### Entity Insight
This action will use a Jinja2 template to create Entity Insights from a JSON object.  The input JSON object must be in the format of EntityResult.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|JSON Object|The raw JSON object that will be used to render the template.  |True|Content|{}|
|Template|The Jinja2 template to display.  Can be a HTML template from "Settings->Environment" or added in content box.|False|Email Content||
|Triggered By|The name of the integration that triggered this entity insight.|True|String|Siemplify|
|Remove BRs|Remove all <br> tags from the rendered template.|False|Boolean|false|
|Create Insight|When enabled, the action will create entity insights.  Default value of true.|False|Boolean|true|



##### JSON Results
```json
{}
```










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.