def std_data(roll_no,std_name, stdt_class, file="student_data.txt"):
    try:
        f=open("f.txt","a+t")
        data= [f"Roll Number: {roll_no}\n", f"Name: {std_name}\n", f"Class: {stdt_class}\n"]
        data.writelines(std_data)
        with open(file, "r") as f:
             lines=f.readlines()
             for lines in lines:
                  print(lines.strip())
    except FileNotFoundError:
        print(f"Error:file '{f}' not found.")    
    finally:
        print("finally block executed")
print("successfully executed")