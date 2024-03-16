def main():
    numbers = input("Enter numbers separated with spaces:" ).strip().split()
    numbers = [int(nums) for nums in numbers]
    print(numbers)
    print("Total sum: ", sum(numbers))

if __name__ == "__main__":
    main()
