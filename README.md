# Defectra 🔍

**AI-Powered Industrial Quality Inspection & Anomaly Detection Platform**

Defectra is a portfolio-grade AI engineering platform that uses computer vision and deep learning to detect product anomalies, generate defect heatmaps, and provide quality inspection analytics through a professional web dashboard.

---

## Project Status

> 🚧 **Phase 01 – Project Foundation** (In Progress)

| Phase | Description | Status |
|-------|-------------|--------|
| 01 | Project Foundation | 🔄 In Progress |
| 02 | Dataset Engineering | ⏳ Pending |
| 03 | Autoencoder Baseline | ⏳ Pending |
| 04 | PatchCore Main Model | ⏳ Pending |
| 05 | DINOv2 Experiments | ⏳ Pending |
| 06 | Backend Development | ⏳ Pending |
| 07 | Frontend Development | ⏳ Pending |
| 08 | MLOps Integration | ⏳ Pending |
| 09 | Cloud Deployment | ⏳ Pending |
| 10 | Testing & Documentation | ⏳ Pending |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| AI / CV | PyTorch, Anomalib, DINOv2, OpenCV |
| Backend | FastAPI, PostgreSQL, SQLAlchemy |
| Frontend | Next.js, TypeScript, Tailwind CSS |
| MLOps | MLflow, DVC, Docker, GitHub Actions |
| Cloud | AWS S3, EC2, CloudWatch |

---

## Project Structure

```
Defectra/
├── apps/
│   ├── backend/          # FastAPI backend
│   └── frontend/         # Next.js frontend
├── ml/
│   ├── data/             # Data pipelines
│   ├── models/           # Model implementations
│   ├── training/         # Training scripts
│   ├── evaluation/       # Evaluation scripts
│   └── inference/        # Inference engine
├── configs/              # Configuration files
├── notebooks/            # Research notebooks
├── infrastructure/       # Docker & AWS configs
└── docs/                 # Documentation
```

---

## Quick Start

```bash
# Clone repository
git clone https://github.com/BuddhiDihansa/Defectra.git
cd Defectra

# Create virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## Dataset

This project uses the [MVTec Anomaly Detection Dataset](https://www.mvtec.com/company/research/datasets/mvtec-ad).

> ⚠️ **License:** CC BY-NC-SA 4.0 — Non-commercial research use only.

---

## Author

**BuddhiDihansa** — AI Engineering Portfolio Project

---

## License

MIT License — See [LICENSE](LICENSE) for details.