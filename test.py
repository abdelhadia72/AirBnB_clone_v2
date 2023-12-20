import re

args = 'city_id="0001" user_id="0001" name=\"My house big\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297'

if not args:
    raise ValueError("No arguments provided.")

args = re.sub(r'name="([^"]+)"', lambda match: f'name="{match.group(1).lower().replace(" ", "_")}"', args)
arg_list = args.split(" ")
kw = {}

for arg in arg_list[1:]:
    arg_splited = arg.split("=")
    if len(arg_splited) == 2:
        key = arg_splited[0]
        value = arg_splited[1]

        if isinstance(value, str):
            value = value.replace('\\"', '"')

        kw[key] = value
        print(kw)