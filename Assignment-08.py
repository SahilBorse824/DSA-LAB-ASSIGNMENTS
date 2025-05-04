
// Problem Statement: Implement shell sort algorithm in JAVA demonstrating 
// shell data structure with modularity of programming language.


PROGRAM >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

  
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    # Start with a large gap, then reduce the gap
    while gap > 0:
        # Perform gapped insertion sort
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

def display_array(arr):
    print(" ".join(map(str, arr)))

def main():
    # Taking user input
    n = int(input("Enter number of elements: "))
    arr = []

    print("Enter elements of the array:")
    for _ in range(n):
        arr.append(int(input()))

    print("\nOriginal Array:")
    display_array(arr)

    # Sorting the array using Shell Sort
    shell_sort(arr)

    print("\nSorted Array using Shell Sort:")
    display_array(arr)

if __name__ == "__main__":
    main()

END OF CODE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  
