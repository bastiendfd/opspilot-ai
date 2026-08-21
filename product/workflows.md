# MVP Workflow

## 1. Upload and inspect

User assigns Actual, Budget and Forecast workbooks. The system displays recognised sheets, headers and validation status before analysis.

## 2. Validate

The system runs deterministic checks. A blocking issue stops insights and links the user to affected rows. Warnings remain visible in all downstream views.

## 3. Analyse

The system computes comparisons and ranks material variances. It never presents an LLM-generated value as a calculation.

## 4. Investigate

User selects a variance, drills into dimensions and sees percentage contribution, source records, formula and assumptions. The user can filter but cannot lose lineage.

## 5. Review explanation

The system frames:

- what happened (computed measure);
- evidence-supported drivers;
- possible explanation (explicitly labelled if inferential);
- suggested owner/action (proposal, not execution);
- confidence derived from evidence completeness, not model self-report alone.

## 6. Human feedback

User chooses Approve, Correct or Reject; correction stores a structured reason and does not alter historical computed source facts.
