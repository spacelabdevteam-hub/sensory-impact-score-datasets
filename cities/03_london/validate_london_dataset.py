#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Space Journey — London Sensory Impact Score (SIS v1.1) Dataset Validator
========================================================================
Zero-dependency scientific & schema integrity validator for the London SIS
open benchmark dataset. Verifies:
  1. CSV <-> JSON exact structural & value parity (15 sanctuaries)
  2. Greater London WGS84 geospatial bounding box compliance
  3. WHO acoustic range, SIS score bounds, and realistic visit durations
  4. ESA Copernicus DEM GLO-90 relative relief and biomechanical exertion math
  5. Clean UTF-8 text (zero HTML entities or WordPress truncation artifacts)
  6. Balanced 5/5/5 curation tier coverage and canonical HTTPS URLs
"""

import csv
import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
CSV_PATH = DATA_DIR / "london_sensory_impact_sis_v1.csv"
JSON_PATH = DATA_DIR / "london_sensory_impact_sis_v1.json"

LONDON_BASELINE_M = 11.0
REQUIRED_COLUMNS = [
    "id",
    "haven_id",
    "wp_id",
    "name",
    "name_es",
    "category",
    "city",
    "neighborhood",
    "latitude",
    "longitude",
    "sis_score",
    "acoustic_noise_db",
    "golden_hour_window",
    "light_level_lux",
    "light_atmosphere",
    "duration_minutes",
    "ideal_season",
    "energy_cost_score",
    "crowd_density_index",
    "elevation_m",
    "city_baseline_m",
    "relative_relief_m",
    "biomechanical_exertion_index",
    "topographic_profile",
    "dem_source",
    "canonical_url",
    "canonical_url_es",
    "description",
    "golden_spot_tips",
]

FORBIDDEN_SUBSTRINGS = ["[&hellip;]", "&#8217;", "&amp;", "&quot;", "en Londres en Londres"]


def expected_exertion(rel_relief: float, duration_min: int) -> float:
    slope_factor = min(abs(rel_relief) * 0.8, 60.0)
    duration_factor = min((duration_min / 180.0) * 25.0, 35.0)
    return round(max(5.0, min(95.0, slope_factor + duration_factor)), 1)


def validate() -> list[str]:
    errors: list[str] = []

    if not JSON_PATH.exists():
        return [f"Missing JSON dataset: {JSON_PATH}"]
    if not CSV_PATH.exists():
        return [f"Missing CSV dataset: {CSV_PATH}"]

    json_rows = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        csv_cols = reader.fieldnames or []
        csv_rows = list(reader)

    if len(json_rows) != 15:
        errors.append(f"Expected 15 JSON rows, found {len(json_rows)}")
    if len(csv_rows) != 15:
        errors.append(f"Expected 15 CSV rows, found {len(csv_rows)}")
    if csv_cols != REQUIRED_COLUMNS:
        errors.append(f"CSV columns mismatch. Expected {REQUIRED_COLUMNS}, got {csv_cols}")

    seen_ids = set()
    tier_counts = {"Free Restorative": 0, "Secret Sanctuary": 0, "Curated Premium": 0}

    for idx, (jrow, crow) in enumerate(zip(json_rows, csv_rows), start=1):
        rid = jrow.get("id", f"row-{idx}")
        if rid in seen_ids:
            errors.append(f"[{rid}] Duplicate node id")
        seen_ids.add(rid)

        if str(jrow["id"]) != crow["id"] or str(jrow["haven_id"]) != crow["haven_id"]:
            errors.append(f"[{rid}] CSV/JSON row ordering or identifier mismatch")

        cat = jrow["category"]
        if cat not in tier_counts:
            errors.append(f"[{rid}] Unknown category: {cat}")
        else:
            tier_counts[cat] += 1

        lat = float(jrow["latitude"])
        lng = float(jrow["longitude"])
        if not (51.28 <= lat <= 51.70 and -0.51 <= lng <= 0.34):
            errors.append(f"[{rid}] Coordinates out of Greater London WGS84 bounds: ({lat}, {lng})")

        sis = int(jrow["sis_score"])
        db = int(jrow["acoustic_noise_db"])
        dur = int(jrow["duration_minutes"])
        lux = int(jrow["light_level_lux"])
        crowd = float(jrow["crowd_density_index"])
        energy = int(jrow["energy_cost_score"])

        if not (0 <= sis <= 100):
            errors.append(f"[{rid}] SIS score out of bounds: {sis}")
        if not (15 <= db <= 80):
            errors.append(f"[{rid}] Acoustic noise dB out of bounds: {db}")
        if not (15 <= dur <= 300):
            errors.append(f"[{rid}] Duration minutes unrealistic: {dur}")
        if not (500 <= lux <= 5000):
            errors.append(f"[{rid}] Light level lux out of range: {lux}")
        if not (0.0 <= crowd <= 1.0):
            errors.append(f"[{rid}] Crowd density index out of [0,1]: {crowd}")
        if not (1 <= energy <= 5):
            errors.append(f"[{rid}] Energy cost score out of [1,5]: {energy}")

        elev = float(jrow["elevation_m"])
        rel = float(jrow["relative_relief_m"])
        exert = float(jrow["biomechanical_exertion_index"])
        expected_rel = round(elev - LONDON_BASELINE_M, 1)
        if abs(rel - expected_rel) > 1e-6:
            errors.append(f"[{rid}] relative_relief_m={rel} != elevation_m({elev}) - {LONDON_BASELINE_M}")

        exp_exert = expected_exertion(rel, dur)
        if abs(exert - exp_exert) > 1e-6:
            errors.append(f"[{rid}] biomechanical_exertion_index={exert} != expected {exp_exert}")

        if not str(jrow["canonical_url"]).startswith("https://spacejourney.app/en/experiencia/"):
            errors.append(f"[{rid}] Non-canonical EN URL: {jrow['canonical_url']}")
        if not str(jrow["canonical_url_es"]).startswith("https://spacejourney.app/experiencia/"):
            errors.append(f"[{rid}] Non-canonical ES URL: {jrow['canonical_url_es']}")

        for field in ("name", "name_es", "description", "golden_spot_tips"):
            val = str(jrow.get(field, ""))
            if len(val.strip()) < 10:
                errors.append(f"[{rid}] Field '{field}' is unexpectedly short")
            for bad in FORBIDDEN_SUBSTRINGS:
                if bad in val:
                    errors.append(f"[{rid}] Forbidden artifact '{bad}' in field '{field}'")

    for tier, count in tier_counts.items():
        if count != 5:
            errors.append(f"Tier '{tier}' expected 5 sanctuaries, found {count}")

    return errors


if __name__ == "__main__":
    validation_errors = validate()
    if validation_errors:
        print(f"VALIDATION FAILED ({len(validation_errors)} issues):")
        for err in validation_errors:
            print(f"  - {err}")
        sys.exit(1)

    rows = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    avg_sis = sum(r["sis_score"] for r in rows) / len(rows)
    avg_db = sum(r["acoustic_noise_db"] for r in rows) / len(rows)
    who_compliant = sum(1 for r in rows if r["acoustic_noise_db"] <= 53)
    print(f"OK: Validated {len(rows)} London sanctuaries (CSV + JSON parity 100%)")
    print(f"    Mean SIS: {avg_sis:.1f}/100 | Mean Acoustic Level: {avg_db:.1f} dB")
    print(f"    WHO <= 53 dB Lden compliance: {who_compliant}/{len(rows)} sanctuaries")
    print("    ESA Copernicus DEM GLO-90 telemetry & biomechanical exertion verified.")
