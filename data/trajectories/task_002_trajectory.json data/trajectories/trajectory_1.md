# Trajectory 1: Document Synthesis for AI Annotation Roles

## User Goal
Compare multiple AI annotation, LLM evaluation, and research-oriented job descriptions to identify common skills and build a unified skill matrix.

## Why this task matters
This task simulates a real OpenClaw-style workflow where information from multiple documents must be read, structured, compared, and summarized into a usable output.

## Ambiguities
- Which skills are core across roles and which are role-specific?
- Should repeated keywords be treated as stronger signals?
- How should technical skills and communication skills be balanced?

## Assumptions
- Skills repeated across multiple job descriptions are likely more important.
- Explicitly stated tools and capabilities are stronger evidence than inferred skills.
- A structured matrix is easier to interpret than raw text comparison.

## Planned Approach
1. Collect three realistic job descriptions related to annotation, evaluation, and AI research workflows
2. Read them into Python
3. Define a skill keyword list
4. Check the presence of each skill in each job description
5. Build a skill matrix
6. Count repeated skills
7. Save the output for reporting

## Actions Taken

### Step 1: Prepared the source documents
Three role descriptions were created and saved as text files inside the data folder.

**Reason:** The task required multiple comparable documents as inputs.

### Step 2: Loaded the documents into Python
The notebook read each job description from the data folder.

**Reason:** Structured analysis cannot begin until the source text is available in memory.

### Step 3: Defined a skill keyword list
A list of relevant skills such as Python, research, evaluation, annotation, reasoning, documentation, SQL, Excel, NLP, and communication was created.

**Reason:** A controlled list makes beginner-level comparison consistent and explainable.

### Step 4: Checked each document for each skill
The code searched whether each keyword appeared in each job description.

**Reason:** This converted unstructured text into structured true/false information.

### Step 5: Built a matrix
The extracted results were converted into a table where rows represented skills and columns represented job descriptions.

**Reason:** A matrix makes overlap and differences easier to analyze.

### Step 6: Calculated repeated skills
The notebook counted how many job descriptions mentioned each skill.

**Reason:** Repeated skills likely represent common expectations across similar roles.

### Step 7: Saved the result
The final skill matrix was exported as a CSV file to the outputs folder.

**Reason:** Saving the output makes the result reusable and portfolio-ready.

## Intermediate Findings
- Python, research, annotation, evaluation, reasoning, documentation, and communication appeared across multiple descriptions.
- Some skills were role-specific, while others were common across all or most roles.
- The matrix format made the comparison clearer than manual reading alone.

## Final Output
A structured skill matrix was generated to compare three job descriptions related to AI annotation and evaluation work.

## Self-Review
## Category-Level Insight
The extracted skills were also grouped into broader categories such as Technical, Analytical, QA/Evaluation, Documentation, and Communication. This made the output more useful because it showed not only which skills appeared, but also what type of capability each role emphasized.

### Strengths
- Clear and structured workflow
- Easy to explain in an interview
- Demonstrates document synthesis and reasoning

### Limitations
- Keyword matching is simple and may miss synonyms or implied skills
- The result depends on the chosen keyword list

### Future Improvements
- Add skill categories such as technical, analytical, QA, and communication
- Use NLP techniques to detect similar terms
- Add weighted scoring for stronger prioritization
## Visualization Insight
Simple bar charts were created to make the synthesis easier to interpret. One chart summarized matched skills by category, and another compared the job descriptions by total matched skills. This made the final analysis more readable and presentation-ready.