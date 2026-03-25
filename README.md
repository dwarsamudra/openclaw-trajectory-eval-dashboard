# OpenClaw-Style Trajectory Simulation Portfolio

## Overview
This project simulates OpenClaw-style workflows involving multi-step reasoning, document synthesis, and structured evaluation. It demonstrates how to convert unstructured job descriptions into actionable insights using Python and structured reasoning.

## Objective
To analyze and compare multiple AI-related job descriptions and identify:
- Core technical and analytical skills
- Role-specific requirements
- Overlapping capabilities across roles

## Tasks Performed

### 1. Document Synthesis
- Loaded three job descriptions (AI Annotation, LLM Evaluation, Research Analyst)
- Extracted key skills using keyword matching

### 2. Skill Structuring
- Converted unstructured text into a structured skill matrix
- Identified repeated and role-specific skills

### 3. Category Mapping
- Grouped skills into categories:
  - Technical
  - Analytical
  - QA/Evaluation
  - Documentation
  - Communication

### 4. Data Analysis
- Built comparison tables and summary statistics
- Identified dominant capability areas

### 5. Visualization
- Bar chart of skills by category
- Comparison of job descriptions by skill coverage

### 6. Trajectory Documentation
- Documented full reasoning process:
  - Goal
  - Ambiguities
  - Assumptions
  - Actions
  - Findings
  - Self-review

## Outputs

- `skill_matrix.csv`
- `detailed_skill_results.csv`
- `category_summary.csv`
- `category_matrix.csv`
- `category_chart.png`
- `jd_chart.png`
- `trajectory_1.md`

## Tools Used

- Python
- Pandas
- Matplotlib
- Jupyter Notebook

## Key Skills Demonstrated

- Multi-step reasoning
- Document synthesis
- Data analysis
- Evaluation thinking
- Structured decision-making
- Workflow documentation

## Why this project matters

This project reflects real-world requirements of AI annotation and evaluation roles where:
- tasks are ambiguous
- reasoning must be justified
- workflows span multiple steps and tools
- outputs must be structured and explainable

## Future Improvements

- Use NLP techniques for better skill extraction
- Add synonym detection
- Build automated evaluation pipelines
- Extend to real-world datasets