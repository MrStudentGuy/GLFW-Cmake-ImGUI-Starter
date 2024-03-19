import re

x = input('Window Name: ')

print(f"Generating class with name {x}... \n")

cppFile = open('app/' + x + '.cpp', 'w')
l1 = f'#include "{x}.h"\n'
l2 = '#include <imgui.h>\n \n'
l3 = f"void {x}::Render() \n"
l4 = "{\n"
l5 = "    ImGuiIO& io = ImGui::GetIO(); (void)io;\n\n"
l6 = "    static float f = 0.0f;\n"
l7 = "    static int counter = 0;\n\n"
l8 = f"    ImGui::Begin(\"{x}\");\n"
l9 = "    ImGui::Text(\"This is some useful text.\");\n"
l10 = "    ImGui::End();\n"
l11 = "}\n"

lines = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11]
cppFile.write(''.join(lines))
cppFile.close()

print(f"{x}.cpp created, creating {x}.h... \n")


hFile = open('app/' + x + '.h', 'w')

l1 = f"#ifndef {x.upper()}_H\n"
l2 = f"#define {x.upper()}_H\n"
l3 = '#include "../UIWindow.h"\n \n'
l4 = '#include "../UIManager.h"\n \n'
l5 = f"class {x} : public UIWindow \n"
l6 = "{\n"
l7 = "public:\n"
l8 = f"    {x}()\n"
l9 = "    {\n"
l10 = "        UIManager::RegisterUIWindow(this);\n"
l11 = "    }\n"
l12 = "    void Render() override;\n"
l13 = "};\n\n"
l14 = "#endif"

lines = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14]
hFile.write(''.join(lines))

print(f"{x}.h created, adding to CMakeLists.txt...")

# Read the contents of the CMakeLists.txt file
with open('CMakeLists.txt', 'r') as f:
    contents = f.read()

# Find the line that defines the APP variable
pattern = r'set\s*\(\s*APP\s*(.*?)\)'
match = re.search(pattern, contents, re.DOTALL)

if match:
    # Extract the existing list of files
    existing_files = match.group(1).strip()

    # Append the new files to the list
    new_files = [f'app/{x}.cpp', f'app/{x}.h']
    new_list = existing_files + ' ' + ' '.join(new_files)

    # Replace the existing APP definition with the new one
    new_contents = re.sub(pattern, f'set( APP {new_list} )', contents, flags=re.DOTALL)

    # Write the modified contents back to the CMakeLists.txt file
    with open('CMakeLists.txt', 'w') as f:
        f.write(new_contents)

    print('CMakeLists.txt updated successfully!')
else:
    print('Error: Could not find the APP variable definition in CMakeLists.txt')

print("All files created successfully! Almost done now, creating instantiation in main.cpp... \n")

# Read the contents of the main.cpp file
with open('main.cpp', 'r') as f:
    lines = f.readlines()

# Find the index where we need to add the include statement
insert_index = 8  # Assuming it should be after line 8
for i, line in enumerate(lines):
    if "int main(void)" in line:
        insert_index = i - 2
        break

# Insert the include statement
lines.insert(insert_index, f'#include "app/{x}.h"\n')

# Find the index where we need to instantiate the class
for i, line in enumerate(lines):
    if "ImVec4 clear_color" in line:
        insert_index = i - 2
        break

# Insert the instantiation
lines.insert(insert_index, f'    {x} {x.lower()}Instance;\n')

# Write the modified contents back to the main.cpp file
with open('main.cpp', 'w') as f:
    f.writelines(lines)

print("main.cpp updated successfully! All actions complete. \n")