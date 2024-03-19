# bank-statement-converter
Use GPT to convert PDF bank statements to CSV

# Getting Started
```
pip install pymupdf
python convert.py
```

# How to use
Create a config file `config.json` in the root directory: 

```
{
    "api_key": "YOUR-OPENAI-KEY",
    "names": [],
    "addresses": [],
    "accounts": []
}
```
The script will also redact some basic keywords, stored in `keywords.json`.
## Using Open AI API


## Using Custom GPT
If you have Chat AI subscription, it might be more economical to use it's UI. [link](https://chat.openai.com/g/g-K1ajucf7u-gnucash-pdf-converter)

Simply upload the pdf and it will output 