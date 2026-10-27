---
annotations_creators:
- expert-generated
language:
- en
- es
license:
- cc-by-4.0
multilinguality:
- multilingual
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- tabular-classification
- tabular-regression
- text-retrieval
task_ids: []
pretty_name: Paris Sensory Impact & Acoustic Tourism Dataset (SIS)
homepage: https://spacejourney.app/en/city/paris-en/
tags:
- sensory-travel
- acoustic-comfort
- solarpunk
- paris-heritage
- urban-wellbeing
- restorative-routes
- 3d-gis
- geospatial
- smart-cities
- sustainability
- environment
- urban-planning
---

# 🥐 Paris Sensory Impact & Acoustic Tourism Dataset (SIS)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Principal Investigator & Author:** [Daniel Adolfo Duque Romero](https://spacejourney.app/)  
**Curated & Maintained by:** [Space Journey Studio](https://spacejourney.app/)  
**City Exploration Hub:** [Paris Contemplative Travel Guide](https://spacejourney.app/en/city/paris-en/)  
**Sensory Itinerary Planner:** [https://spacejourney.app/en/itinerary-planner/](https://spacejourney.app/en/itinerary-planner/)  
**Sensory Copilot (AI Guide):** [https://spacejourney.app/en/ai-journey-assistant/](https://spacejourney.app/en/ai-journey-assistant/)  
**License:** Creative Commons Attribution 4.0 International ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/))

---

## 📌 Dataset Summary

The **Paris Sensory Impact Dataset (SIS)** is an independent, expert-curated benchmark capturing quantitative environmental, acoustic, and luminous telemetry across 15 iconic sanctuary sites, Haussmann cloisters, and hidden gardens in Paris, France.

Designed for urban wellbeing research and mindful travel routing, this dataset establishes empirical baselines to counter overtourism and acoustic saturation along the Seine corridor. It powers the algorithmic routing of the [Space Journey Sensory Itinerary Planner](https://spacejourney.app/en/itinerary-planner/).

---

## 🚀 Quick Start (Python)

Load the dataset directly using the Hugging Face `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("spacejourney/paris-sensory-impact-dataset")
print(dataset["train"][0])
```

---

## 📊 Dataset Structure & Features

Available in both structured JSON (`data/paris_sensory_dataset_v1.json`) and tabular CSV (`data/paris_sensory_dataset_v1.csv`).

| Feature | Type | Description | Example |
| :--- | :---: | :--- | :--- |
| `id` | string | Unique sensory node identifier | `"PAR-01"` |
| `name` | string | Curated experience title | `"Sainte-Chapelle: The Medieval Reliquary of Light"` |
| `city` | string | Metropolitan destination | `"Paris"` |
| `neighborhood` | string | Urban district | `"Île de la Cité / Distrito 1"` |
| `duration_minutes` | int | Recommended contemplative duration | `45` |
| `optimal_window` | string | Optimal solar light & calm window | `"10:30 - 15:00 CET"` |
| `ideal_season` | string | Preferred weather season | `"Primavera / Días de sol intenso"` |
| `sis_score` | int | Sensory Impact Score (0 to 100) | `89` |
| `estimated_noise_db` | int | Ambient sound pressure level (dB) | `50` |
| `sensory_intensity_level` | int | Physical exertion level (1 to 4) | `3` |
| `canonical_url` | string | Verified English experience endpoint | `"https://spacejourney.app/en/experiencia/sainte-chapelle-the-medieval-reliquary-of-light/"` |
| `description` | string | Qualitative architectural narrative | `"La Sainte-Chapelle es el sueño cumplido del gótico radiante..."` |

---

## 🌐 Official Verification & Live Implementations

* **English City Guide:** [https://spacejourney.app/en/city/paris-en/](https://spacejourney.app/en/city/paris-en/) *(también en [Español](https://spacejourney.app/ciudad/paris/))*
* **Global Itinerary Planner:** [https://spacejourney.app/en/itinerary-planner/](https://spacejourney.app/en/itinerary-planner/)
* **Official Website:** [https://spacejourney.app/](https://spacejourney.app/)

