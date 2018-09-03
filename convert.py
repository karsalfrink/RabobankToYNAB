import csv, time

transactions = open('transactions.csv')
reader = csv.reader(transactions)

transactionsConverted = open('transactionsConverted.csv', 'w')
writer = csv.writer(transactionsConverted)

# Write header row
writer.writerow(['Date','Payee','Category','Memo','Outflow','Inflow'])

reader.next()

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
    outflow = amount
    inflow = '0'
  elif amount > 0:
    outflow = '0'
    inflow = amount

  writer.writerow([date, payee, category, memo, outflow, inflow])

transactionsConverted.close()