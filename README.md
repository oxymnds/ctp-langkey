# CTP-Langkey

The automation workflow localization file for CTP-iOS

## How to use

1. clone this repository
2. go to the directory and run this command
```bash
pip install -r requirements.txt
```
3. download Localization data from Google Sheets by run this command
```bash
python download.py
```
4. generate Localization JSON by run this command
```bash
python generate.py
```
5. generate Swift Enum files by run this command
```bash
python generate_swift_from_json.py output/en.json
```
6. copy the generated files in `/output` to your Xcode's project
