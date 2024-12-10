import sys

def main():
    if len(sys.argv) != 3:
        print("Введите два числа n и m")
        return
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    array = [i + 1 for i in range(n)]
    result_path = ""
    current_index = 0
    for _ in range(n):
        result_path += str(array[current_index])
        current_index = (current_index + m - 1) % n

    print("Полученный путь:", result_path)
if __name__ == "__main__":
    main()
