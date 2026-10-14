"""Core logic for the Deep-time Data Optimizer."""

import pandas as pd
from typing import List, Dict, Any


ESSENTIAL_FIELDS = [
    "name",
    "age_ma",
    "locality",
    "lithology",
    "taxon_or_unit",
    "reference",
]


def calculate_completeness(row: pd.Series) -> float:
    """Return a simple completeness score (0–1) based on essential fields."""
    present = 0
    for field in ESSENTIAL_FIELDS:
        val = row.get(field)
        if pd.notna(val) and str(val).strip() not in ("", "nan", "None"):
            present += 1
    return round(present / len(ESSENTIAL_FIELDS), 2)


def suggest_improvements(row: pd.Series) -> List[str]:
    """Generate human-readable improvement suggestions."""
    suggestions = []
    if pd.isna(row.get("age_ma")) and pd.isna(row.get("min_age_ma")):
        suggestions.append("Add a numerical age (Ma) or age range.")
    if pd.isna(row.get("locality")) or str(row.get("locality", "")).strip() == "":
        suggestions.append("Add locality or geographic information.")
    if pd.isna(row.get("lithology")) or str(row.get("lithology", "")).strip() == "":
        suggestions.append("Add lithology or rock type.")
    if pd.isna(row.get("taxon_or_unit")) or str(row.get("taxon_or_unit", "")).strip() == "":
        suggestions.append("Add taxonomic name or stratigraphic unit.")
    if pd.isna(row.get("reference")) or str(row.get("reference", "")).strip() == "":
        suggestions.append("Add a reference or citation.")
    if not suggestions:
        suggestions.append("Metadata looks reasonably complete for basic discovery.")
    return suggestions


def generate_summary(row: pd.Series) -> str:
    """Create a short, readable summary for humans and AI systems."""
    parts = []
    name = row.get("name", "Unnamed record")
    parts.append(str(name))

    age = row.get("age_ma")
    if pd.notna(age):
        parts.append(f"at approximately {age} Ma")

    locality = row.get("locality")
    if pd.notna(locality) and str(locality).strip():
        parts.append(f"from {locality}")

    lithology = row.get("lithology")
    if pd.notna(lithology) and str(lithology).strip():
        parts.append(f"in {lithology}")

    unit = row.get("taxon_or_unit")
    if pd.notna(unit) and str(unit).strip():
        parts.append(f"({unit})")

    return " ".join(parts) + "."


def optimize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Add optimization columns to a copy of the input dataframe."""
    result = df.copy()
    result["completeness_score"] = result.apply(calculate_completeness, axis=1)
    result["improvement_suggestions"] = result.apply(
        lambda r: "; ".join(suggest_improvements(r)), axis=1
    )
    result["structured_summary"] = result.apply(generate_summary, axis=1)
    result["optimized_for_retrieval"] = True
    return result
