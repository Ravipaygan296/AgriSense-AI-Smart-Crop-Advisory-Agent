import yaml
import os
import json

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

