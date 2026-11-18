import pandas as pd
from pathlib import Path

input_path = Path("data/transformed/events.csv")
output_path = Path("data/features/events.csv")

df = pd.read_csv(input_path)

df["duration_minutes"] = df["duration_seconds"] / 60

df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Features saved to {output_path}")
print(f"Rows: {len(df)}")
