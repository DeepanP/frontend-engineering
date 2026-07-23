#!/usr/bin/env python3
import json, re, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PLUGIN=ROOT/"plugins/frontend-engineering/plugin.json"
MARKET=ROOT/".github/plugin/marketplace.json"
CHANGELOG=ROOT/"CHANGELOG.md"

def load(p): return json.loads(p.read_text(encoding="utf-8"))
def save(p,d): p.write_text(json.dumps(d,indent=2)+"\n",encoding="utf-8")
def parse(v):
    m=re.fullmatch(r"(\d+)\.(\d+)\.(\d+)",v)
    if not m: raise SystemExit(f"Invalid semantic version: {v}")
    return list(map(int,m.groups()))
def bump(v,kind):
    a=parse(v)
    if kind=="major": return f"{a[0]+1}.0.0"
    if kind=="minor": return f"{a[0]}.{a[1]+1}.0"
    if kind=="patch": return f"{a[0]}.{a[1]}.{a[2]+1}"
    parse(kind); return kind

if len(sys.argv)!=2:
    raise SystemExit("Usage: python3 scripts/bump-plugin-version.py major|minor|patch|X.Y.Z")

plugin=load(PLUGIN); market=load(MARKET)
old=plugin["version"]; new=bump(old,sys.argv[1])
plugin["version"]=new

found=False
for item in market["plugins"]:
    if item["name"]=="frontend-engineering":
        item["version"]=new; found=True
if not found: raise SystemExit("frontend-engineering missing from marketplace.json")

save(PLUGIN,plugin); save(MARKET,market)
print(f"frontend-engineering: {old} -> {new}")
print("Updated plugin.json and marketplace plugin entry.")
print("Review CHANGELOG.md, commit, tag, and push after CI passes.")
