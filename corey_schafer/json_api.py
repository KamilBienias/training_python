import json
from urllib.request import urlopen
import re

passed_url = input("Pass url: ")

with urlopen(passed_url) as response:
    source = response.read()

print("Shows whole site")
print(source)
source_as_string = str(source)
# print("Shows whole site as string")
# print(source_as_string)
passed_expression = input("Pass expression you are looking for: ")
result_of_searching = re.findall(passed_expression, source_as_string)
print(result_of_searching)
how_many_times = len(result_of_searching)
print("Expression", passed_expression, "appears", how_many_times, "times")
print()

expression_as_dict = {
    "expression_name": passed_expression,
    "appears_times": how_many_times
}
print("expression_as_dict looks like that")
print(expression_as_dict)

print()
print("expression_as_json looks like that")
expression_as_json = json.dumps(expression_as_dict, indent=2)
print(expression_as_json)

print("Saves expression_as_dict to expression.json")
with open("expression.json", "w") as f:
    json.dump(expression_as_dict, f, indent=2)

# data = json.loads(source)

# print(json.dumps(data, indent=2))

# usd_rates = dict()
#
# for item in data['list']['resources']:
#     name = item['resource']['fields']['name']
#     price = item['resource']['fields']['price']
#     usd_rates[name] = price
#
# print(50 * float(usd_rates['USD/INR']))