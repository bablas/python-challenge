import os
import csv

date = []
profloss = []


#Step 1 input and output files
input_file = "budget_data.csv"
output_file = "budget_data_analysis.txt"
csv_input= os.path.join(input_file)
txt_output = os.path.join(output_file)

#Step 2 Open Input File
with open(csv_input, mode='r', newline='') as budget_data:
    reader = csv.reader(budget_data, delimiter=',')

    next(reader)

    totalmonths = 0
    totalprofloss = 0
    for row in reader:
        date.append(row[0])
        profloss.append(row[1])
        totalmonths = totalmonths + 1
        totalprofloss = totalprofloss + int(row[1])

#Step 3 Print Summary header
print()
print(f"Financial Analysis")
print(f"-"*50)

#Step 4 Total Months
print(f"Total Months: {totalmonths}")

#Step 5 Total Profit and Loss
print(f"Total Profit/Loss: {totalprofloss}")

#Step 6 Total Average Change 
averagechange = round(totalprofloss/totalmonths, 2)
print(f"Average Change: {averagechange}")

#Step 7 Greatest Increase in Profits
highestprofit = 0
for i in range(len(profloss)):
    if int(profloss[i]) - int(profloss[i - 1]) > highestprofit:
        highestprofit = int(profloss[i]) - int(profloss[i - 1])
        highestdate = date[i]
print(f"Greatest Increase in Profits: {highestdate} ${highestprofit}")

#Step 8 Greatest Decrease in Profits
lowestprofit = 0
for k in range(len(profloss)):
    if int(profloss[k]) - int(profloss[k - 1]) < lowestprofit:
        lowestprofit = int(profloss[k]) - int(profloss[k - 1])
        lowestdate = date[k]
print(f"Greatest Decrease in Profits: {lowestdate} ${lowestprofit}")
print()
print()


#Step 9 Write to File
with open(txt_output, mode='w', newline='') as summary_txt:
    writer = csv.writer(summary_txt)

    writer.writerows([
        [f"Financial Analysis"],
        [f"-"*50],
        [f"Total Months: {totalmonths}"],
        [f"Total Profit/Loss: {totalprofloss}"],
        [f"Average Change: {averagechange}"],
        [f"Greatest Increase in Profits: {highestdate} ${highestprofit}"],
        [f"Greatest Decrease in Profits: {lowestdate} ${lowestprofit}"]
    ])
