import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#creation of dataframe

students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Sai varshith", "Varshitha", "Kerrthi", "Akshara", "Maheen"],
    "Math": [80, 90, np.nan, 60, 95],
    "Science": [60, 95, 60, np.nan, 92],
    "English": [85, 99, 50, 65, np.nan],
    "Attendance": [55, 86, 70, 35, 56]
})

print("\n📌 Original Dataset:\n", students)

# #finding null values values
# print(students.isna())

# #filling null values
null_values=students.fillna(students.mean(numeric_only=True),inplace=True)
# print(null_values)


#Calculate total marks
students["Total marks"]=students["Math"]+students["Science"]+students["English"]
# print(students)

#Calculate average marks
students["Average marks"]=students["Total marks"]/3
# print(students)

# setting grades as per their marks
students["Grades"]=np.where(students["Total marks"]>250,"A+",students["Total marks"])
# print(students)

#finding toppers 
students["Topper students"]=np.where(students["Total marks"]>250,students["Name"],"None")
# print(students)

#finding weak students
students["Weak students"]=np.where(students["Total marks"]<250,students["Name"],"None")
# print(students)

#pass / fail detection
students["Pass"]=np.where((students[["Math","Science","English"]]<50).any(axis=1),"Fail","Pass")
# print(students)

#Attendece eligibility
students["Attendence Eligibility"]=np.where(students["Attendance"]<75,"Condonation","Eligible")
# print(students)

#Perform subject-wise analysis
print("Highest in each subject:")
print(students[["Math","Science","English"]].max())

print("Lowest in each subject:")
print(students[["Math","Science","English"]].min())

#finding subject wise toppers
Subject_toppers={
    "Math Topper":students.loc[students["Math"].idxmax(),"Name"],
    "English Topper":students.loc[students["English"].idxmax(),"Name"],
    "Science Topper":students.loc[students["Science"].idxmax(),"Name"]
}
print(Subject_toppers)
print("\n📌 Upadted Dataset:\n",students)

#----------------------------------------
#matplotlib
#----------------------------------------
#graph of students vs math marks
sorted_names=students.sort_values("Name")

plt.plot(sorted_names["Name"],sorted_names["Math"],marker="o")

# plt.scatter(sorted_names["Name"],sorted_names["Math"])
plt.grid(True)
plt.title("Math marks of students")
plt.xlabel("students")
plt.ylabel("marks")
plt.show()

# #graph of students vs science marks
# plt.scatter(sorted_names["Name"],sorted_names["Science"])
plt.plot(sorted_names["Name"],sorted_names["Science"],marker="o")
plt.grid(True)
plt.title("science marks of students")
plt.xlabel("students")
plt.ylabel("marks")
plt.show()

# #graph of students vs english marks
# plt.scatter(sorted_names["Name"],sorted_names["English"])
plt.plot(sorted_names["Name"],sorted_names["English"],marker="o")
plt.grid(True)
plt.title("english marks of students")
plt.xlabel("students")
plt.ylabel("marks")
plt.show()

# Bar Chart – Student Average Marks
plt.bar(students["Name"],students["Average marks"])
plt.title("Average marks of students ")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()

#marks distribution using hsitogram
plt.figure()
plt.hist(students["Average marks"])
plt.title("Distribution of marks")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

#Attendance Visualization
plt.bar(students["Name"],students["Attendance"])
plt.axhline(75)
plt.title("Attendence Eligibility")
plt.xlabel("Students")
plt.ylabel("Attendence")
plt.show()

pass_students=students["Pass"].value_counts()

plt.figure()
plt.bar(pass_students.index,pass_students.values)
plt.xlabel("Students")
plt.ylabel("Pass/Fail")
plt.tight_layout()
plt.show() 

#Pie Chart – Grade Distribution
grade_distribution=students["Grades"].apply(lambda x:"A+" if x=="A+" else "Others").value_counts()
plt.pie(grade_distribution.values,labels=grade_distribution.index,autopct='%1.1f%%')
plt.title("Grade distribution")
plt.show() 