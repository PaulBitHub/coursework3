import json
import func

# Чтение данных из файла OPERATIONS
with open('../operations.json', 'r') as file_operations:
    data = json.load(file_operations)

executed_data = func.find_executed_elements(data)
for ex_operation in executed_data:
    ex_operation['date_int'] = func.date_to_int(ex_operation['date'])

sorted_executed_data = sorted(executed_data, key=lambda x: x['date_int'])
five_last_operations = sorted_executed_data[:-5:-1]
func.display_transaction(five_last_operations)
