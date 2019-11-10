import random


def train_test_split(dataset, split = 0.6):
    train = []
    train_num = round(len(dataset) * split)
    test_num = len(dataset) - train_num
    for num in range(train_num):
        index = random.randrange(len(dataset))
        train.append(dataset.pop(index))
    test = dataset
    return train, test



def cross_validation_split(dataset, fold = 3):
    fold_size = round(len(dataset) / fold)
    dataset_cross_validation = list()
    dataset_split = list()
    for i in range(fold - 1):
        for num in range(fold_size):
            index = random.randrange(len(dataset))
            dataset_split.append(dataset.pop(index))
        dataset_cross_validation.append(dataset_split)
    dataset_cross_validation.append(dataset)
    return dataset_cross_validation



if __name__ == "__main__":
    import loadcsv
    filename = "iris.csv"
    dataset = loadcsv.load_csv(filename)
    random.seed(1)
    train, test = train_test_split(dataset, 0.6)
    print(train)
    print(test)
    print("\n" + "below is cross validation")
    dataset_c_v = cross_validation_split(dataset, 3)
    for i in dataset_c_v:
        print(dataset_c_v)
