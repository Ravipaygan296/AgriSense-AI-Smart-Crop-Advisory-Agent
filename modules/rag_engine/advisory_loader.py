import os

def load_advisories(folder="data/advisories/"):
    advisories = []
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                advisories.append({"source": file, "content": f.read()})
    return advisories

