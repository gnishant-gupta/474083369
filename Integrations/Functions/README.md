
# Functions

A set of math and data manipulation actions created for Google SecOps Community to power up playbook capabilities.

Python Version - 3


#### Dependencies
| |
|-|
|googleapis_common_protos-1.70.0-py3-none-any.whl|
|TIPCommon-2.2.7-py2.py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|
|hashID-3.1.4-py2.py3-none-any.whl|
|filelock-3.18.0-py3-none-any.whl|
|google_auth-2.40.3-py2.py3-none-any.whl|
|charset_normalizer-3.4.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|idna-3.10-py3-none-any.whl|
|google_api_core-2.25.1-py3-none-any.whl|
|webencodings-0.5.1-py2.py3-none-any.whl|
|bleach-6.2.0-py3-none-any.whl|
|jsonpath_ng-1.7.0-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|uritools-5.0.0-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|pillow-11.0.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|httpx-0.28.1-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|anyio-4.9.0-py3-none-any.whl|
|tld-0.13-py2.py3-none-any.whl|
|urlextract-1.9.0-py3-none-any.whl|
|pyparsing-3.2.3-py3-none-any.whl|
|ply-3.11-py2.py3-none-any.whl|
|urllib3-2.5.0-py3-none-any.whl|
|cachetools-5.5.2-py3-none-any.whl|
|platformdirs-4.3.8-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|proto_plus-1.26.1-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|typing_extensions-4.14.0-py3-none-any.whl|
|protobuf-6.31.1-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|pytz-2024.2-py2.py3-none-any.whl|
|xmltodict-0.14.2-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|tinycss2-1.4.0-py3-none-any.whl|
|certifi-2025.6.15-py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|
|google_api_python_client-2.174.0-py3-none-any.whl|


## Actions
#### Convert Time Format
Convert a datetime value from one format to another format.  
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Timezone|Output timezone|False|String||
|Input|The input datetime value that will be converted.|True|String|<input val>|
|From Format|The datetime format the input string is in.  https://strftime.org/|True|String|X|
|To Format|The desired time format of the output.  Use Arrow time format. https://arrow.readthedocs.io/en/stable/#supported-tokens|True|String|YYYY/MM/DD|
|Time Delta In Seconds|Shift parameter that allows to change the output actual time to either the future (positive) or past (negative). This shift is measured in seconds|True|String|0|



##### JSON Results
```json
{}
```



#### Detect Hash Type
This action detects the most likely hash type of entities. Supported types are SHA256, MD5, SHA1, SHA-512.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hashes|One or more hashes that are comma separated. |False|String||



##### JSON Results
```json
[{"Hash": "275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F", "HashType": "SHA-256"}, {"Hash": "202cb962ac59075b964b07152d234b70", "HashType": "MD5"}]
```



#### Calculate Timestamp
Use the 'Calculate Timestamp' action to find a new point in time by moving forward or backward from a starting time.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Input Type|The starting point to be used as the baseline time for the timestamp offset calculation.|False|List|Current Time|
|Custom Timestamp|The specific date and time value that the action uses as its starting point when Input Type is set to Custom Timestamp.|False|String||
|Custom Timestamp Format|The format of the Custom Timestamp when Input Type is set to Custom Timestamp. If no value is provided, the action defaults to epoch time.|False|String|%Y-%m-%dT%H:%M:%S%z|
|Timestamp Delta|A comma-separated list of time offsets that dictates the calculated time change, requiring a supported unit (m - months, d - days, H - hours, M - minutes, S - seconds) and an operator (+ for future, - for past) for each independently processed entry. For example: +30M, -30M, +1d, -24H.|False|String|+30M,-30M|
|Output Timestamp Format|The desired structure for the resulting calculated timestamp. If no value is provided, the action defaults to epoch time.|False|String|%Y-%m-%dT%H:%M:%S%z|



##### JSON Results
```json
{"original_timestamp": "2025-11-10T08:32:41+0000", "calculated_timestamps": {"timestamp+30M": "2025-11-10T09:02:41+0000", "timestamp-30M": "2025-11-10T08:02:41+0000"}}
```



#### Defang Text
This action defangs the input text by replacing http with hxxp, dot with [.] in IPs and @ with [at] in emails.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Input|The input that needs to be defanged.|False|String||



##### JSON Results
```json
{"converted_text": "Check hxxps://example[.]com/path?query=1 and 192[.]168[.]1[.]1 or user.name+tag[at]sub[.]example[.]co[.]uk"}
```



#### Extract IOCs
Extract domains, IP addresses, URLs and Emails from a string.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Input String|The string to extract the IP addresses from.|True|String|<input string>|



##### JSON Results
```json
{"domains": ["google.com"], "ips": ["1.1.1.1"], "urls": ["www.google.com"], "emails": ["user@user.com"]}
```



#### Create Thumbnail
Creates a Base64 Thumbnail of an image.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Base64 Image|The Base64 string of the image.|False|String||
|Thumbnail Size|Comma separated.  Pixels.   X , Y|True|String|250,250|
|Input JSON|Input JSON|False|String||
|Image Key Path|If using Input JSON, the keypath for the image field.|False|String||



##### JSON Results
```json
{"thumbnail": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="}
```



#### Math Arithmetic
A set of built in math operators:
Plus - returns a result for the sum of 2 arguments
Sub - returns a result for 1 argument minus the other
Multi - returns a result for 1 argument multiplied by the other
Div - returns a result for 1 argument divided by the other
Mod - returns the result of the percentage between 2 arguments
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Function|The function you would like to run on 2 given arguments |True|List|Plus|
|Arg 2|The second argument |True|String|{}|
|Arg 1|The first argument|True|String|{}|



##### JSON Results
```json
{}
```



