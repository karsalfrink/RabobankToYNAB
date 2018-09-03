import csv, time

transactions = open('transactions.csv')
reader = csv.reader(transactions)

transactionsConverted = open('transactionsConverted.csv', 'w')
writer = csv.writer(transactionsConverted)

# Write header row
writer.writerow(['Date','Payee','Category','Memo','Outflow','Inflow'])

reader.next()
for row in reader:
	date = time.strftime('%d/%m/%Y', time.strptime(row[2], '%Y%m%d')) # DD/MM/YYYY
	payee = row[6]
	category = ''
	memo = row[10]

	# Check if the transaction is Debit (outflow) or Credit (inflow)
	if row[3] == 'D':
		outflow = row[4]
		inflow = '0'
	elif row[3] == 'C':
		outflow = '0'
		inflow = row[4]

	writer.writerow([date, payee, category, memo, outflow, inflow])

transactionsConverted.close()