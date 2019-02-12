import os
import csv

#Step 1 US state Abbreviations Dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Step 2 Open Input
inputfile = os.path.join("employee_data.csv")

with open(inputfile, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    empid = []
    first=[]
    last=[]
    splitDate=[]
    dob=[]
    ssn=[]
    state=[]
        
    for row in csvreader:

        #Step 3 Assign Employee ID
        empid.append(row[0])
    
        #Step 4 Split First and Last Name
        firstLast = row[1].split(" ")
        first.append(firstLast[0])
        last.append(firstLast[1])
        
        #Step 5 Split Date, Change the Order, then add the /
        splitDate = row[2].split("-")
        splitDate[0], splitDate[1], splitDate[2] = splitDate[1], splitDate[2], splitDate[0]
        USDate = "/".join(splitDate)
        dob.append(USDate)
        
        #Step 6 Mask SSN
        splitSSN = row[3].split("-")
        ssn.append(f"***-**-{splitSSN[2]}")
        
        #Step 7 Look up State Dictionary
        stateAbbr = us_state_abbrev[row[4]]
        state.append(stateAbbr)
    

#Step 8 Zip lists together
formatedoutput = zip(empid,first,last,dob,ssn,state)

#Step 9 Write the Output File
outputfile = os.path.join("Formated_Employee_Data.csv")
with open(outputfile, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    
    writer.writerow(["Emp ID","Fist Name","Last Name", "DOB","SSN","State"])
    writer.writerows(formatedoutput)