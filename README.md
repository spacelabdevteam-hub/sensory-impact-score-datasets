# 🌍 Space Journey — Open Sensory Impact Score (SIS) City Datasets (Rome, Paris & CDMX)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22756473.svg)](https://doi.org/10.5281/zenodo.22756473)
[![WHO Acoustic Guideline](https://img.shields.io/badge/WHO_Guideline-53_dB_Lden-006699)](https://spacejourney.app/standards/sensory-impact-score/)
[![Hugging Face Organization](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-spacejourney-FFD21E)](https://huggingface.co/spacejourney)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC--BY--4.0-10B981)](https://creativecommons.org/licenses/by/4.0/)

> **Open-Access Acoustic ($\text{dB}$), Photic ($\text{lx}$), and Crowd-Density ($\rho$) Urban Benchmarks for Contemplative Human Mobility.**  
> *Curated by [Space Journey](https://spacejourney.app/) & Cited via CERN Zenodo ([`10.5281/zenodo.22756473`](https://doi.org/10.5281/zenodo.22756473)).*

---

## 🏛️ Active City Benchmarks in This Repository (Phase 1 — Europe & LATAM)

This repository consolidates our peer-cited tabular datasets (`.csv`, `.json`, and Jupyter Notebooks) synchronized with the [**Space Journey Hugging Face Hub (`huggingface.co/spacejourney`)**](https://huggingface.co/spacejourney):

| City Benchmark | Repository Folder | Hugging Face Parquet / Viewer Hub | Live City Portal |
| :--- | :--- | :--- | :--- |
| 🇮🇹 **Rome, Italy** | [`cities/01_rome/`](./cities/01_rome/) | [`spacejourney/rome-sensory-impact-dataset`](https://huggingface.co/datasets/spacejourney/rome-sensory-impact-dataset) | [Rome Guide](https://spacejourney.app/ciudad/roma/) |
| 🇫🇷 **Paris, France** | [`cities/02_paris/`](./cities/02_paris/) | [`spacejourney/paris-sensory-impact-dataset`](https://huggingface.co/datasets/spacejourney/paris-sensory-impact-dataset) | [Paris Guide](https://spacejourney.app/ciudad/paris/) |
| 🇲🇽 **Mexico City (CDMX)** | [`cities/03_cdmx/`](./cities/03_cdmx/) | [`spacejourney/cdmx-sensory-impact-dataset`](https://huggingface.co/datasets/spacejourney/cdmx-sensory-impact-dataset) | [CDMX Guide](https://spacejourney.app/ciudad/cdmx/) |
| 🌐 **Global Index (v3.0)** | [MCP Engine Repo](https://github.com/spacelabdevteam-hub/space-journey-mcp-engine) | [`spacejourney/global-sensory-impact-benchmark`](https://huggingface.co/datasets/spacejourney/global-sensory-impact-benchmark) | [SIS Standard](https://spacejourney.app/standards/sensory-impact-score/) |

*(Note: Phase 2 city benchmarks are released incrementally following our open research cadence).*

---

## 🔗 Live Ecosystem & Tools

- **Model Context Protocol (MCP) Server:** [`spacelabdevteam-hub/space-journey-mcp-engine`](https://github.com/spacelabdevteam-hub/space-journey-mcp-engine) (`https://mcp.spacelab.network/mcp`)
- **The Sensory Atlas (3D WebGL Playable):** [`spacelabdevteam-hub/the-sensory-atlas-prototype`](https://github.com/spacelabdevteam-hub/the-sensory-atlas-prototype) ([Live Demo](https://spacejourney.app/play/roma-atlas/))
- **Interactive Itinerary Planner:** [https://spacejourney.app/planificador-de-viajes/](https://spacejourney.app/planificador-de-viajes/)
- **Sensory Earth 3D Globe (227 Countries):** [https://spacejourney.app/sensory-earth/](https://spacejourney.app/sensory-earth/)

---

## 📜 Citation (CC-BY-4.0)

```bibtex
@dataset{duque_romero_2026_sis,
  author       = {Duque Romero, Adolfo Daniel and {Space Journey Research Lab}},
  title        = {{The Sensory Impact Score (SIS): An Open Acoustic, Photic, and Crowd-Density Benchmark for Contemplative Urban Mobility}},
  year         = 2026,
  publisher    = {Zenodo / CERN},
  version      = {3.0.0},
  doi          = {10.5281/zenodo.22756473},
  url          = {https://doi.org/10.5281/zenodo.22756473}
}
```
