import os
import json
import sys

def camel_case_conversion(s):
    """Converts a string to CamelCase."""
    words = s.split('_')
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

def gather_keys(data, path=''):
    """Recursively gather all the keys and their paths from the JSON data."""
    keys = []
    for k, v in data.items():
        new_key = f"{path}.{k}" if path else k
        if isinstance(v, dict):
            keys.extend(gather_keys(v, new_key))
        else:
            keys.append(new_key)
    return keys

def generate_swift_enum(keys_structure):
    """Generate Swift enum code based on the JSON keys structure."""
    grouped_keys = {}
    for key in keys_structure:
        top_level_key = key.split('.')[0]
        camel_case_key = camel_case_conversion(top_level_key)
        if camel_case_key not in grouped_keys:
            grouped_keys[camel_case_key] = []
        grouped_keys[camel_case_key].append(key)

    swift_files = {}
    for camel_case_key, keys in grouped_keys.items():
        enum_name = camel_case_key.capitalize()
        swift_code = f"public extension LangKey {{\n    enum {enum_name}: String {{\n"
        for key in keys:
            components = key.split('.')
            if len(components) >= 3:
                case_name = camel_case_conversion(f"{components[1]}_{components[2]}")
            else:
                case_name = camel_case_conversion(components[-1])
            swift_code += f"        case {case_name} = \"{key}\"\n"
        swift_code += "    }\n}"
        swift_files[f"LangKey+{enum_name}.swift"] = swift_code

    return swift_files

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py path_to_json_file")
        sys.exit(1)
    
    json_file_path = sys.argv[1]
    
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    keys_structure = gather_keys(data)
    swift_files = generate_swift_enum(keys_structure)

    # Ensure the "output" directory exists relative to the current directory
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name, content in swift_files.items():
        # Prepend the directory path to the filename
        output_path = os.path.join(output_dir, file_name)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"Generated {len(swift_files)} Swift files in {output_dir}.")