#### Detect IP Type
This action checks if an IP is an IPv4 address or IPv6 address.  IP Address entities will be enriched with IPType field.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IP Addresses|Comma-separated|False|String||



##### JSON Results
```json
[{"Address": "2.2.2.2", "IPType": "IPV4"}, {"Address": "2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF", "IPType": "IPV6"}, {"IPType": "IPV4", "Address": "1.1.1.1"}]
```



#### Ping
Check connectivity
Timeout - 600 Seconds



##### JSON Results
```json
{}
```



#### SanitizeHTML
Given a fragment of HTML, SantizeHTML will parse it according to the HTML5 parsing algorithm and sanitize any disallowed tags or attributes. This algorithm also takes care of things like unclosed and (some) misnested tags.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Tags|Tags is the allowed set of HTML tags. Comma separated list. HTML tags not in this list will be escaped or stripped. |False|String|a,abbr,acronym,b,blockquote,code,em,i,li,ol,strong,ul,table,tr,td,th,h1,h2,h3,body,tbody,thead,div,footer,head,header,html,img,option,p,section,span,strong,svg|
|Attributes|Attributes lets you specify which attributes are allowed. Value should be a comma separated list.Default  {'a': ['href', 'title'], 'abbr': ['title'],|False|String|None|
|Styles|If you allow the style attribute, specify the allowed styles set, for example color and background-color. Value should be comma separated list.|False|String|None|
|Allow All Attributes|Set to True to allow all attributes.|False|Boolean|false|
|Input HTML|The HTML fragment that will be sanitized.|True|String||



##### JSON Results
```json
{}
```



#### String Functions
This action includes basic Pythonic string functions as mentioned below - 
Lower: Converts the input string to lowercase.
Upper: Converts the input string to uppercase (duplicated case in the script).
Strip: Removes leading and trailing whitespaces from the input string.
Title: Converts the first character of each word in the input string to uppercase.
Count: Counts the occurrences of `param_1` in the input string.
Replace: Replaces occurrences of `param_1` with `param_2` in the input string. It supports the placeholder code _SPACE_ in both parameters, which is automatically converted to a standard space before the replacement is performed.
Find: Finds the first occurrence of `param_1` in the input string and returns its index.
IsAlpha: Checks if all characters in the input string are alphanumeric.
IsDigit: Checks if all characters in the input string are digits.
Regex Replace: Performs a regex-based replacement of `param_1` with `param_2` in the input string. It supports the placeholder code _SPACE_ in both parameters, which is automatically converted to a standard space before the replacement is performed.
JSON Serialize: Converts the input string to a JSON formatted string.
Regex: Finds all occurrences of the pattern `param_1` in the input string, joins them using `param_2` (defaulting to ", "), and returns the result.
DecodeBase64: Decodes the input string from base64 using `param_1` as the encoding type. Default to utf-8
EncodeBase64: Encodes the input string in base64 using `param_1` as the encoding type. Default to utf-8
RemoveNewLines: Removes new lines from the input string, replacing them with spaces.
Split: Splits the input string using `param_1` (or "," if not provided) and adds the result to the Siemplify result.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Param 2|The second parameter (this is an optional parameter as some functions require only 1 param)|False|String| |
|Param 1|The first parameter (this is an optional parameter as some functions require only 1 param)|False|String|None|
|Input|The input for the current fuction|True|String|Example|
|Function|Select the function you would like to run from the list|True|List|Lower|



##### JSON Results
```json
{}
```



#### Time Duration Calculator
The Time Duration Calculator will calculate the time that has elapsed/difference between two dates with time.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Input DateTime 1|The first input datetime value.  Supports either strftime format or "now" for the current time.|True|String||
|Input DateTime 1 Format|The strftime format of the DateTime string.https://strftime.org/|True|String|%Y-%m-%dT%H:%M:%S%z|
|Input DateTime 2|The second input datetime value.  Supports either strftime format or "now" for the current time.|True|String|now|
|Input DateTime 2 Format|The strftime format of Input DateTime 2.|True|String|%Y-%m-%dT%H:%M:%S%z|



##### JSON Results
```json
{"years": 0, "days": 31, "hours": 744, "minutes": 44640, "seconds": 2678400, "duration": "Time between dates: 0 years, 31 days, 0 hours, 0 minutes and 0 seconds"}
```



#### XMLtoJson
Convert XML formatted data to JSON.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|xml|Convert XML to JSON|True|String|<e> <a>text</a> <a>text</a> </e>|



##### JSON Results
```json
{}
```



#### Math Functions
A set of built-in Python functions - 
Abs - returns the absolute value of a number
Float - returns a floating point number
Display - converts the number to include commas where needed
Hex - converts a number into a hexadecimal value
Int - returns an integer number
Max - returns the largest item in an iterable 
Min - returns the smallest item in an iterable
Round - rounds a number
Sort - returns a sorted number
Sum - sums the items of an iterator
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Function|Select the Math Function you would like to run on the number|True|List|Max|
|Numbers|The numbers you would like to run the Math function on.|True|String|13.5,-90,566,11.32|



##### JSON Results
```json
{}
```



#### IP to Integer
Converts an IP address or list of IP addresses to integers or longs.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IP Addresses|Comma separated list of IP addresses to be converted into integers.|True|String||



##### JSON Results
```json
{"192.168.1.1": 3232235777, "192.168.1.2": 3232235778}
```



#### Run JSONPath Query
The action runs an JSONPath Query on a given json and extracts values according to the expression.
View https://github.com/h2non/jsonpath-ng for more information on JSONPath
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Json|Json input|True|Code|{}|
|JSONPath Expression|JSONPath expressions always refers to a JSON structure in the same way as XPath expressions are used in combination with an XML document.|True|String||



##### JSON Results
```json
{}
```










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.