from utils.extract import extract_full_body_html
from config.tools import get_config
from utils.parse import parse_raw_attributes
from utils.process import format_and_transform, save_to_file
from selectolax.parser import HTMLParser


if __name__ == '__main__':
    # Get the configuration
    config = get_config()

    # Get the html parser
    html = extract_full_body_html(
        config.get("url"), 
        wait_for=config.get("container").get("selector")
    )
    
    # Get the nodes from html parsed
    name_container = config.get("container").get("name")
    nodes = parse_raw_attributes(html, [config.get("container")]).get(name_container)

    # If fail to get any print FAIL TO FETCHING DATA
    if len(nodes) == 0:
        print("FAIL TO FETCHING DATA")
    # Else
    else:
        # Temporary data storage
        data = []
        for node in nodes:
            # Parse raw attributes
            attrs = parse_raw_attributes(node, config.get('item'))
            # Post-preprocessing parsed attributes
            attrs = format_and_transform(attrs)
            # Store the data into storage
            data.append(attrs)
        
        # Save the file as csv
        save_to_file("extract", data)