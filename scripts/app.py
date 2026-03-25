import json
from pathlib import Path
import pandas as pd
import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="OpenClaw Trajectory Lab",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("OpenClaw Trajectory Intelligence Lab")
st.caption("GlassClaw-style reviewer dashboard for OpenClaw task evaluation")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.header("Filters")

# --------------------------------------------------
# PATHS
# --------------------------------------------------
trajectory_folder = Path("F:/openclaw-trajectory-eval-lab/data/trajectories")
score_file = Path("F:/openclaw-trajectory-eval-lab/evaluation/trajectory_scores.csv")
evidence_file = Path("F:/openclaw-trajectory-eval-lab/data/evidence/evidence_tracker.csv")

# --------------------------------------------------
# LOAD TRAJECTORY JSON FILES
# --------------------------------------------------
files = sorted(trajectory_folder.glob("task_*_trajectory.json"))

rows = []
all_tasks = []

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        all_tasks.append(data)
        rows.append({
            "task_id": int(data["task_id"]),
            "task_title": data["task_title"],
            "difficulty": data["difficulty"],
            "status": data["status"],
            "trajectory_score": float(data["review"]["overall_score"])
        })

df = pd.DataFrame(rows)

# --------------------------------------------------
# LOAD CSV FILES
# --------------------------------------------------
scores_df = pd.read_csv(score_file)
evidence_df = pd.read_csv(evidence_file)

# Clean column names
df.columns = [str(c).strip() for c in df.columns]
scores_df.columns = [str(c).strip() for c in scores_df.columns]
evidence_df.columns = [str(c).strip() for c in evidence_df.columns]

# Convert types
df["task_id"] = df["task_id"].astype(int)
scores_df["task_id"] = scores_df["task_id"].astype(int)
evidence_df["task_id"] = evidence_df["task_id"].astype(int)

# --------------------------------------------------
# BUILD EVIDENCE COUNT
# --------------------------------------------------
evidence_count = evidence_df.groupby("task_id").size().reset_index(name="evidence_count")

# --------------------------------------------------
# BUILD SUMMARY TABLE
# --------------------------------------------------
summary_df = df.merge(
    scores_df[["task_id", "overall_score"]],
    on="task_id",
    how="left"
).merge(
    evidence_count,
    on="task_id",
    how="left"
)

summary_df = summary_df.rename(columns={"overall_score": "review_score"})

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------
difficulty_filter = st.sidebar.multiselect(
    "Select Difficulty",
    options=sorted(summary_df["difficulty"].dropna().unique()),
    default=sorted(summary_df["difficulty"].dropna().unique())
)

status_filter = st.sidebar.multiselect(
    "Select Status",
    options=sorted(summary_df["status"].dropna().unique()),
    default=sorted(summary_df["status"].dropna().unique())
)

filtered_df = summary_df[
    (summary_df["difficulty"].isin(difficulty_filter)) &
    (summary_df["status"].isin(status_filter))
].copy()

# --------------------------------------------------
# HANDLE EMPTY FILTER RESULT
# --------------------------------------------------
if filtered_df.empty:
    st.warning("No tasks match the selected filters. Please change the sidebar filters.")
    st.stop()

# --------------------------------------------------
# TOP METRICS
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tasks", len(filtered_df))
col2.metric("Avg Review Score", round(filtered_df["review_score"].mean(), 2))
col3.metric("Best Score", round(filtered_df["review_score"].max(), 2))
col4.metric("Total Evidence", int(filtered_df["evidence_count"].sum()))

st.markdown("---")

# --------------------------------------------------
# SUMMARY TABLE
# --------------------------------------------------
st.subheader("📊 Trajectory Summary")
st.dataframe(filtered_df, use_container_width=True)

# --------------------------------------------------
# SCORE DISTRIBUTION
# --------------------------------------------------
st.subheader("📈 Score Distribution")
chart_df = filtered_df.set_index("task_title")[["trajectory_score", "review_score"]]
st.line_chart(chart_df)

