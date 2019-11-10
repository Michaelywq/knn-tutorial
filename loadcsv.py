# how to read csv by python
from csv import reader

def load_csv(filename):
    dataset = list()
    with open(filename, 'r', encoding='utf-8-sig') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

if __name__ == "__main__":
    filename = "iris.csv"
    dataset = load_csv(filename)
    for i in dataset:
        print(dataset)

