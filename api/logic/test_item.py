import csv

def extract_text_from_csv(file_path: str):
    resulting_text = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            resulting_text.append(",".join(row))
    result = "\n".join(resulting_text)
    return result

file = "C:/Users/Jason C/Code/dolphins-backend/api/logic/test.csv"
res = extract_text_from_csv(file)
print(res)