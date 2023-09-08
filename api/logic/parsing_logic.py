import boto3
import PyPDF2
import os
import csv

from dolphins_backend.settings import AWS_ACCESS_KEY, AWS_SECRET_KEY

# BUCKET_NAME = 'pdf-bucket-123'  # Change this to YiPeng's bucket name

# session = boto3.Session(
#     aws_access_key_id=AWS_ACCESS_KEY,
#     aws_secret_access_key=AWS_SECRET_KEY,
#     region_name='us-east-1'
# )

# s3 = session.client('s3')

# def read_files(filenames):

#     data = []

#     for file in filenames:
#         obj = s3.get_object(Bucket=BUCKET_NAME, Key=file)
#         filename = os.path.basename(file)
#         file_path = '/tmp/' + filename
#         with open(file_path, 'wb') as f:
#             f.write(obj['Body'].read())

#         file_ext = file.rsplit(".", 1)[1].lower()

#         parsed_data = parser(file_path, file_ext)
#         data.append(parsed_data)
    
#     return data

# Bypass S3 for a while
def read_files(filenames):
    
    data = []

    for file in filenames:
        file = "./api/logic/" + file
        file_path = os.path.abspath(file)
        file_ext = file.rsplit(".", 1)[1].lower()

        print(file_path)
        parsed_data = parser(file_path, file_ext)
        data.append(parsed_data)
    
    return data

def parser(file_path: str, file_ext: str):
    if not os.path.exists(file_path):
        raise ValueError("File does not exist")

    match file_ext:

        case "pdf":
            return extract_text_from_pdf(file_path)

        case "csv":
            return extract_text_from_csv(file_path)

        case _:
            raise ValueError("File type not supported")


def extract_text_from_pdf(file_path: str):
    resulting_text = ""
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Read each page's text (assuming it's a text-based PDF)
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            page_text = page.extract_text()
            resulting_text += page_text
        
    return resulting_text

def extract_text_from_csv(file_path: str):
    resulting_text = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        resulting_text.append(",".join(header))
        
        for row in csvreader:
            resulting_text.append(",".join(row))
            
    result = "\n".join(resulting_text)
    return result