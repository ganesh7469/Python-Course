
'''Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''


user_input = input("Enter some text to write to the file: ")

with open('output.txt', 'w') as file:
    file.write(user_input)

additional_input = input("Enter additional text to append to the file: ")

print("additional text appended successfully.")

with open('output.txt', 'a') as file:
    file.write("\n" + additional_input)

with open('output.txt', 'r') as file:
    final_content = file.read()

print("Final content of the file output.txt:")
print(final_content)