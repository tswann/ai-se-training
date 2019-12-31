
def run():
    TAXI_DATA = './data/yellow_tripdata_2019-01.csv'
    results = using_lists(TAXI_DATA)
    #results = using_generators(TAXI_DATA)
    row_count = 0

    for row in results:
        row_count += 1

    print(f"Row count is {row_count}")

@profile
def using_lists(file_name):
    with open(file_name) as file:
        result = file.read().split("\n")
    return result

@profile
def using_generators(file_name):
    for row in open(file_name, "r"):
        yield row


if __name__ == '__main__':
    run()