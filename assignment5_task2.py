

'''Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''

numbers = list(range(1, 11))
extracted = numbers[:5]
reversed_extracted = extracted[::-1]

print("\nOriginal list:", numbers)
print("\nExtracted list:", extracted)
print("\nReversed list:", reversed_extracted)