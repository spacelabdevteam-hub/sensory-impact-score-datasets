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
pretty_name: London Sensory Impact & Acoustic Heritage Dataset (SIS)
homepage: https://spacejourney.app/en/city/london/
tags:
- sensory-travel
- acoustic-comfort
- solarpunk
- london-heritage
- urban-wellbeing
- restorative-routes
- copernicus-dem
- 3d-gis
- geospatial
- smart-cities
- sustainability
- environment
- urban-planning
---

# 🌿 London Sensory Impact & Acoustic Heritage Dataset (SIS v1.1)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/spacelabdevteam-hub/sensory-impact-score-datasets/blob/main/cities/03_london/explore_london_sensory_impact.ipynb)
[![Hugging Face Dataset](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-london--sensory--impact--dataset-FFD21E)](https://huggingface.co/datasets/spacejourney/london-sensory-impact-dataset)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22756473.svg)](https://doi.org/10.5281/zenodo.22756473)
[![WHO Acoustic Guideline](https://img.shields.io/badge/WHO_Guideline-53_dB_Lden-006699)](https://spacejourney.app/standards/sensory-impact-score/)
[![Copernicus DEM](https://img.shields.io/badge/Elevation-ESA_Copernicus_DEM_GLO--90-10B981)](https://spacejourney.app/standards/sensory-impact-score/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-10B981.svg)](https://creativecommons.org/licenses/by/4.0/)

**Principal Investigator & Author:** [Daniel Adolfo Duque Romero](https://spacejourney.app/)  
**Curated & Maintained by:** [Space Journey Studio](https://spacejourney.app/)  
**Open Science Archive:** [Zenodo (CERN Infrastructure) — DOI: 10.5281/zenodo.22756473](https://doi.org/10.5281/zenodo.22756473)  
**Hugging Face Hub Dataset:** [spacejourney/london-sensory-impact-dataset](https://huggingface.co/datasets/spacejourney/london-sensory-impact-dataset)  
**City Exploration Hub:** [London Contemplative Travel Guide](https://spacejourney.app/en/city/london/) *(also in [Español](https://spacejourney.app/ciudad/londres/))*  
**Sensory Itinerary Planner:** [https://spacejourney.app/en/itinerary-planner/](https://spacejourney.app/en/itinerary-planner/)  
**Sensory Earth (3D Audio Globe):** [https://spacejourney.app/earth/](https://spacejourney.app/earth/)  
**Sensory Copilot (AI Guide):** [https://spacejourney.app/en/ai-journey-assistant/](https://spacejourney.app/en/ai-journey-assistant/)

---

## 📌 Dataset Summary

The **London Sensory Impact Dataset (SIS v1.1)** is an independent, open-access urban benchmark recording quantitative acoustic, luminous, crowd-density, and satellite elevation telemetry across **15 verified contemplative sanctuaries, botanical ruins, canal corridors, and historic monuments** in London, United Kingdom.

Aligned with the **Rome (`01_rome`)**, **Paris (`02_paris`)**, and **Mexico City (`03_cdmx`)** open benchmarks, this catalog maps London's acoustic and topographic contrasts across the Thames basin — from the `25 dB` dawn stillness of **Primrose Hill** (`55.0 m` elevation, SIS `97/100`) and the `30 dB` waterfall resonance of **Kyoto Garden** in Holland Park, to Solarpunk architectural refuges inside the financial core such as **St Dunstan in the East** (`45 dB`) and the **Barbican Conservatory** (`40 dB`, SIS `97/100`).

- **Mean Sensory Impact Score (SIS):** `92.3 / 100`
- **Mean Ambient Acoustic Level:** `43.9 dB`
- **WHO Environmental Noise Compliance (`≤ 53 dB Lden`):** `13 / 15` sanctuaries (with dawn/twilight mitigation windows for high-traffic Thames & Westminster corridors)
- **Topographic Reference:** **ESA Copernicus DEM GLO-90** (`11.0 m` Greater London Thames basin baseline; range `1.0 m` to `55.0 m`)

---

## 📊 Dataset Structure & Features

The dataset is published in canonical structured JSON (`data/london_sensory_impact_sis_v1.json`) and tabular CSV (`data/london_sensory_impact_sis_v1.csv`), with backwards-compatible mirrors (`data/londres_sensory_dataset_v1.{csv,json}`) for legacy consumers.

| Feature | Type | Description | Example |
| :--- | :---: | :--- | :--- |
| `id` | string | Unique tier node identifier (`L` = Free Restorative, `S` = Secret Sanctuary, `P` = Curated Premium) | `"L-02"` |
| `haven_id` | string | Space Journey global registry identifier | `"LON-2821"` |
| `wp_id` | int | Production CMS reference ID | `2821` |
| `name` | string | Verified English experience title | `"Primrose Hill \| London skyline"` |
| `name_es` | string | Verified Spanish experience title | `"Primrose Hill \| El horizonte de Londres"` |
| `category` | string | Curation tier (`Free Restorative`, `Secret Sanctuary`, `Curated Premium`) | `"Free Restorative"` |
| `city` | string | Metropolitan destination | `"London"` |
| `neighborhood` | string | London borough or historic district | `"Primrose Hill (Camden, North London)"` |
| `latitude` | float | Decimal WGS84 latitude | `51.539` |
| `longitude` | float | Decimal WGS84 longitude | `-0.16` |
| `sis_score` | int | Continuous Sensory Impact Score (`0–100`, where `100` = peak restorative calm) | `97` |
| `acoustic_noise_db` | int | Ambient sound pressure level in A-weighted decibels (`dB`) | `25` |
| `golden_hour_window` | string | Optimal solar lighting & low-friction visiting window | `"06:00 - 07:30 GMT/BST"` |
| `light_level_lux` | int | Ambient luminous flux under optimal window (`Lux`) | `2400` |
| `light_atmosphere` | string | Qualitative photic signature of the space | `"Natural / Panoramic view"` |
| `duration_minutes` | int | Calibrated contemplative visit duration (minutes) | `90` |
| `ideal_season` | string | Recommended seasonal window | `"Spring / Autumn"` |
| `energy_cost_score` | int | Discrete physical exertion rating (`1` = Minimal/Flat, `5` = High fatigue) | `2` |
| `crowd_density_index` | float | Pedestrian congestion index (`0.00` = Solitary sanctuary, `1.00` = Acute crowding) | `0.06` |
| `elevation_m` | float | Satellite ground elevation above sea level (`m`, ESA Copernicus DEM GLO-90) | `55.0` |
| `city_baseline_m` | float | Greater London Thames basin reference elevation (`11.0 m`) | `11.0` |
| `relative_relief_m` | float | Elevation delta vs. city baseline (`elevation_m - 11.0`) | `44.0` |
| `biomechanical_exertion_index` | float | Continuous topographic & duration exertion score $P_{\text{exertion}}$ (`5.0–95.0`) | `47.7` |
| `topographic_profile` | string | Walkability grade classification (`<2%`, `2–5%`, `>6%`) | `"Panoramic Hill Ascent (>6% grade)"` |
| `dem_source` | string | Digital Elevation Model attribution | `"ESA Copernicus DEM GLO-90"` |
| `canonical_url` | string | Verified live English sanctuary guide on Space Journey | `"https://spacejourney.app/en/experiencia/primrose-hill-london-skyline/"` |
| `canonical_url_es` | string | Verified live Spanish sanctuary guide on Space Journey | `"https://spacejourney.app/experiencia/primrose-hill-londres-amanecer-mirador-secreto/"` |
| `description` | string | Qualitative architectural and contemplative narrative | `"There is an exact moment, just as the sun breaks the horizon..."` |
| `golden_spot_tips` | string | Micro-location vantage point for optimal sensory stillness | `"Stand 3 meters south of the summit triangulation pole..."` |

---

## 🏛️ Master Catalog: 15 Verified London Sanctuaries

### 🌿 Free Restorative (5 Nodes)
* **L-01 | [Sky Garden](https://spacejourney.app/en/experiencia/sky-garden-the-forest-in-the-clouds/) (`45 dB` · SIS `90` · `40.0 m` DEM):** Elevated botanical canopy high above Fenchurch Street's financial towers with panoramic Thames twilight views.
* **L-02 | [Primrose Hill](https://spacejourney.app/en/experiencia/primrose-hill-london-skyline/) (`25 dB` · SIS `97` · `55.0 m` DEM):** Protected dawn skyline viewpoint over Regent's Park and Central London with London's quietest acoustic baseline.
* **L-03 | [St Dunstan in the East](https://spacejourney.app/en/experiencia/st-dunstan-in-the-east-the-garden-among-the-ruins/) (`45 dB` · SIS `93` · `26.0 m` DEM):** Christopher Wren Gothic church ruins reclaimed by climbing ivy, palms, and fountain acoustics in the Square Mile.
* **L-04 | [Little Venice](https://spacejourney.app/en/experiencia/little-venice-the-quietest-walk-through-londons-canals/) (`45 dB` · SIS `93` · `31.0 m` DEM):** Willow-shaded confluence of the Grand Union and Regent's Canals with narrowboat reflections and slow towpath rhythm.
* **L-05 | [Kyoto Garden](https://spacejourney.app/en/experiencia/kyoto-garden-the-japanese-garden-in-london/) (`30 dB` · SIS `97` · `37.0 m` DEM):** Traditional Japanese rock waterfall, koi pond, and maple canopy tucked inside Holland Park.

### 🗝️ Secret Sanctuary (5 Nodes)
* **S-01 | [Leadenhall Market at 6:00 AM](https://spacejourney.app/en/experiencia/leadenhall-market-diagon-alley-at-600-am/) (`40 dB` · SIS `94` · `40.0 m` DEM):** Ornate Victorian wrought-iron and glass arcade experienced in near-total stillness before the City wakes.
* **S-02 | [BAPS Shri Swaminarayan Mandir](https://spacejourney.app/en/experiencia/baps-shri-swaminarayan-mandir-the-hidden-hindu-temple/) (`30 dB` · SIS `94` · `34.0 m` DEM):** Hand-carved Italian Carrara marble and Bulgarian limestone sanctuary in Neasden offering profound indoor acoustic stillness.
* **S-03 | [St Katharine Docks](https://spacejourney.app/en/experiencia/st-katharine-docks-the-secret-port-of-tower-bridge/) (`50 dB` · SIS `92` · `6.0 m` DEM):** Historic enclosed marina beside Tower Bridge shielding travelers from arterial riverfront crowds.
* **S-04 | [Barbican Conservatory](https://spacejourney.app/en/experiencia/barbican-conservatory-londons-solarpunk-oasis/) (`40 dB` · SIS `97` · `30.0 m` DEM):** Brutalist concrete architecture reclaimed by over 2,000 tropical plant species and tranquil koi ponds under diffused glass light.
* **S-05 | [The Queen's Walk](https://spacejourney.app/en/experiencia/the-queens-walk-thames-walk/) (`65 dB` · SIS `85` · `1.0 m` DEM):** Flat Thameside cultural promenade from Westminster to Millennium Bridge calibrated for autumn/winter golden-hour light.

### ✨ Curated Premium (5 Nodes)
* **P-01 | [Tower of London (First Access & Keys)](https://spacejourney.app/en/experiencia/tower-of-london-first-access-protocol-and-key-ceremony/) (`48 dB` · SIS `89` · `19.0 m` DEM):** Opening-bell fortress entry and 700-year-old Ceremony of the Keys protocol minimizing crowd friction.
* **P-02 | [Cutty Sark](https://spacejourney.app/en/experiencia/cutty-sark-the-copper-giant-under-the-glass/) (`45 dB` · SIS `93` · `5.0 m` DEM):** Suspended 1869 tea clipper hull in Greenwich Dry Dock bathed in glass-filtered zenith light.
* **P-03 | [Westminster Abbey (Verger Tour)](https://spacejourney.app/en/experiencia/westminster-abbey-the-whisper-of-history-in-stone-verger-tour/) (`55 dB` · SIS `88` · `10.0 m` DEM):** Intimate small-group Verger access to the Shrine of St Edward the Confessor and Gothic chapels.
* **P-04 | [Kensington Palace](https://spacejourney.app/en/experiencia/kensington-palace-the-garden-of-royal-memories/) (`45 dB` · SIS `93` · `29.0 m` DEM):** Red-brick royal chambers paired with the Sunken Garden and Round Pond sunset reflection.
* **P-05 | [Churchill War Rooms](https://spacejourney.app/en/experiencia/churchill-war-rooms-the-freedom-bunker/) (`50 dB` · SIS `89` · `8.0 m` DEM):** Preserved 1945 Whitehall subterranean Map Room experienced during the low-density `09:30` opening slot.

---

## 🔬 Methodology: SIS & ESA Copernicus DEM GLO-90

The **Sensory Impact Score (SIS)** evaluates restorative urban quality on a continuous `0–100` scale:

$$\text{SIS} = 100 - \left( 0.35 \cdot P_{\text{noise}}(dB) + 0.30 \cdot P_{\text{crowd}}(\rho) + 0.20 \cdot P_{\text{exertion}}(E) - 0.15 \cdot B_{\text{light}}(\text{lx}, \theta_{\odot}) \right)$$

Where:
* **$P_{\text{noise}}(dB)$ (Weight: 35%):** Acoustic sound pressure anchored against the **World Health Organization (WHO) 53 dB Lden** environmental guideline (`< 40 dB` = Deep Restorative Sanctuary, `40–50 dB` = Contemplation Zone, `> 53 dB` = Urban Corridor mitigated by dawn/twilight windows).
* **$P_{\text{crowd}}(\rho)$ (Weight: 30%):** Pedestrian congestion index (`0.00` = solitary stillness to `1.00` = mass crowding).
* **$P_{\text{exertion}}(E)$ (Weight: 20%):** Biomechanical exertion index computed deterministically from **ESA Copernicus DEM GLO-90** elevation (`elevation_m`), London's Thames basin baseline (`11.0 m`), and visit duration:
  $$P_{\text{exertion}} = \operatorname{clip}\!\left(\min\!\left(|\Delta h| \cdot 0.8,\; 60\right) + \min\!\left(\frac{\text{duration}_{\min}}{180} \cdot 25,\; 35\right),\; 5.0,\; 95.0\right)$$
* **$B_{\text{light}}(\text{lx}, \theta_{\odot})$ (Weight: 15%):** Photic harmony bonus rewarding glare-free golden hour and architectural skylight irradiance (`1,800–3,200 Lux`).

---

## 💻 Quickstart & Reproducibility

### 1. Interactive Google Colab (One-Click Live Execution)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/spacelabdevteam-hub/sensory-impact-score-datasets/blob/main/cities/03_london/explore_london_sensory_impact.ipynb)

### 2. Hugging Face (`datasets` library)
```python
from datasets import load_dataset

dataset = load_dataset(
    "spacejourney/london-sensory-impact-dataset",
    data_files="data/london_sensory_impact_sis_v1.csv",
)
df = dataset["train"].to_pandas()
print(df[["id", "name", "sis_score", "acoustic_noise_db", "elevation_m"]].head())
```

### 3. Python (Pandas — Direct GitHub Mirror)
```python
import pandas as pd

url = "https://raw.githubusercontent.com/spacelabdevteam-hub/sensory-impact-score-datasets/main/cities/03_london/data/london_sensory_impact_sis_v1.csv"
df = pd.read_csv(url)

# Filter Deep Restorative Sanctuaries (Acoustic Noise <= 40 dB)
quiet_london = df[df["acoustic_noise_db"] <= 40]
print(quiet_london[["id", "name", "acoustic_noise_db", "sis_score", "elevation_m"]])
```

### 4. DuckDB (Serverless SQL via Hugging Face Hub)
```sql
SELECT id, name, category, sis_score, acoustic_noise_db, elevation_m, golden_hour_window
FROM 'hf://datasets/spacejourney/london-sensory-impact-dataset/data/london_sensory_impact_sis_v1.csv'
ORDER BY sis_score DESC, acoustic_noise_db ASC;
```

### 5. Automated Schema & Scientific Validation (Zero Dependencies)
```bash
python cities/03_london/validate_london_dataset.py
```

---

## 🌐 Project Ecosystem & Live Implementations

* **London City Guide (English):** [https://spacejourney.app/en/city/london/](https://spacejourney.app/en/city/london/) *(also in [Español](https://spacejourney.app/ciudad/londres/))*
* **Global Sensory Itinerary Planner:** [https://spacejourney.app/en/itinerary-planner/](https://spacejourney.app/en/itinerary-planner/)
* **Sensory Earth (3D Audio & Atmosphere Globe):** [https://spacejourney.app/earth/](https://spacejourney.app/earth/)
* **Sensory Copilot (AI Guide):** [https://spacejourney.app/en/ai-journey-assistant/](https://spacejourney.app/en/ai-journey-assistant/)
* **Open Science Archive (CERN Zenodo):** [https://doi.org/10.5281/zenodo.22756473](https://doi.org/10.5281/zenodo.22756473)
* **Knowledge Graph (Wikidata):** [https://www.wikidata.org/wiki/Q141455396](https://www.wikidata.org/wiki/Q141455396)
* **Official Website:** [https://spacejourney.app/](https://spacejourney.app/)

---

## 📜 Academic Citation & Attribution (BibTeX)

If you use the London SIS dataset or methodology in academic research, open urban mobility tools, or AI evaluation benchmarks, please cite:

```bibtex
@dataset{duque_romero_2026_zenodo_22756473,
  author       = {Duque Romero, Daniel Adolfo and {Space Journey Studio}},
  title        = {London Sensory Impact & Acoustic Heritage Dataset (SIS v1.1)},
  year         = {2026},
  month        = nov,
  publisher    = {Zenodo},
  version      = {1.1.0},
  doi          = {10.5281/zenodo.22756473},
  url          = {https://doi.org/10.5281/zenodo.22756473}
}
```

Or cite the Hugging Face Hub repository:

```bibtex
@misc{spacejourney_london_hf_2026,
  author       = {Duque Romero, Daniel Adolfo},
  title        = {London Sensory Impact & Acoustic Heritage Dataset (SIS v1.1)},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/spacejourney/london-sensory-impact-dataset}}
}
```
