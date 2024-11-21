import json

# NOTE: 
#   - We assume that only one container that we will extract

_config = {
    "url": "https://store.steampowered.com/specials",
    "meta": {
        "name": "Steam Sales Scraper",
        "description": "Extracts the special offer games from steam",
        "author": "Quentin Bauer",
        "version": 0.1,
    }
    "container": {
        "name": "store_sale_divs",
        "selector": "div[class*='sale_item_browser']  div[class*='ImpressionTrackedElement']",
        "match": "all",
        "type": "node",
    },
    "item": [
        {
            "name": "title",
            "selector": "div[class*=StoreSaleWidgetTitle]",
            "match": "first",
            "type": "text",
        },
        {
            "name": "thumbnail",
            "selector": "img",
            "match": "first",
            "type": "node",
        },
        {
            "name": "tags",
            "selector": "*[class*='WidgetTag']",
            "match": "all",
            "type": "text",
        },
        {
            "name": "release_date",
            "selector": "div:has(span):nth-child(3) > div:nth-child(2) > div",
            "match": "first",
            "type": "text",
        },
        {
            "name": "review_score",
            "selector": "a[class*='ReviewScore'] > div > div:nth-child(1)",
            "match": "first",
            "type": "text",
        },
        {
            "name": "review_user",
            "selector": "a[class*='ReviewScore'] > div > div:nth-child(3)",
            "match": "first",
            "type": "text",
        },
        {
            "name": "price_currency",
            "selector": "div[class*='Price'] > div:last-child > div:nth-child(1)",
            "match": "first",
            "type": "text",
        },
        {
            "name": "sale_price",
            "selector": "div[class*='Price'] > div:last-child > div:nth-child(2)",
            "match": "first",
            "type": "text",
        },
        {
            "name": "original_price",
            "selector": "div[class*='Price'] > div:last-child > div:nth-child(1)",
            "match": "first",
            "type": "text",
        },

    ]
}

def get_config(load_from_file=False):
    if load_from_file:
        with open("config.json", "r") as f:
            return json.load(f)
            
    return _config

def generate_config():
    with open("config.json", "w") as f:
        json.dump(_config, f, indent=4)


if __name__ == "__main__":
    generate_config()