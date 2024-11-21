from selectolax.parser import Node
from datetime import datetime
import re
import pandas as pd

def get_attrs_from_node(node: Node, attr: str) -> str:
    if node is None or not issubclass(Node, type(node)):
        raise ValueError("The function expects a selecolax node to be provided")
    
    return node.attributes.get(attr)

def get_first_n(items: list, n: int = 5) -> list:

    return items[:n]

def date_formatting(date: str, from_format: str, to_format: str = "%Y-%m-%d"):
    date_obj = datetime.strptime(date, from_format)

    formatted_date = date_obj.strftime(to_format)
    return formatted_date

def get_number(text: str):
    numbers = re.findall(r'\d+', text)
    if numbers:
        return ''.join(numbers)
    return '0'

def get_currency(text: str):
    match = re.search(r'[A-Za-z]+', text)
    if match:
        return match.group()
    else:
        return ''

def format_and_transform(parsed: dict) -> dict:
    transforms = {
        "thumbnail": lambda n: get_attrs_from_node(n, "src"),
        "tags": lambda tags: get_first_n(tags, 5),
        "release_date": lambda date: date_formatting(date, from_format="%b %d, %Y"),
        "review_user": lambda n: int(get_number(n)),
        "price_currency": lambda text: get_currency(text),
        "sale_price": lambda n: float(get_number(n)),
        "original_price": lambda n: float(get_number(n)),
    }

    for k, v in transforms.items():
        if k in parsed:
            parsed[k] = v(parsed[k])

    return parsed

def save_to_file(filename: str = 'extract', data: list[dict] = None):
    if data is None:
        raise ValueError("The function expects data to be provided as a list of dictionaries")
    
    df = pd.DataFrame(data)
    filename = f"{datetime.now().strftime('%Y_%m_%d')}_{filename}.csv"
    df.to_csv(filename, index=False)