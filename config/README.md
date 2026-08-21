# Configuration

Only non-secret, environment-neutral configuration belongs here.

- Do not add API keys, tokens, passwords, customer identifiers, private URLs or production connection strings.
- Add a committed `.env.example` only when an external service is explicitly approved.
- Model provider selection must stay separate from deterministic business logic.
