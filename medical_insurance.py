medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# replacing # with $
updated_medical_data = medical_data.replace("#", "$")
print(updated_medical_data)

# counting the number of records
num_records = 0
for record in updated_medical_data:
  if record == '$':
    num_records += 1

print('There are', num_records, 'medical records in the data')

# splitting records with the ;
medical_data_split = updated_medical_data.split(";")
#print(medical_data_split)

# creating a list that splits the records
medical_records = []
for record in medical_data_split:
  medical_records.append(record.split(","))
print(medical_records)

# removing whitespace
medical_records_clean = []
for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip(" "))
  medical_records_clean.append(record_clean)

print(medical_records_clean)

# printing each name in medical data
for name in medical_records_clean:
  print(name[0].upper())

names = []
ages = []
bmis = []
insurance_costs = []

for i in medical_records_clean:
  names.append(i[0])
  ages.append(i[1])
  bmis.append(i[2])
  insurance_costs.append(i[3])

print(names)
print(ages)
print(bmis)
print(insurance_costs)

# calculating average bmi
total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)
average_bmi = total_bmi / len(bmis)
print(average_bmi)

total_cost = 0
nums = []
# removin the $ so costs can be converted to numbers
for data in insurance_costs:
  nums.append(data.replace("$", ""))

# calculating the average cost of insurance
for num in nums:
  total_cost += float(num)
average_cost = total_cost / len(nums)
print("This is the average cost", average_cost)

# displaying data of each patient
for data in medical_records_clean:
  print(f"{data[0].split()[0]}, is, {data[1]} years old with a BMI of {data[2]} and an insurance cost of {data[3]}")







