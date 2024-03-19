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


## Using Chat GPT UI
If you have Chat AI subscription, it might be more economical to use it's UI. Here is a prompt to generate the CSV file:
```
Given this PDF bank statement, please generate a CSV file format specifically structured for import into GnuCash. Ensure the CSV file includes columns for Date, Description, and Amount. Make sure to include all transactions.
```