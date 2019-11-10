import loadcsv, datasetformat, resampling, random
import knn


# import data
filename = "iris.csv"
dataset = loadcsv.load_csv(filename)



# reformat data
for i in range(0, 3):
    dataset = datasetformat.str_to_float(dataset, i)
dataset = datasetformat.output_to_int(dataset, 3)

# cross-validation
dataset_c_v = resampling.cross_validation_split(dataset, 10)

for each in dataset_c_v:
    train, test = resampling.train_test_split(each, 0.9)
    for i in test:
        for j in train:
            prediction = knn.get_prediction(train, i, 5)
            print("test_data: ", i, "prediction: %s, probability: %s" % prediction)

        print("\n")
