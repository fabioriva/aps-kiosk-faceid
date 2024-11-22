import csv

# Define the CSV file name
csv_file = "directory_structure.csv"

# Open the CSV file in read mode
with open(csv_file, 'r') as file:
    reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in reader:
        print(row)
        # for r in row:
        #     print(r)


# static void read_csv(const string& filename, vector<Mat>& images, vector<int>& labels, char separator = ';') {
#     std::ifstream file(filename.c_str(), ifstream::in);
#     if (!file) {
#         string error_message = "No valid input file was given, please check the given filename.";
#         CV_Error(Error::StsBadArg, error_message);
#     }
#     string line, path, classlabel;
#     while (getline(file, line)) {
#         stringstream liness(line);
#         getline(liness, path, separator);
#         getline(liness, classlabel);
#         if(!path.empty() && !classlabel.empty()) {
#             images.push_back(imread(path, 0));
#             labels.push_back(atoi(classlabel.c_str()));
#         }
#     }
# }
