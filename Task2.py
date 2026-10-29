import pandas as pd
df=pd.read_csv("clean_data.csv")

print("\nSummary Statistics")

print(df[["salary","experience_years","performance_rating"]].agg(["mean", "median", "min", "max", "std"]))


print("\nDepartment Analysis")

print(df.groupby("department")["salary"].agg(["mean", "median", "min", "max", "count"]))
print("\nCorrelation Analysis")

correlation = df[
    ["salary", "experience_years", "performance_rating"]
].corr()

print(correlation)

print("\nTop 3 Correlation Relationships")

correlation = df[
    ["salary", "experience_years", "performance_rating"]
].corr()

print(correlation)
print("Salary and Experience:")
print(correlation.loc["salary", "experience_years"])

print("Salary and Performance:")
print(correlation.loc["salary", "performance_rating"])

print("Experience and Performance:")
print(correlation.loc["experience_years", "performance_rating"])

print("\nAverage Salary by Department")

print(
    df.groupby("department")["salary"].mean().sort_values(
        ascending=False
    )
)
budget = pd.DataFrame({
    "department": [
        "It", "Hr", "Sales", "Finance",
        "Operations", "Marketing", "Support"
    ],
    "budget": [
        5000000, 2000000, 3000000, 4000000,
        2500000, 2200000, 1800000
    ]
})

merged_df = pd.merge(df, budget, on="department")

print(merged_df[["department", "salary", "budget"]].head())
