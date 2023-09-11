import csv
import os

budget_data = os.path.join( "Resources", "budget_data.csv")
months= []
net_amount=[]
change_list=[]
month_count=0
budget=[0]




with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print (csvreader)
    csv_header = next(csvreader)
  

    for row in csvreader:
        months.append(row[0])
        net_amount.append(int(row[1]))
        if month_count >0:
            change= int(row[1])-previous_amount
            change_list.append(change)
    
        month_count+=1
        previous_amount=int(row[1])
        
    
    greatest_increase1 = max(change_list)
    #print(greatest_increase1)
    greatest_increase_Pos = change_list.index(greatest_increase1)+1
    #print(greatest_increase_Pos)

    greatest_decrease2 = min(change_list)
    greatest_decrease_Pos = change_list.index(greatest_decrease2)+1

    #print(len(months))
    #print(sum(net_amount))
avg_change=round(sum(change_list)/len(change_list),2)

    #print(avg_change)
#print(greatest_decrease_Pos)
    


output_text= (
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {len(months)}\n"
f"Total: ${sum(net_amount)}\n"
f"Average Change: ${avg_change}\n"
f"Greatest Increase in Profits:{months[greatest_increase_Pos]} (${greatest_increase1})\n"
f"Greatest Decrease in Profits: {months[greatest_decrease_Pos]}(${greatest_decrease2})"

)
print(output_text)

output_path = os.path.join("Analysis", "budget_analysis.txt")
with open(output_path,"w") as txtfile:
    txtfile.write(output_text)
