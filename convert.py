import csv, time

transactions = open('transactions.csv', encoding = "ISO-8859-1")
reader = csv.reader(transactions)

transactionsConverted = open('transactionsConverted.csv', 'w')
writer = csv.writer(transactionsConverted)

# Write header row
writer.writerow(['Date','Payee','Category','Memo','Outflow','Inflow'])

next(reader)

for row in reader:
  date = time.strftime('%d/%m/%Y', time.strptime(row[4], '%Y-%m-%d')) # DD/MM/YYYY
  payee = row[9]
  category = ''
  memo = row[19]
  amount = row[6]
  amount = amount.replace(',','.')
  amount = float(amount)

  # Check if the transaction is Debit (outflow) or Credit (inflow)
  if amount < 0:
    outflow = -1*amount
    inflow = '0'
  elif amount > 0:
    outflow = '0'
    inflow = amount

  writer.writerow([date, payee, category, memo, outflow, inflow])

transactionsConverted.close()