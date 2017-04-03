# RabobankToYNAB

Converts [Rabobank](https://www.rabobank.nl/) statements to a [YNAB Classic](http://classic.youneedabudget.com) compatible format.

Inspired by [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/chapter14/).

## How to use

1. Export statements as CSV from Rabobank online banking website
2. Place exported file in same directory as `convert.py` script
3. Make sure exported statement is named 'transactions.txt'
4. Run `python convert.py`
5. Converted statements should appear in same directory, named 'transactionsConverted.csv'
6. Import converted statements into YNAB

Happy budgeting!