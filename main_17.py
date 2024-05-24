#!/usr/bin/python3
import inspect
import io
import sys
import cmd
import shutil
import os

"""
 Backup console file
"""
if os.path.exists("tmp_console_main.py"):
    shutil.copy("tmp_console_main.py", "console.py")
shutil.copy("console.py", "tmp_console_main.py")


"""
 Updating console to remove "__main__"
"""
with open("tmp_console_main.py", "r") as file_i:
    console_lines = file_i.readlines()
    with open("console.py", "w") as file_o:
        in_main = False
        for line in console_lines:
            if "__main__" in line:
                in_main = True
            elif in_main:
                if "cmdloop" not in line:
                    file_o.write(line.lstrip("    "))
            else:
                file_o.write(line)

import console


"""
 Create console
"""
console_obj = "HBNBCommand"
for name, obj in inspect.getmembers(console):
    if inspect.isclass(obj) and issubclass(obj, cmd.Cmd):
        console_obj = obj

my_console = console_obj(stdout=io.StringIO(), stdin=io.StringIO())
my_console.use_rawinput = False


"""
 Exec command
"""
def exec_command(my_console, the_command, last_lines = 1):
    my_console.stdout = io.StringIO()
    real_stdout = sys.stdout
    sys.stdout = my_console.stdout
    my_console.onecmd(the_command)
    sys.stdout = real_stdout
    lines = my_console.stdout.getvalue().split("\n")
    return "\n".join(lines[(-1*(last_lines+1)):-1])


"""
 Tests
"""
result = exec_command(my_console, "all City", 8)
if result is None or result == "":
    print("FAIL: No cities retrieved")
if "my_id_c_0" not in result or "my_id_c" not in result or "San Francisco" not in result:
    print("FAIL: Missing information c0")
if "my_id_c_1" not in result or "my_id_c" not in result or "San Jose" not in result:
    print("FAIL: Missing information c1")
if "my_id_c_2" not in result or "my_id_c" not in result or "Los Angeles" not in result:
    print("FAIL: Missing information c2")
if "my_id_c_3" not in result or "my_id_c" not in result or "Fremont" not in result:
    print("FAIL: Missing information c3")
if "my_id_c_4" not in result or "my_id_c" not in result or "Palo Alto" not in result:
    print("FAIL: Missing information c4")
if "my_id_c_5" not in result or "my_id_c" not in result or "Oakland" not in result:
    print("FAIL: Missing information c5")
if "my_id_a_0" not in result or "my_id_a" not in result or "Page" not in result:
    print("FAIL: Missing information a0")
if "my_id_a_1" not in result or "my_id_a" not in result or "Phoenix" not in result:
    print("FAIL: Missing information a1")

print("OK", end="")

shutil.copy("tmp_console_main.py", "console.py")
