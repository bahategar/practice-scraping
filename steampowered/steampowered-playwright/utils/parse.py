from selectolax.parser import Node, HTMLParser
from typing import Union

def parse_raw_attributes(node: Union[Node, str], items: list) -> dict :
    if not issubclass(Node, type(node)) or not issubclass(str, type(node)):
        ValueError("Make sure the node type is str or Node selectolax.")

    if issubclass(str, type(node)):
        node = HTMLParser(node)
    
    parsed = {}
    for item in items:
        match = item.get("match")
        type_ = item.get("type")
        selector = item.get("selector")
        name = item.get("name")

        if match == "all":
            matched = node.css(selector)
            if matched:
                if type_ == 'text':
                    parsed[name] = [n.text() for n in matched]
                elif type_ == 'node':
                    parsed[name] = matched
            else:
                parsed[name] = ''
        
        elif match == "first":
            matched = node.css_first(selector)

            if matched:
                if type_ == 'text':
                    parsed[name] = matched.text()
                elif type_ == 'node':
                    parsed[name] = matched
            else:
                parsed[name] = ''

    return parsed