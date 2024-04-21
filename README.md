ensure pip installed: 
```shell
pip -V
```

install pip if required:
```shell
sudo apt instal python3-pip
```

install project dependencies:
```shell
pip3 install cloudscraper beautifulsoup4 transliterate lxml datetime
```

to change target city you should modify main.py

run:
```shell
python3 main.py
```

after parser is done, install zip utility:
```shell
sudo apt install zip
```

and archive CSVs:
```shell
zip -r archive.zip . -x "cianparser*" -x "*.git*" -x "*.py" -x "*.md"
```

you can download archive from remote machine with:
```shell
spc user@remote-ip:/path/to/cian_parser/archive.zip Local/Folder/
```