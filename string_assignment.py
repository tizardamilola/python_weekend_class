text = "python programming"
first_char = text[0]
fifth_char = text[4]
last_char = text[-1]
print("First character:", first_char)
print("Fifth character:", fifth_char)
print("Last character:", last_char)

words = "computer"
for letter in words:
    print(f"original: {letter}, uppercase: {letter.upper()}")

sentence = "learning python is fun"
lenght = len(sentence)
has_python = "python" in sentence
print("Length of the sentence:", lenght)
print("Does the sentence contain 'python'?", has_python)

phone = "+2348179776605"
country_code = phone[:4]
first_four_digit = phone[4:8]
local_format = '0' + phone[4:]
print(f"country code: {country_code}")
print(f"first four digit: {first_four_digit}")
print(f"local format: {local_format}")

text = "Artificial Intelligence"
reversed_text = text[::-1]
print(f"Origina_text: {text}")
print(f"Reversed_text: {reversed_text}")

name = "Temi Benson"
upper_case_name = name.upper()
lower_case_name = name.lower()
e_count = name.lower().count('e')
print(upper_case_name)
print(lower_case_name)
print(e_count)

languages = "python, javascript, C++, java"
lang_list = languages.split(',')
result = '|'.join(lang_list)
print(result)

files = ["report.docx", "slides.pptx", "data.pdf", "notes.txt", "presentation.pptx"]
documents = []
presentation = []
for file in files:
    if file.endswith(('.docx', '.pdf', '.txt')):
        documents.append(file)
    elif file.endswith(('.pptx')):
        presentation.append(file)
print("documents:", documents)
print("presentations:", presentation)

rice_price = 4500
beans_price = 1200
def total_price(rice, beans):
    return rice + beans
print(rice_price)
print(beans_price)
print(total_price(rice_price, beans_price))

height = 1.987654321
print(f"Height: {height:.2f}")

