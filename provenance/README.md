# Provenance

Every substantive AI generation run creates one YAML record named:

```text
YYYYMMDD-HHMMSS-<prompt-id>-<scope>.yaml
```

Records must conform to `schemas/provenance.schema.json` and list inputs, outputs, sources, validation, unresolved items, and human approvals.
