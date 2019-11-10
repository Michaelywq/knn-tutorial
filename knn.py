import math

# find distance between data:
def euclidean_distance(row_1, row_2):
    distance = []
    for i in range(len(row_1) - 1):
        d = (row_2[i] - row_1[i])**2
        distance.append(d)
    return math.sqrt(sum(distance))

# find the nearest neighbors around the test_row
def get_neighbors(dataset, test_row, num_neighbors):
    sorted_dataset = sorted(dataset, key = lambda x: euclidean_distance(test_row, x))
    return sorted_dataset[0: num_neighbors]

# make prediction
def get_prediction(dataset, test_row, num_neighbors):
    sorted_dataset = get_neighbors(dataset, test_row, num_neighbors)
    output_value = [i[-1] for i in sorted_dataset]
    classification = max(output_value, key = lambda x: output_value.count(x))
    probability = str(output_value.count(classification) / len(output_value) * 100) + "%"
    return (classification, probability)
