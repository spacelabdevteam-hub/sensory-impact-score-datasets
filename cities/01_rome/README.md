---
annotations_creators:
- expert-generated
language:
- en
- es
- pt
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
pretty_name: Rome Sensory Impact & Acoustic Heritage Dataset (SIS)
homepage: https://spacejourney.app/
tags:
- sensory-travel
- acoustic-comfort
- solarpunk
- rome-heritage
- urban-wellbeing
- restorative-routes
- 3d-gis
- geospatial
- smart-cities
- sustainability
- environment
- urban-planning
---

# 🏛️ Rome Sensory Impact & Acoustic Heritage Dataset (SIS)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22756473.svg)](https://doi.org/10.5281/zenodo.22756473)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Principal Investigator & Author:** [Daniel Adolfo Duque Romero](https://spacejourney.app/)  
**Curated & Maintained by:** [Space Journey Studio](https://spacejourney.app/)  
**Open Science Repository:** [Zenodo (CERN Infrastructure) - DOI: 10.5281/zenodo.22756473](https://doi.org/10.5281/zenodo.22756473)  
**Project Homepage:** [https://spacejourney.app/](https://spacejourney.app/)  
**Interactive 3D Spatial Atlas:** [https://spacejourney.app/play/roma-atlas/](https://spacejourney.app/play/roma-atlas/)  
**Sensory Itinerary Planner:** [https://spacejourney.app/en/itinerary-planner/](https://spacejourney.app/en/itinerary-planner/)

---

## 📌 Dataset Summary

The **Rome Sensory Impact Dataset (SIS)** is an independent, expert-curated benchmark recording quantitative environmental, acoustic, and luminous telemetry across 15 monumental and sanctuary heritage sites in Rome, Italy. 

Designed for urban wellbeing research and restorative travel planning, this dataset provides empirical metrics for acoustic tranquility, luminous comfort, and human energy preservation. It powers the algorithmic routing of the [Space Journey Sensory Itinerary Planner](https://spacejourney.app/en/itinerary-planner/) and the [3D Sensory Atlas WebGL Engine](https://spacejourney.app/play/roma-atlas/).

---

## 📊 Dataset Structure & Features

The dataset is provided in both structured JSON (`data/rome_sensory_impact_sis_v1.json`) and tabular CSV (`data/rome_sensory_impact_sis_v1.csv`).

| Feature | Type | Description | Example |
| :--- | :---: | :--- | :--- |
| `id` | string | Unique sensory node identifier | `"P-04"` |
| `name` | string | Full name of the heritage experience | `"Vittoriano: Terrazza delle Quadrighe"` |
| `category` | string | Curation tier (`Free Restorative`, `Secret Sanctuary`, `Curated Premium`) | `"Curated Premium"` |
| `neighborhood` | string | Historic district or urban zone | `"Piazza Venezia"` |
| `latitude` | float | Decimal coordinate (WGS84) | `41.8947` |
| `longitude` | float | Decimal coordinate (WGS84) | `12.4839` |
| `sis_score` | int | Continuous Sensory Impact Score (0 to 100 scale, where 100 indicates maximum restorative calm; mapped to 5 traveler tiers in UX) | `94` |
| `acoustic_noise_db` | int | Ambient sound pressure level in decibels (A-weighted, dB) | `42` |
| `golden_hour_window` | string | Optimal solar lighting window for contemplation | `"18:15 - 19:40 CET"` |
| `light_level_lux` | int | Ambient luminous flux under optimal window (Lux) | `3200` |
| `energy_cost_score` | int | Physical exertion index (1 = Minimal / Elevator, 5 = Extreme steep incline) | `1` |
| `crowd_density_index` | float | Congestion index (0.00 = Deserted sanctuary, 1.00 = Severe mass crowding) | `0.08` |
| `canonical_url` | string | Interactive endpoint on Space Journey | `"https://spacejourney.app/play/roma-atlas/"` |
| `description` | string | Qualitative architectural and contemplative narrative | `"Panoramic glass elevator ascent..."` |

---

## 🔬 Methodology: The Sensory Impact Score (SIS)

The **Sensory Impact Score (SIS)** is calculated as a multi-factor restorative index evaluated on a continuous scale from 0 to 100. In user-facing applications, this score is grouped into 5 sensory tiers (Levels 1 to 5) to assist traveler decision-making.

### Algorithmic Definition & Computational Model:
```text
SIS = 100 - (0.35 * NoisePenalty + 0.30 * CrowdPenalty + 0.20 * ExertionPenalty - 0.15 * LightBonus)
```

Where:
* **NoisePenalty (Weight: 35%):** Sound pressure level normalized against the World Health Organization (WHO) 53 dB Lden environmental guideline. Baseline quietude (< 40 dB) incurs 0 penalty, while high-friction corridors (> 70 dB) receive full penalty weighting.
* **CrowdPenalty (Weight: 30%):** Pedestrian congestion index (0.00 = solitary contemplation, 1.00 = acute mass tourism density).
* **ExertionPenalty (Weight: 20%):** Physical exertion metric (1 to 5 scale accounting for elevation gradient, steps, and cobblestone fatigue).
* **LightBonus (Weight: 15%):** Solar quality coefficient rewarding warm, glare-free golden hour irradiance (2,000 to 3,500 Lux).

### Mathematical Formulation:
$$\text{SIS} = 100 - \left( 0.35 \times \text{NoisePenalty} + 0.30 \times \text{CrowdPenalty} + 0.20 \times \text{ExertionPenalty} - 0.15 \times \text{LightBonus} \right)$$

1. **Acoustic Decibel Thresholds (WHO Environmental Noise Guidelines Alignment):**
   * `< 40 dB`: Deep Restorative Sanctuary (e.g., Via Appia Antica at 34 dB, Parco degli Acquedotti at 36 dB).
   * `40 - 48 dB`: High Contemplation Zone (e.g., Gianicolo Hill at 41 dB, Vittoriano Chariots Terrace at 42 dB).
   * `> 55 dB`: Urban Friction Zone (mitigated by specialized dawn/dusk visiting protocols).

2. **Solar Zenith & Lux Telemetry:**
   * Natural sunlight calculated per geographic orientation to identify glare-free, warm golden hour windows (2,000 - 3,500 Lux).

3. **Human Energy Preservation (EC):**
   * Calibrating walking elevation gain, cobblestone fatigue, and thermal stress to ensure travelers avoid sensory exhaustion.

---

## 🎯 Applications & Research Context

* **Algorithmic Route Curation:** Training generative systems to synthesize travel itineraries that prioritize mental recovery, acoustic health, and unhurried pacing.
* **Spatial Computing & Digital Twins:** Populating WebGL and Three.js environments with empirical acoustic telemetry ([The Sensory Atlas](https://spacejourney.app/play/roma-atlas/)).
* **Urban Soundscape Exploration:** Independent reference data for analyzing pedestrian tranquility corridors in historic metropolitan centers.

---

## 🌐 Project Ecosystem & Implementations

* **Project Homepage:** [https://spacejourney.app/](https://spacejourney.app/)
* **Open Science Repository (Zenodo):** [https://doi.org/10.5281/zenodo.22756473](https://doi.org/10.5281/zenodo.22756473)
* **Knowledge Graph (Wikidata):** [https://www.wikidata.org/wiki/Q141455396](https://www.wikidata.org/wiki/Q141455396)
* **Interactive 3D Atlas:** [https://spacejourney.app/play/roma-atlas/](https://spacejourney.app/play/roma-atlas/)
* **Sensory Route Planner:** [https://spacejourney.app/en/itinerary-planner/](https://spacejourney.app/en/itinerary-planner/)
* **AI Sensory Assistant:** [https://spacejourney.app/en/ai-journey-assistant/](https://spacejourney.app/en/ai-journey-assistant/)
* **Design Case Study:** [Behance Showcase](https://www.behance.net/gallery/255668901/Space-Journey-Solarpunk-UX-Itinerary-Planner)

---

## 📜 Academic Citation & Attribution (BibTeX)

If you use this dataset or the SIS methodology in academic research, AI fine-tuning, or spatial applications, please cite:

```bibtex
@dataset{duque_romero_2026_zenodo_22756473,
  author       = {Duque Romero, Daniel Adolfo and {Space Journey Studio}},
  title        = {Rome Sensory Impact & Acoustic Heritage Dataset (SIS)},
  year         = {2026},
  month        = sep,
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.22756473},
  url          = {https://doi.org/10.5281/zenodo.22756473}
}
```

Or reference the Hugging Face repository:

```bibtex
@misc{spacejourney_roma_hf_2026,
  author       = {Duque Romero, Daniel Adolfo},
  title        = {Rome Sensory Impact & Acoustic Heritage Dataset (SIS)},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/spacejourney/rome-sensory-impact-dataset}}
}
```
