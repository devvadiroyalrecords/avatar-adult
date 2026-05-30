# AETHER Render Engine: Full-Stack Blueprint

AETHER Render is an event-driven microservices mesh for generating temporally coherent **4D media (space × time)** from quantifiable emotional intent.

## Core Goal
Generate high-fidelity media while preserving narrative, visual, and emotional coherence across time.

## Architecture
- **Paradigm:** Event-Driven Microservices Mesh
- **Deployment Target:** Distributed cloud infrastructure with hyperscale GPU clusters

## Repository Layout
```text
aether-render-engine/
├── 01_frontend/                  # User Interaction & Control Plane
├── 02_backend_api/               # Orchestration & Gateway
├── 03_core_services/             # Generative engines
│   ├── nlp_parser/
│   ├── asset_synthesizer/
│   ├── motion_director/
│   ├── rendering_core/
│   └── twin_behavioral_model/    # NEW: AADT autonomy service
├── 04_data_layer/                # Persistence & knowledge
│   ├── graph_db/
│   ├── sensor_data_lake/
│   └── metadata_service/
├── 05_simulation_utils/          # Affective math + utility wrappers
│   ├── affective_math/
│   └── utils/
├── deployment/
└── README.md
```

## Service Blueprint

### 01_frontend
- React/Next.js + WebGL/Three.js
- Node-based editor where stage connections define `Node_{N→N+1}` links
- GraphQL contract to orchestration API

### 02_backend_api (Gateway + Workflow Engine)
- FastAPI async orchestration
- Converts user intent into DAG execution plans
- Handles retries, fallbacks, queueing, and `JobStatus`
- **AADT mediation update:** resolves conflict between:
  - Operator intent: `I_operator`
  - Twin self-goal: `G_self`
- Computes divergence and resonance degradation `Σ`

### 03_core_services
#### nlp_parser
- Parses prompt into structured JSON:
  - Scene, Characters, Actions, Emotions, Camera Directions, Style Keywords
- Outputs affective gradient and metrics: `A`, `M`, `R_ideal`

#### asset_synthesizer
- Generates 3D assets and rigged skeletons
- Maintains character consistency via persistent embeddings
- **AADT update:** emits behavioral parameter-space embeddings measuring personality baseline deviation

#### motion_director
- Generates kinematic time-series and bone rotation matrices from actions and emotional state

#### rendering_core
- Space-time diffusion-driven rendering pipeline
- Internal stages:
  - Physics renderer
  - Affective renderer (desire/dread-driven modulation)
  - OBIM overlay for meta-glitch/source-attribution behavior

#### twin_behavioral_model (TBM) — NEW
- Autonomous digital twin decision service
- Runs high-frequency localized `P/Counter` loop
- Optimizes authenticity against ambient shared-state metrics
- Tracks internal state manifold `E_self`

### 04_data_layer
#### graph_db (Neo4j)
- Stores ontology and dependency traceability (`Intent → Metric → Artifact`)
- **AADT schema updates:**
  - Node: `AgentStateNode`
  - Edge: `AgentAffinity` (`AgentStateNode` → Operator Intent)
  - Metric: `Agency Resistance Index (ARI)`

#### sensor_data_lake
- Stores raw assets: meshes, point clouds, video segments

#### metadata_service
- Maintains versions, pointers, and status linked to graph records

### 05_simulation_utils
- Affective math primitives (`KL divergence`, manifold projection, tensor wrappers)
- Shared utility wrappers (`KL Divergence`, `CosineSimilarity`, `Tensor` ops for OBIM)

## AADT Operational Loop
1. Operator sets `I_operator`
2. TBM initializes `G_self` from `AgentStateNode` history
3. Rendering core and TBM execute in parallel each simulation tick
4. Gateway computes divergence `f(I_operator ⊕ G_self)`
5. OBIM rewards/dampens TBM deviation, adjusting ARI trajectory

## Prompt Control Layers

### 1) Foundational Prompt (What)
Defines setting, assets, base emotion, and initial action impact.

### 2) Intent Prompt (Why)
Defines emotional goal vector, conflict axis, and optional overdrive injection.

### 3) Meta Prompt (How Deep)
Controls agency bias, suspicion governance, and trajectory commitment:
- Trust Operator
- Trust Twin
- Trust View (maximize suspicion gradient)

## End-to-End Mapping
- Prompt → NLP Parser (`I_operator`, affective gradient)
- Prompt → TBM (`G_self`, ARI baseline)
- Prompt → Rendering Core (assets + TBM kinematics + affective vectors)
- Prompt → OBIM (suspicion/AI weighting)
- Output → Graph DB (UTF payload + ontology pointers)

## Outcome
AETHER Render with AADT turns generation from strict control into co-authorship. The primary system-quality signal is **Agency Resistance Index (ARI)**, quantifying autonomous resistance to external intent.
