import requests
from bs4 import BeautifulSoup
import csv


def parse_hcpc_code():
    try:
        url = "https://www.hcpcsdata.com/Codes"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the table containing the HCPC codes
        table = soup.find("table", {"id": "ctl00_MainContent_rptCodes_ctl00_dgCodes"})
        if table is None:
            raise ValueError("Table not found on the webpage")

        # Define the header of the CSV file
        header = ["Group", "Category", "Code", "Long Description", "Short Description"]
        
        # Open a CSV file in write mode
        with open("hcpc_codes.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)  # Write the header to the CSV file
            
            # Iterate through each row in the table
            for row in table.find_all("tr")[1:]:
                # Extract data from each cell in the row
                cells = row.find_all("td")
                group = cells[0].text.strip()
                category = cells[1].text.strip()
                code = cells[2].text.strip()
                long_description = cells[3].text.strip()
                short_description = cells[4].text.strip()
                
                # Write the extracted data to the CSV file
                writer.writerow([group, category, code, long_description, short_description])

        print("CSV file created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def generate_serializer_errors(args):
    message = ""
    for key, values in args.items():
        error_message = ""
        for value in values:
            error_message += value + ","
        error_message = error_message[:-1]

        # message += "%s : %s | " %(key,error_message)
        message += f"{key} - {error_message} | "
    return message[:-3]