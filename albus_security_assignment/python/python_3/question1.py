import csv

def rem_dup(csv_read):
    ls=[]
    for i in csv_read:
        if len(i) != 0 and i.lower() not in [j.lower() for j in ls + csv_read[:csv_read.index(i)] + csv_read[csv_read.index(i)+1:]]:
            ls.append(i)
    return ls

def empty_csv(fname):
    with open(fname,'r') as input_file:
        with open('output.csv','w') as output_file:
            for line in input_file:
                fields=line.strip().split(',')
                for i in range(len(fields)):
                    if fields[i]=='':
                        fields[i]='N/A'
                output_file.write(','.join(fields) + '\n')


fname=input("Enter the csv filename:")
with open(fname, newline = '') as csv_file:
    f_read = csv.reader(csv_file, delimiter = ',')
    unique_lines = rem_dup(list(f_read))

print("The content in the csv file after removing the duplicates are:")
for line in unique_lines:
    print(line)

empty_csv(fname)
#output is in output.csv file