# --------------------------------------------------
# LOW SCORE TASKS
# --------------------------------------------------
st.subheader("⚠️ Low Score Tasks")
low_score_df = filtered_df[filtered_df["review_score"] < 8.3]

if not low_score_df.empty:
    st.warning("Some tasks need improvement.")
    st.dataframe(low_score_df, use_container_width=True)
else:
    st.success("All tasks are performing well.")

st.markdown("---")

# --------------------------------------------------
# TASK SEARCH
# --------------------------------------------------
search = st.text_input("Search Task by Title")

filtered_task_ids = set(filtered_df["task_id"].tolist())

filtered_tasks = [
    t for t in all_tasks if int(t["task_id"]) in filtered_task_ids
]

if search.strip():
    filtered_tasks = [
        t for t in filtered_tasks
        if search.lower() in t["task_title"].lower()
    ]

if not filtered_tasks:
    st.warning("No task found for the current search.")
    st.stop()

# --------------------------------------------------
# TASK SELECTOR
# --------------------------------------------------
task_options = {f"{t['task_id']} - {t['task_title']}": t for t in filtered_tasks}
selected = st.selectbox("Select a task", list(task_options.keys()))
task = task_options[selected]

# --------------------------------------------------
# TASK OVERVIEW
# --------------------------------------------------
st.subheader("🧠 Task Overview")
left, right = st.columns([2, 1])

with left:
    st.write("**Title:**", task["task_title"])
    st.write("**Description:**", task["task_description"])

with right:
    st.write("**Difficulty:**", task["difficulty"])
    st.write("**Status:**", task["status"])

# --------------------------------------------------
# PLAN
# --------------------------------------------------
st.subheader("🧭 Plan")
for item in task["trajectory"]["plan"]:
    st.write("-", item)

# --------------------------------------------------
# TRAJECTORY STEPS
# --------------------------------------------------
st.subheader("⚙️ Trajectory Steps")
for step in task["trajectory"]["steps"]:
    with st.expander(f"Step {step['step_number']}: {step['action']}"):
        st.write("**Reasoning:**", step["reasoning"])
        st.write("**Tool Used:**", step["tool_used"])
        st.write("**Output:**", step["output"])

# --------------------------------------------------
# EVIDENCE
# --------------------------------------------------
st.subheader("📂 Evidence")
task_id = int(task["task_id"])
task_evidence = evidence_df[evidence_df["task_id"] == task_id]
st.dataframe(task_evidence, use_container_width=True)

# --------------------------------------------------
# REVIEWER SCORES
# --------------------------------------------------
st.subheader("📝 Reviewer Scores")
review = task["review"]

score_view = pd.DataFrame({
    "Metric": [
        "Task Understanding",
        "Planning",
        "Evidence Grounding",
        "Reasoning Depth",
        "Final Answer",
        "Overall"
    ],
    "Score": [
        review["task_understanding_score"],
        review["planning_score"],
        review["evidence_grounding_score"],
        review["reasoning_depth_score"],
        review["final_answer_score"],
        review["overall_score"]
    ]
})

st.dataframe(score_view, use_container_width=True)

# --------------------------------------------------
# FINAL ANSWER
# --------------------------------------------------
st.subheader("✅ Final Answer")
st.write(task["trajectory"]["final_answer"]["summary"])

st.write("**Justification:**")
for j in task["trajectory"]["final_answer"]["justification"]:
    st.write("-", j)

# --------------------------------------------------
# CONFIDENCE STATUS
# --------------------------------------------------
score = task["review"]["overall_score"]

if score >= 8.5:
    st.success(f"High Confidence Output ({score})")
elif score >= 8.0:
    st.warning(f"Moderate Confidence Output ({score})")
else:
    st.error(f"Low Confidence Output ({score})")

# --------------------------------------------------
# OPTIONAL RAW JSON VIEW
# --------------------------------------------------
show_json = st.checkbox("Show Raw JSON")

if show_json:
    st.subheader("🧾 Raw JSON")
    st.json(task, expanded=False)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption("Built by Anvesh Dubey | OpenClaw-style AI Evaluation System")