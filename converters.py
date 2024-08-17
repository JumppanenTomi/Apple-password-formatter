import csv

def AppleToUniversal(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['url', 'username', 'password']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()

        for row in reader:
            url = row['URL']
            username = row['Username']
            password = row['Password']
            
            writer.writerow({
                'url': url,
                'username': username,
                'password': password,
            })
    pass

def UniversalToApple(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['Title', 'URL', 'Username', 'Password', 'Notes', 'OTPAuth']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()

        for row in reader:
            title = f"{row['url'].split('//')[1].split('/')[0]} ({row['username']})"
            url = row['url']
            username = row['username']
            password = row['password']
            notes = ''
            otp_auth = ''
            
            writer.writerow({
                'Title': title,
                'URL': url,
                'Username': username,
                'Password': password,
                'Notes': notes,
                'OTPAuth': otp_auth
            })
    pass