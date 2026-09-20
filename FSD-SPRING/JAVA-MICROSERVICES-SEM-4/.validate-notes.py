#!/usr/bin/env python3
"""Validate NOTES/ and IMAGES/ after conversion."""
import json, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTES = ROOT / "NOTES"
IMAGES = ROOT / "IMAGES"
RAW = ROOT / "raw-files"
m = json.load(open(ROOT / ".processing-map.json"))

expected_notes = {n["dest"] for n in m["notes"] + m["image_only_notes"]}
actual_notes = {p.name for p in NOTES.glob("*.md")}
expected_imgs = {ip["dest"] for ip in m["images"]}
actual_imgs = {p.name for p in IMAGES.glob("*.png")}

print("=== COUNTS ===")
print(f"Expected notes: {len(expected_notes)}  Actual: {len(actual_notes)}")
print(f"Expected imgs:  {len(expected_imgs)}  Actual: {len(actual_imgs)}")
print(f"Raw txt still:  {len(list(RAW.glob('*.txt')))}")
print(f"Raw png still:  {len(list(RAW.glob('*.png')))}")

missing_notes = sorted(expected_notes - actual_notes)
extra_notes = sorted(actual_notes - expected_notes)
missing_imgs = sorted(expected_imgs - actual_imgs)
print("\nMissing notes:", missing_notes or "none")
print("Extra notes:", extra_notes or "none")
print("Missing imgs:", missing_imgs or "none")

space_files = [n for n in actual_notes if " " in n] + [i for i in actual_imgs if " " in i]
print("Filenames with spaces:", space_files or "none")

issues = []
ai_bad = []
mycodes_bad = []
img_section_bad = []
broken_refs = []
abs_paths = []

for md in sorted(NOTES.glob("*.md")):
    text = md.read_text(encoding="utf-8", errors="replace")
    if "## 🤖 AI Points" not in text:
        ai_bad.append((md.name, "missing AI Points heading"))
    else:
        # count numbered points after AI Points
        after = text.split("## 🤖 AI Points", 1)[1].split("## 💻 My Codes", 1)[0]
        nums = re.findall(r"(?m)^\s*\d+\.\s+", after)
        if len(nums) != 5:
            ai_bad.append((md.name, f"AI points count={len(nums)}"))
    if "## 💻 My Codes" not in text:
        mycodes_bad.append(md.name)
    else:
        body = text.split("## 💻 My Codes", 1)[1].split("## 🖼️ Image", 1)[0].strip()
        if body:
            mycodes_bad.append(f"{md.name} (not empty: {body[:40]!r})")
    if "## 🖼️ Image" not in text:
        img_section_bad.append(md.name)
    for ref in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
        if ref.startswith("/") or re.match(r"^[A-Za-z]:\\", ref) or ref.startswith("file:"):
            abs_paths.append((md.name, ref))
        elif ref.startswith("../IMAGES/"):
            target = NOTES.parent / ref[3:]  # strip ../
            # path is NOTES/../IMAGES/x -> IMAGES/x
            target = (md.parent / ref).resolve()
            if not target.exists():
                broken_refs.append((md.name, ref))
        else:
            broken_refs.append((md.name, f"non-relative-or-unexpected:{ref}"))

print("\n=== STRUCTURE CHECKS ===")
print("AI Points issues:", ai_bad or "none")
print("My Codes issues:", mycodes_bad or "none")
print("Missing Image section:", img_section_bad or "none")
print("Broken image refs:", broken_refs or "none")
print("Absolute paths:", abs_paths or "none")

ok = not (missing_notes or missing_imgs or ai_bad or mycodes_bad or img_section_bad or broken_refs or abs_paths or space_files)
print("\nOVERALL:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
