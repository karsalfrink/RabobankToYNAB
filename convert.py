import csv, time

transactions = open('transactions.csv')
reader = csv.reader(transactions)

transactionsConverted = open('transactionsConverted.csv', 'w')
writer = csv.writer(transactionsConverted)

# Write header row
writer.writerow(['Date','Payee','Category','Memo','Outflow','Inflow'])

reader.next()
for row in reader:
	category = ''

	# Check if the transaction is Debit (outflow) or Credit (inflow)
	if row[3] == 'D':
		outflow = row[4]
		inflow = '0'
	elif row[3] == 'C':
		outflow = '0'
		inflow = row[4]

	writer.writerow([date, payee, category, memo, outflow, inflow])
  date = time.strftime('%d/%m/%Y', time.strptime(row[4], '%Y-%m-%d')) # DD/MM/YYYY
  payee = row[9]
  memo = row[19]

transactionsConverted.close()