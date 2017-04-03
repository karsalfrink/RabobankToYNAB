# RabobankToYNAB
Converts [Rabobank](https://www.rabobank.nl/) statements to a [YNAB](http://www.youneedabudget.com) compatible format.

Inspired by [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/chapter14/).

## How to use

1. Export your statements as CSV from the Rabobank online banking website
2. Place your export in the same directory as the `convert.py` script
3. Make sure the exported statement is named 'transactions.txt'
4. Run `python convert.py`
5. Your converted statements should appear in the same directory, named 'transactionsConverted.csv'
6. Import your converted statements into YNAB, happy budgeting!