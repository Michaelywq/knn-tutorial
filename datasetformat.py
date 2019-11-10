def str_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column])
    return dataset

def output_to_dict(dataset, column):
    output_dict = dict()
    output_set = set([row[column] for row in dataset])
    for num, output in enumerate(output_set):
        output_dict[output] = num
    return output_dict


# make output from string to int (0,1,2,3....)
def output_to_int(dataset, column):
    output_dict = output_to_dict(dataset, column)
    for each in dataset:
        if each[column] in output_dict:
            each[column] = output_dict[each[column]]
    return dataset



if __name__ == "__main__":
    import loadcsv, resampling
    filename = "iris.csv"
    dataset = loadcsv.load_csv(filename)

# reformat data
    for i in range(0, 3):
        dataset = str_to_float(dataset, i)

    dataset = output_to_int(dataset, 3)
    print(dataset)
