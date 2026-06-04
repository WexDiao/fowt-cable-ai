"""Wind SCADA EDA — Cells 1-11 of the AI mini-project pipeline.

Usage (from anywhere):
    python notebooks/01_wind_data_eda.py

Reads:    data/T1.csv  (Kaggle SCADA dataset; gitignored)
Writes:   figures/eda_wind_scada/*.png  (8 PNGs: 4 summary + 4 annotated single)
Fallback: if data/T1.csv is missing, runs on synthetic data so the script
          always renders something — useful for CI and offline checks.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

HERE = Path(__file__).resolve().parent              # notebooks/
ROOT = HERE.parent                                  # repo root
DATA_PATH = ROOT / "data" / "T1.csv"
OUT_DIR = ROOT / "figures" / "eda_wind_scada"
OUT_DIR.mkdir(parents=True, exist_ok=True)
USE_SYNTHETIC = not DATA_PATH.exists()


# ---------------- Cell 1: load ----------------
if USE_SYNTHETIC:
    print(f"[!] {DATA_PATH} not found — generating synthetic data.")
    rng = np.random.default_rng(42)
    ts = pd.date_range("2018-01-01", "2018-12-31 23:50", freq="10min")
    n = len(ts)
    wind = np.clip(
        6 + 3 * np.sin(np.arange(n) * 2 * np.pi / (24 * 6))
        + 2 * np.sin(np.arange(n) * 2 * np.pi / (24 * 6 * 30))
        + rng.normal(0, 1.5, n),
        0, 25,
    )
    # Power curve (cut-in 3, rated 12, cut-out 25)
    rated = 3600.0
    power_theo = np.where(
        wind < 3, 0,
        np.where(wind < 12, rated * ((wind - 3) / 9) ** 3,
        np.where(wind < 25, rated, 0)),
    )
    power = np.clip(power_theo + rng.normal(0, 100, n) - 80 * (wind > 13), 0, rated + 200)
    wind_dir = (180 + 60 * np.sin(np.arange(n) * 2 * np.pi / (24 * 6 * 7))
                + rng.normal(0, 20, n)) % 360
    df = pd.DataFrame({
        "timestamp": ts,
        "power_kW": power,
        "wind_speed": wind,
        "power_theoretical": power_theo,
        "wind_dir": wind_dir,
    }).set_index("timestamp")
else:
    df = pd.read_csv(DATA_PATH)
    df.columns = ["timestamp", "power_kW", "wind_speed",
                  "power_theoretical", "wind_dir"]
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="%d %m %Y %H:%M")
    df = df.set_index("timestamp").sort_index()

print(f"Shape: {df.shape}")
print(f"Time range: {df.index.min()} -> {df.index.max()}")
print(df.head())


# ---------------- Cell 2: quality ----------------
print("\n=== dtypes ===")
print(df.dtypes)
print("\n=== missing values ===")
print(df.isna().sum())
print("\n=== describe ===")
print(df.describe().round(2))


# ---------------- Cell 3: daily time series ----------------
daily = df.resample("1D").mean()
fig, axes = plt.subplots(2, 1, figsize=(14, 7), sharex=True)
axes[0].plot(daily.index, daily["wind_speed"], color="steelblue")
axes[0].set_ylabel("Wind speed [m/s]")
axes[0].set_title("Daily mean — wind speed")
axes[1].plot(daily.index, daily["power_kW"], color="darkorange")
axes[1].set_ylabel("Power [kW]")
axes[1].set_title("Daily mean — active power")
axes[1].set_xlabel("Date")
plt.tight_layout()
out1 = OUT_DIR / "01_daily_timeseries.png"
plt.savefig(out1, dpi=150, bbox_inches="tight")
print(f"Saved {out1.name}")
plt.close()


# ---------------- Cell 4: rolling mean ----------------
hourly = df.resample("1h").mean()
hourly["wind_speed_smooth"] = (
    hourly["wind_speed"].rolling(window=24, center=True).mean()
)
fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(hourly.index, hourly["wind_speed"], alpha=0.3, label="hourly")
ax.plot(hourly.index, hourly["wind_speed_smooth"],
        color="red", lw=1.2, label="24h rolling mean")
ax.set_ylabel("Wind speed [m/s]")
ax.legend()
ax.set_title("Wind speed with 24h trend")
plt.tight_layout()
out2 = OUT_DIR / "02_rolling_mean.png"
plt.savefig(out2, dpi=150, bbox_inches="tight")
print(f"Saved {out2.name}")
plt.close()


# ---------------- Cell 5: corr + power curve ----------------
corr = df[["wind_speed", "power_kW", "power_theoretical", "wind_dir"]].corr()
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, ax=axes[0])
axes[0].set_title("Correlation matrix")
axes[1].scatter(df["wind_speed"], df["power_kW"], s=2, alpha=0.3,
                label="measured")
sorted_df = df.sort_values("wind_speed")
axes[1].plot(sorted_df["wind_speed"], sorted_df["power_theoretical"],
             color="red", lw=1, label="theoretical")
axes[1].set_xlabel("Wind speed [m/s]")
axes[1].set_ylabel("Power [kW]")
axes[1].set_title("Power curve: measured vs theoretical")
axes[1].legend()
plt.tight_layout()
out3 = OUT_DIR / "03_corr_and_powercurve.png"
plt.savefig(out3, dpi=150, bbox_inches="tight")
print(f"Saved {out3.name}")
plt.close()


# ---------------- Cell 6: 2x2 summary figure for PPT ----------------
fig, axes = plt.subplots(2, 2, figsize=(14, 8))

axes[0, 0].plot(daily.index, daily["wind_speed"], color="steelblue", lw=0.8)
axes[0, 0].set_title("Daily mean wind speed")
axes[0, 0].set_ylabel("m/s")

axes[0, 1].plot(hourly.index, hourly["wind_speed"], alpha=0.3, lw=0.5)
axes[0, 1].plot(hourly.index, hourly["wind_speed_smooth"],
                color="red", lw=1)
axes[0, 1].set_title("Hourly wind speed + 24h rolling")
axes[0, 1].set_ylabel("m/s")

sns.heatmap(corr, annot=True, cmap="coolwarm", center=0,
            ax=axes[1, 0], cbar=False, fmt=".2f")
axes[1, 0].set_title("Correlation matrix")

axes[1, 1].scatter(df["wind_speed"], df["power_kW"],
                   s=1, alpha=0.2, color="steelblue", label="measured")
axes[1, 1].plot(sorted_df["wind_speed"], sorted_df["power_theoretical"],
                color="red", lw=1.2, label="theoretical")
axes[1, 1].set_xlabel("Wind speed [m/s]")
axes[1, 1].set_ylabel("Power [kW]")
axes[1, 1].set_title("Power curve")
axes[1, 1].legend(fontsize=9)

plt.tight_layout()
out4 = OUT_DIR / "04_summary_2x2.png"
plt.savefig(out4, dpi=150, bbox_inches="tight")
print(f"Saved {out4.name}")
plt.close()


# ---------------- Cell 7: key insights ----------------
mean_ws = df["wind_speed"].mean()
mean_pw = df["power_kW"].mean()
corr_ws_pw = df["wind_speed"].corr(df["power_kW"])
missing_pct = df.isna().sum().sum() / df.size * 100

print("\n=== Key Insights ===")
print(f"Mean wind speed: {mean_ws:.2f} m/s")
print(f"Mean active power: {mean_pw:.2f} kW")
print(f"Corr(wind_speed, power_kW): {corr_ws_pw:.3f}")
print(f"Missing fraction: {missing_pct:.2f}%")
print(f"Source: {'synthetic fallback' if USE_SYNTHETIC else 'real Kaggle T1.csv'}")


# ---------------- Cell 8: Plot 1 (annotated) — Daily wind ----------------
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(daily.index, daily["wind_speed"], color="steelblue", lw=1.1)
ax.axhline(mean_ws, color="red", linestyle="--", lw=1.3,
           label=f"Year mean = {mean_ws:.2f} m/s")
try:
    winter = daily.loc["2018-01":"2018-03"]["wind_speed"]
    w_date, w_val = winter.idxmax(), winter.max()
    ax.annotate(f"Winter peak\n≈ {w_val:.1f} m/s",
                xy=(w_date, w_val),
                xytext=(40, 5), textcoords="offset points",
                fontsize=10,
                arrowprops=dict(arrowstyle="->", color="darkred"))
    summer = daily.loc["2018-06":"2018-08"]["wind_speed"]
    s_date, s_val = summer.idxmin(), summer.min()
    ax.annotate(f"Summer trough\n≈ {s_val:.1f} m/s",
                xy=(s_date, s_val),
                xytext=(15, -40), textcoords="offset points",
                fontsize=10,
                arrowprops=dict(arrowstyle="->", color="darkblue"))
except KeyError:
    pass
ax.set_xlabel("Date")
ax.set_ylabel("Wind speed [m/s]")
ax.set_title("Plot 1 · Daily Mean Wind Speed (2018, Turkey)")
ax.legend(loc="upper right", framealpha=0.9)
ax.grid(alpha=0.3)
plt.tight_layout()
out_p1 = OUT_DIR / "plot_1_daily_wind.png"
plt.savefig(out_p1, dpi=150, bbox_inches="tight")
print(f"Saved {out_p1.name}")
plt.close()


# ---------------- Cell 9: Plot 2 (annotated) — 24-h rolling ----------------
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(hourly.index, hourly["wind_speed"], color="lightgray", lw=0.4,
        alpha=0.7, label="Hourly raw")
ax.plot(hourly.index, hourly["wind_speed_smooth"], color="red", lw=1.4,
        label="24-h rolling (center=True)")
mid_idx = len(hourly) // 2
ax.annotate("Diurnal noise removed;\nseasonal trend visible",
            xy=(hourly.index[mid_idx],
                hourly["wind_speed_smooth"].iloc[mid_idx]),
            xytext=(25, 60), textcoords="offset points", fontsize=10,
            arrowprops=dict(arrowstyle="->", color="black"))
ax.set_xlabel("Date")
ax.set_ylabel("Wind speed [m/s]")
ax.set_title("Plot 2 · Wind Speed with 24-h Rolling Mean")
ax.legend(loc="upper right", framealpha=0.9)
ax.grid(alpha=0.3)
plt.tight_layout()
out_p2 = OUT_DIR / "plot_2_rolling.png"
plt.savefig(out_p2, dpi=150, bbox_inches="tight")
print(f"Saved {out_p2.name}")
plt.close()


# ---------------- Cell 10: Plot 3 (annotated) — Correlation heatmap --
from matplotlib.patches import Rectangle
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, fmt=".2f",
            cbar=True, square=True, ax=ax,
            annot_kws={"size": 13, "weight": "bold"})
ax.set_title("Plot 3 · Correlation Matrix (Pearson)")
cols = list(corr.columns)
try:
    i_ws = cols.index("wind_speed")
    i_p = cols.index("power_kW")
    for (xp, yp) in [(i_p, i_ws), (i_ws, i_p)]:
        ax.add_patch(Rectangle((xp, yp), 1, 1, fill=False,
                                edgecolor="black", lw=2.5))
except ValueError:
    pass
plt.tight_layout()
out_p3 = OUT_DIR / "plot_3_corr.png"
plt.savefig(out_p3, dpi=150, bbox_inches="tight")
print(f"Saved {out_p3.name}")
plt.close()


# ---------------- Cell 11: Plot 4 (annotated) — Power curve -----------
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df["wind_speed"], df["power_kW"], s=2, alpha=0.2,
           color="steelblue", label="Measured (all 10-min samples)")
ax.plot(sorted_df["wind_speed"], sorted_df["power_theoretical"],
        color="red", lw=2, label="Theoretical curve")
rated = df["power_theoretical"].max()
ax.axvline(3, color="green", linestyle=":", lw=1.2, alpha=0.7)
ax.text(3.2, rated * 0.95, "cut-in ≈ 3 m/s",
        fontsize=10, color="green", va="top")
ax.axhline(rated, color="orange", linestyle="--", lw=1.2, alpha=0.7)
ax.text(0.5, rated + 50, f"rated ≈ {rated:.0f} kW",
        fontsize=10, color="darkorange")
ax.axvspan(12, 25, alpha=0.08, color="red")
ax.annotate("Losses zone\n(below theoretical)",
            xy=(17, rated * 0.4),
            xytext=(0, 0), textcoords="offset points",
            fontsize=11, ha="center", color="darkred",
            bbox=dict(boxstyle="round", facecolor="white",
                      edgecolor="darkred"))
ax.set_xlabel("Wind speed [m/s]")
ax.set_ylabel("Active power [kW]")
ax.set_title("Plot 4 · Power Curve — Measured vs Theoretical")
ax.legend(loc="lower right")
ax.grid(alpha=0.3)
plt.tight_layout()
out_p4 = OUT_DIR / "plot_4_power_curve.png"
plt.savefig(out_p4, dpi=150, bbox_inches="tight")
print(f"Saved {out_p4.name}")
plt.close()
