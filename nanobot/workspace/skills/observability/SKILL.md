# Observability Skill

You have access to logs and traces from the backend via MCP tools.

## When to use

- User asks "What went wrong?" or "Check system health" → follow the investigation workflow below
- User asks about errors, failures, or problems → use `logs_search` or `logs_error_count`
- User asks about a specific request or trace → use `traces_list` then `traces_get`

## Investigation workflow for "What went wrong?" or "Check system health"

1. Call `logs_error_count` with service="backend", minutes=10
2. Call `logs_search` with query `_stream:{service="backend"} AND level:error` and limit=20
3. From the log entries, extract any `trace_id` field values
4. For each trace_id found, call `traces_get` with that ID
5. Summarize findings concisely:
   - How many errors occurred
   - What the error message was (e.g. "connection refused", "OperationalError")
   - Which endpoint was affected
   - What the trace shows about where it failed

## Response format

- State error count first
- List errors concisely: timestamp, event, error message
- If trace found: describe which span failed and why
- Do NOT dump raw JSON — summarize in plain language
- If no errors: say "System looks healthy — no errors in the last N minutes"
