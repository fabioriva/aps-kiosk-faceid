import os
import csv

# Define the directory to walk through
directory = "/home/parkbot/github/aps-kiosk-faceid/data"

# Define the CSV file name
csv_file = "directory_structure.csv"

id = 0
# Open the CSV file in write mode
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    # writer.writerow(["Path", "Type"])  # Write the header row

    # Walk through the directory
    for root, dirs, files in os.walk("data/"):
        print('1')
        print(root)
        print('2')
        print(dirs)
        print('3')
        print(files)
        for name in dirs:
            # writer.writerow([os.path.join(root, name), "Directory"])
            id += 1

        for name in files:
            # writer.writerow([os.path.join(root, name), "File"])
            # writer.writerow([os.path.join(root, name), ])
            writer.writerow(
                [os.path.join(root, name), id, root.split('/')[-1]])

print(f"CSV file '{csv_file}' created successfully!")
