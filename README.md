# 🌍 Space Journey — Open Sensory Impact Score (SIS) Benchmark Datasets (6 Global Cities & 94 Sanctuaries)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22756473.svg)](https://doi.org/10.5281/zenodo.22756473)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/spacelabdevteam-hub/sensory-impact-score-datasets/blob/main/explore_global_sensory_benchmark.ipynb)
[![WHO Acoustic Guideline](https://img.shields.io/badge/WHO_Guideline-53_dB_Lden-006699)](https://spacejourney.app/standards/sensory-impact-score/)
[![Hugging Face Organization](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-spacejourney-FFD21E)](https://huggingface.co/spacejourney)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC--BY--4.0-10B981)](https://creativecommons.org/licenses/by/4.0/)

> **Open-Access Acoustic (dB), Photic (lx), Topographic Elevation (ESA Copernicus DEM GLO-90), and Crowd-Density (pax/m²) Urban Benchmarks for Contemplative Human Mobility.**  
> *Curated by [Space Journey](https://spacejourney.app/) & Cited via CERN Zenodo ([10.5281/zenodo.22756473](https://doi.org/10.5281/zenodo.22756473)).*

---

## 🏛️ Active City Benchmarks (94 Curated Sanctuaries Across 6 Cities)

Each city benchmark includes verified `.csv` and `.json` datasets with **ESA Copernicus DEM GLO-90 satellite elevation**, relative relief, and the biomechanical exertion index ($P_{\text{exertion}}$):

| City Benchmark | GitHub Folder | Hugging Face Dataset | Sanctuaries | Live City Guide |
| :--- | :--- | :--- | :---: | :--- |
| 🌐 **Global Benchmark (94 Sanctuaries)** | [data/global_sensory_benchmark_v3.csv](./data/global_sensory_benchmark_v3.csv) | [global-sensory-impact-benchmark](https://huggingface.co/datasets/spacejourney/global-sensory-impact-benchmark) | **94** | [SIS Standard](https://spacejourney.app/standards/sensory-impact-score/) |
| 🇮🇹 **Rome, Italy** | [cities/01_rome/](./cities/01_rome/) | [rome-sensory-impact-dataset](https://huggingface.co/datasets/spacejourney/rome-sensory-impact-dataset) | **15** | [Rome Guide](https://spacejourney.app/ciudad/roma/) |
| 🇫🇷 **Paris, France** | [cities/02_paris/](./cities/02_paris/) | [paris-sensory-impact-dataset](https://huggingface.co/datasets/spacejourney/paris-sensory-impact-dataset) | **15** | [Paris Guide](https://spacejourney.app/ciudad/paris/) |
| 🇬🇧 **London, UK** | [cities/03_london/](./cities/03_london/) | [london-sensory-impact-dataset](https://huggingface.co/datasets/spacejourney/london-sensory-impact-dataset) | **15** | [London Guide](https://spacejourney.app/ciudad/londres/) |
| 🇲🇽 **Mexico City (CDMX)** | [cities/04_cdmx/](./cities/04_cdmx/) | [cdmx-sensory-impact-dataset](https://huggingface.co/datasets/spacejourney/cdmx-sensory-impact-dataset) | **15** | [CDMX Guide](https://spacejourney.app/ciudad/cdmx/) |
| 🇺🇸 **New York City, USA** | [cities/05_new_york/](./cities/05_new_york/) | [new-york-sensory-impact-dataset](https://huggingface.co/datasets/spacejourney/new-york-sensory-impact-dataset) | **17** | [New York Guide](https://spacejourney.app/ciudad/nueva-york/) |
| 🇺🇸 **Miami, USA** | [cities/06_miami/](./cities/06_miami/) | [miami-sensory-impact-dataset](https://huggingface.co/datasets/spacejourney/miami-sensory-impact-dataset) | **17** | [Miami Guide](https://spacejourney.app/ciudad/miami/) |

---

## 📐 Scientific Methodology: The Sensory Impact Score (SIS)

Defined in our open technical standard ([`/standards/sensory-impact-score/`](https://spacejourney.app/standards/sensory-impact-score/) & [CERN Zenodo DOI `10.5281/zenodo.22756473`](https://doi.org/10.5281/zenodo.22756473)), the **Sensory Impact Score (SIS 0–100)** quantifies the restorative quality of a cultural space:

$$\text{SIS} = 100 - \left( 0.35 \cdot P_{\text{noise}}(dB) + 0.30 \cdot P_{\text{crowd}}(\rho) + 0.20 \cdot P_{\text{exertion}}(E) - 0.15 \cdot B_{\text{light}}(\text{lx}, \theta_{\odot}) \right)$$

Where:
- **$P_{\text{noise}}(dB)$:** Non-linear acoustic penalty anchored to the **WHO 53 dB Lden** threshold.
- **$P_{\text{crowd}}(\rho)$:** Pedestrian density penalty (pax/m²) derived from hourly visitation curves.
- **$P_{\text{exertion}}(E)$:** Biomechanical and thermal friction index computed using **ESA Copernicus DEM GLO-90** satellite elevation (`elevation_m`, `relative_relief_m`).
- **$B_{\text{light}}(\text{lx}, \theta_{\odot})$:** Photic harmony bonus during golden hour and architectural twilight.

---

## 🔗 Live Ecosystem & Tools

- **Machine-Readable LLMs Manifest:** [https://spacejourney.app/llms.txt](https://spacejourney.app/llms.txt) & [llms-full.txt](https://spacejourney.app/llms-full.txt)
- **Model Context Protocol (MCP) Server:** [spacelabdevteam-hub/space-journey-mcp-engine](https://github.com/spacelabdevteam-hub/space-journey-mcp-engine) (`https://space-journey-engine.spacelab-mcp.workers.dev/mcp`)
- **The Sensory Atlas (3D WebGL Playable):** [spacelabdevteam-hub/the-sensory-atlas-prototype](https://github.com/spacelabdevteam-hub/the-sensory-atlas-prototype) ([Live Demo](https://spacejourney.app/play/roma-atlas/))
- **Interactive Itinerary Planner:** [https://spacejourney.app/planificador-de-viajes/](https://spacejourney.app/planificador-de-viajes/)
- **Sensory Earth 3D Globe (227 Countries):** [https://spacejourney.app/sensory-earth/](https://spacejourney.app/sensory-earth/)
