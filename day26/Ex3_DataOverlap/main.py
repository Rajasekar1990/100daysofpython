# Write your code above 👆
with open("file1.txt", "r") as file1:
    file1_content = file1.readlines()

with open("file2.txt", "r") as file2:
    file2_content = file2.readlines()

# def update_file(content):
#     final_content = []
#     for item in content:
#         file_content = item.strip("\n")
#         final_content.append(file_content)
#     return final_content

# result = [common for common in update_file(file1_content) if common in update_file(file2_content)]

result = [int(common) for common in file1_content if common in file2_content]
print(result)
