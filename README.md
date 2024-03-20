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

Simply upload the pdf and it will output the CSV. 

When importing the CSV to a credit card account, first select the credit account. Map the `Account` column to `Transfer Account`, `Amount` to  `Amount (negated)`.

GPT infers the transaction type and save it to the `Account` column.
```
For each transaction, infer the transaction type from its description:
If related to salary,  Account is "Income:Salary:CAD";
If related to dining,  Account is "Expenses:Dining";
If related to groceries,  Account is "Expenses:Groceries";
If related to uber, lyft, flight ticket or other transportation, Account is "Expenses:Entertainment:Travel";
If related to hobbies (muay thai, martial arts, skiing), Account is "Expenses:Hobbies";
If related to any subscription service,  Account is "Expenses:Subscriptions";
If related to parking, Account is "Expenses:Auto:Parking";
If related to gas or fuel, Account is "Expenses:Auto:Fuel";
For all the other expenses, Account is "Expenses:Adjustment"

```