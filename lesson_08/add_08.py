def read_test_data(file_path):
    try:
        file = open(file_path, "r")
        print(f"File was opened: {file_path}")
        data = file.read()
        if not data:
            raise ValueError("Test data is empty")
        print(f"Data from file: {data}")
    except FileNotFoundError:
        print(f"Error in file {file_path}. It should have name...")
    except ValueError:
        print(f"Error in file {file_path}. It should have data...")
    finally:
        print("Closing file")
        try:
            # File was never opened
            file.close()
        except NameError:
            print("File wasn't opened")

example_file_path = "/Users/feshv/hillel_py/aqa_hillel_13_08/lesson8/test_cases.txt"
read_test_data(example_file_path)