import pandas as pd
df = pd.read_csv("employees_messy.csv")
before_rows = len(df)
before_missing = df.isnull().sum().sum()
before_duplicates = df.duplicated().sum()


df = df.drop_duplicates()

for col in ["name", "department", "city", "gender", "contract_type"]:
    df[col] = df[col].str.strip().str.title()

df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["experience_years"] = pd.to_numeric(
    df["experience_years"], errors="coerce"
)
df["performance_rating"] = pd.to_numeric(
    df["performance_rating"], errors="coerce"
)
df["joining_date"] = pd.to_datetime(
    df["joining_date"], dayfirst=True, errors="coerce"
)

for col in ["salary", "experience_years", "performance_rating"]:
    df[col] = df[col].fillna(df[col].median())

for col in ["name", "department", "city", "gender", "contract_type"]:
    df[col] = df[col].fillna(df[col].mode()[0])

df["joining_date"] = df["joining_date"].fillna(
    df["joining_date"].mode()[0]
)

q1 = df["salary"].quantile(0.25)
q3 = df["salary"].quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr


df["salary"] = df["salary"].clip(lower, upper)

df.to_csv("clean_data.csv", index=False)

print(
    f"Rows {before_rows} -> {len(df)} | "
    f"Missing values {before_missing} -> {df.isnull().sum().sum()} | "
    f"Duplicates {before_duplicates} -> {df.duplicated().sum()}"
)
