# Founder Report — Kickoff Cycle

**Date:** 2026-08-17  
**Scope:** independent local foundation only. No deployment, outreach, purchase, legal action, external model call or employer/customer data use.

## What changed

- Created a new local Git repository at `C:\Users\basti\opspilot`.
- Created the proposed product/research/data/source/test structure.
- Documented the vision, architecture, product principles, security posture, compliance notes, roadmap, decision log, requirements, workflow and P0 backlog.
- Created a customer-discovery framework and initial ICP hypothesis.
- Created the first cited competitive landscape covering 17 named alternatives.

## What was built

- Architecture v0: file-first deterministic analytical core; optional LLM only after evidence construction.
- Explicit canonical data and lineage contract.
- Security/data boundary: synthetic/public/authorised data only; no direct enterprise connections; no external LLM egress by default.
- Economic model placeholder: 4 controllers × 15h/month × 12 × €75/h = **€54,000/year** illustrative capacity value.

## What we learned

- The space is crowded with broad AI/BI, process intelligence, FP&A and industrial-operation platforms.
- Therefore generic “AI insights” is not a viable positioning wedge.
- The credible narrow wedge is the controller investigation loop: validate → reconcile → attribute → expose sources → human-reviewed action.
- Product-market fit is entirely unvalidated: no real customer interview, workflow measurement, willingness-to-test or willingness-to-pay evidence exists yet.

## Evidence

- 17 official source URLs recorded and cited in `research/competitive-landscape.md`.
- Citation verification passed at 26% source-bearing sentence coverage; facts are cited and strategic interpretations are explicitly labelled.
- Local environment inspection: Git and Python 3.11 available; FastAPI/Pydantic available; `pandas`, `openpyxl`, `pytest`, Streamlit and Docker absent.

## Main risks

1. Incumbent substitution: SAP/Microsoft/FP&A platforms may be adequate for target users.
2. Integration/security burden may exceed value before the product proves itself.
3. Synthetic-data success may not survive imperfect real exports.
4. Monthly workflow may not create sufficient measurable economic value.
5. V.I.E constraints may restrict commercial activity; legal position must be confirmed before any outreach/commercialisation.

## Competitive developments

Broad capabilities in Microsoft Fabric/Power BI, Celonis, Planful, Vena, Cube, Tulip, PTC and logistics AI products reinforce that the product must lead with **verified, traceable workflow value**, not agent novelty. See the cited landscape for individual evidence and limitations.

## Metrics

| Metric | Current | Status |
|---|---:|---|
| Real interviews | 0 / 15–20 | Not started |
| Controlled source workbooks | 0 / 3 | Blocked on approved Excel dependencies |
| Automated tests | 0 | Blocked on approved pytest dependency |
| P0 engine modules | 0 / 5 | Not started |
| Competitors first-mapped | 17 | Complete for first pass; depth incomplete |
| Employer/customer data used | 0 | As required |

## Decisions needed from Bastien

1. May I install the proposed local Python development dependencies (`pandas`, `openpyxl`, `pytest`, Streamlit) to build and test the synthetic Excel MVP?
2. Before contact: do you authorise any customer-discovery outreach? If yes, what channel and relationship boundaries are acceptable? No outreach will occur without this.
3. Is the initial controller-led Actual/Budget/Forecast wedge the preferred hypothesis to test first, or do you want a deliberately constrained comparison against a different workflow before build?

## Recommended next 3 actions

1. Approve or decline the local dependency installation; if approved, build the synthetic dataset and one tested end-to-end reconciliation slice via TDD.
2. Review the interview guide and define permissible outreach boundaries, then begin real discovery only with consent.
3. Deepen the competitor map only for the short list most likely to appear in target interviews, especially SAP/Microsoft and the FP&A alternative actually used by each participant.
