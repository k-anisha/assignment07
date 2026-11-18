import pandas as pd
from pathlib import Path

VALID_EVENT_TYPES = {
    "click",
    "login",
    "purchase",
    "scroll",
    "view",
}

input_path = Path("data/raw/events.csv")
output_path = Path("data/clean/events.csv")

df = pd.read_csv(input_path)

df = df.dropna()

df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")

df = df.dropna(subset=["duration_seconds"])
df = df[df["duration_seconds"] > 0]

df["duration_seconds"] = df["duration_seconds"].astype(int)

df["timestamp"] = pd.to_datetime(df["timestamp"], format="mixed", errors="coerce")

df = df.dropna(subset=["timestamp"])

df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Cleaned data saved to {output_path}")
print(f"Remaining rows: {len(df)}")
