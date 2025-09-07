import pandas as pd

# Load dataset
df = pd.read_csv("students.csv",
encoding ="utf-8-sig",sep=",")
# Calculate average score for each student
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# Add Pass/Fail column (threshold = 40%)
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# ---- Analysis ----
print("\n===== Student Grades Analyzer =====")

# 1. Average, highest, lowest per subject
for subject in ["Math", "Science", "English"]:
    print(f"\n📘 {subject}:")
    print(f"   ➡ Average: {df[subject].mean():.2f}")
    print(f"   ➡ Highest: {df[subject].max()}")
    print(f"   ➡ Lowest : {df[subject].min()}")

# 2. Top 3 students by average score
print("\n🏆 Top 3 Students (by Average Score):")
top_students = df.nlargest(3, "Average")[["Name", "Average"]]
print(top_students.to_string(index=False))

# 3. Final DataFrame with Pass/Fail
print("\n📊 Final Result Table:")
print(df.to_string(index=False))