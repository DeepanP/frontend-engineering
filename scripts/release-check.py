#!/usr/bin/env python3
import subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
checks=[
    ["python3",str(ROOT/"scripts/validate-plugin-version.py")],
    ["python3",str(ROOT/"verify-toolkit.py")] if (ROOT/"verify-toolkit.py").exists() else None,
]
for cmd in [x for x in checks if x]:
    print("+"," ".join(cmd))
    r=subprocess.run(cmd,cwd=ROOT)
    if r.returncode: sys.exit(r.returncode)
required=[
".github/plugin/marketplace.json",
"plugins/frontend-engineering/plugin.json",
"plugins/frontend-engineering/agents/frontend-orchestrator.agent.md",
"plugins/frontend-engineering/workflows/feature-development/WORKFLOW.md",
"plugins/frontend-engineering/workflows/bug-fix/WORKFLOW.md",
"plugins/frontend-engineering/workflows/pr-preparation/WORKFLOW.md",
]
missing=[x for x in required if not (ROOT/x).exists()]
if missing: raise SystemExit("Missing required files:\n"+"\n".join(missing))
print("PASS: release structure checks completed.")
