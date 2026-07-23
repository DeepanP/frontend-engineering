#!/usr/bin/env python3
import json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
plugin=json.loads((ROOT/"plugins/frontend-engineering/plugin.json").read_text())
market=json.loads((ROOT/".github/plugin/marketplace.json").read_text())
v=plugin.get("version","")
if not re.fullmatch(r"\d+\.\d+\.\d+",v):
    raise SystemExit(f"plugin.json version is not SemVer: {v}")
entry=next((x for x in market.get("plugins",[]) if x.get("name")=="frontend-engineering"),None)
if not entry: raise SystemExit("frontend-engineering missing from marketplace")
if entry.get("version")!=v:
    raise SystemExit(f"Version mismatch: plugin.json={v}, marketplace={entry.get('version')}")
source=entry.get("source","").lstrip("./")
if source!="plugins/frontend-engineering":
    raise SystemExit(f"Unexpected marketplace source: {entry.get('source')}")
if not (ROOT/source/"plugin.json").exists():
    raise SystemExit(f"Marketplace source does not resolve: {source}")
print(f"PASS: frontend-engineering version {v} is synchronized and source resolves.")
