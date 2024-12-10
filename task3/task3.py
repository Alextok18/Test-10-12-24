import json

def main(values_path, tests_path, report_path):
    with open(values_path, 'r') as file:
        values = json.load(file)

    with open(tests_path, 'r') as file:
        tests = json.load(file)

    def fill_values(test_items):
        for test in test_items:
            if 'id' in test and test['id'] in values:
                test['value'] = values[test['id']]
            if 'values' in test:
                fill_values(test['values'])

    fill_values(tests['tests'])

    with open(report_path, 'w') as file:
        json.dump(tests, file, indent=4)

if __name__ == "__main__":
    main("values.json", "tests.json", "report.json")
