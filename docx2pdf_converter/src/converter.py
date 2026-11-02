import json
from pathlib import Path


def load_settings(settings_path):
    # Path() is used to point to a specific location on the disk,
    # acts like a pointer to tell python where the file is
    settings_path = Path(settings_path)
    # "with" is used to open the file and close it safely even if an error occurs
    # open the file (Path object) in read mode "r"  
    with settings_path.open("r", encoding="utf-8") as f:
        # parse the content of the file in json (cause it's a json file)
        # returning a python dict
        settings = json.load(f)
    return settings

def main():
    settings = load_settings("config/settings.json")
    # again 
    input_dir = Path(settings["input_dir"])
    output_dir = Path(settings["output_dir"])  

    if not input_dir.exists() or not input_dir.is_dir():
        print(f"Error: The input directory doesn't exist or isn't a directory: {input_dir}")
        return  
    
    output_dir.mkdir(parents=True, exist_ok=True)



if __name__ == "__main__":
    main()


