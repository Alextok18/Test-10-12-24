def calculate_minimum_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = 0
    for num in nums:
        moves += abs(num - median)
    return moves

def main():
    filename = "input.txt"

    try:
        with open(filename, 'r') as file:
            nums = [int(line.strip()) for line in file]
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return

    result = calculate_minimum_moves(nums)
    print(result)


if __name__ == "__main__":
    main()
