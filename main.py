import re

# Function to extract email addresses using regular expressions
def extract_emails(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
        return emails

# Extracting emails from the HTML file
file_path = '/home/ivan/PycharmProjects/projectRegularForStankin/file.html'
emails = extract_emails(file_path)
print("Extracted Emails:", emails)
z