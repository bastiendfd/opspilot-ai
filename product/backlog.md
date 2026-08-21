# Product Backlog

**Rule:** a task exists only if it improves validation, reliable product behaviour, customer value or learning.

| ID | Priority | Objective | Rationale | Dependencies | Definition of done | Status |
|---|---|---|---|---|---|---|
| VAL-01 | P0 | Run 15–20 non-leading discovery interviews. | Tests the costly recurring-workflow hypothesis before broad build. | Interview guide; consent/outreach approval before contact. | Interviews recorded with no fabricated entries; patterns synthesised. | Not started |
| DATA-01 | P0 | Create NOVA INDUSTRIES GmbH synthetic model and source workbooks. | Enables independent, repeatable demo and tests. | Canonical schema. | Actual/Budget/Forecast workbooks plus documented ground truth. | Not started |
| ENG-01 | P0 | Implement Excel ingestion with immutable source IDs. | Foundation of lineage. | Approved dependencies. | Valid workbook becomes canonical records with file/sheet/row lineage. | Not started |
| ENG-02 | P0 | Implement deterministic validation gate. | Prevents false analysis. | ENG-01, schema. | Required quality checks produce structured findings and block unsafe analysis. | Not started |
| ENG-03 | P0 | Implement reconciliation and variance ranking. | Core controller value. | ENG-01/02. | Actual/Budget/Forecast and period comparisons reproduce expected values. | Not started |
| ENG-04 | P0 | Implement reproducible drill-down and evidence bundles. | Makes variance attribution trustworthy. | ENG-03. | Every displayed driver resolves to source records and formula metadata. | Not started |
| ENG-05 | P0 | Add bounded explanation/recommendation formatter. | Translates evidence into usable management language. | ENG-04. | Cannot emit uncited figures; labels inference separately. | Not started |
| UI-01 | P0 | Build minimal upload and evidence review UI. | Validates comprehensibility with a controller. | ENG-01 to ENG-05. | Upload, findings, drill-down, source view, approve/correct/reject work locally. | Not started |
| QA-01 | P0 | Test happy path and injected quality/anomaly cases. | Reliability is MVP success criterion. | DATA-01 and engine modules. | All required tests pass; known anomalies are rediscovered. | Not started |
| SEC-01 | P1 | Threat model and input/prompt-injection tests. | Business files are sensitive/untrusted. | Core interfaces. | Risks documented and key controls tested. | Not started |
| MKT-01 | P1 | Build cited competitor map of 15+ companies. | Identify differentiation and competitive risk. | Official/reputable sources. | Facts/inferences/hypotheses clearly separated. | Complete — first pass |
| VAL-02 | P0 | Run an 8–10 workflow-displacement protocol. | Test whether the current stack actually fails at trusted variance investigation. | Outreach authorisation; interview scorecard. | At least 8 observed workflows; advance only if 3+ show substantial manual reconciliation for a trusted answer. | Not started |
| VAL-03 | P0 | Test data fit with five heterogeneous synthetic export packs. | Avoid mistaking one NOVA schema for a reusable product. | Canonical schema and configurable mappings. | Non-engineer configuration under four hours; repeat refresh without code; no bespoke code. | Not started |
| VAL-04 | P0 | Validate buyer and security feasibility in parallel. | Avoid a false traction signal from user enthusiasm alone. | VAL-02; explicit outreach approval. | Named buyer, credible paid-test path and bounded security/integration requirement. | Not started |
| PROD-01 | P1 | Define feedback data model for approve/correct/reject. | Preserves human oversight and future learning signal. | UI-01. | Feedback is structured and auditable; no training claim. | Not started |
| INT-01 | P2 | Evaluate SAP/Power BI/SharePoint connector sequencing. | Integration can unlock pilots, but must follow validated wedge. | Interview evidence. | Ranked decision record with implementation/revenue evidence. | Deferred |
| SAAS-01 | P3 | Multi-tenant security, SSO and billing. | Premature before pilot signal. | Paying design partners. | Explicit decision to start. | Deferred |
