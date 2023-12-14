def prepare_data(data):
    prepare_data = sorted(data)
    prepare_data1 = prepare_data.pop(0)
    prepare_data2 = prepare_data.reverse()
    prepare_data3 = prepare_data.pop(0)
    new_prepare_data = sorted(prepare_data)
    return new_prepare_data
# print(new_prepare_data)
# print(prepare_data3)
# print(prepare_data2)
# print(prepare_data1)
# print(prepare_data)