from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby.name)
print(python)
print(visual_basic)
print(python.name)


program_list = [ruby, python, visual_basic]
print("The dynamically typed languages are: ")
for programs in program_list:
    if programs.is_dynamic():
        print(programs.name)
