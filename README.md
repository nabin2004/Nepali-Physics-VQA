# Nepali VQA: Physics Question Answering with Gemma3n

## Overview

Nepali VQA is a multimodal question answering system fine-tuned on Nepali physics visual question datasets using Google’s Gemma3n language model. The system supports input queries that include both text prompts and images (e.g., physics diagrams), and returns accurate, context-aware answers in Nepali.

The project focuses on supervised fine-tuning (SFT) of the Gemma3n model on (prompt + image + answer) pairs, enabling multimodal reasoning specific to physics concepts. The final model is served via an interactive web interface designed for student use.

---

## Architecture

- **Model Backbone:** Gemma3n — a smaller-scale, efficient LLM from Google, fine-tuned with QLoRA or PEFT techniques.
- **Dataset:** Nepali-translated and curated visual question-answer pairs from ScienceQA and Textbook Question Answering (TQA).
- **Multimodal Inputs:** Combines text and image embeddings for comprehensive understanding.
- **Backend:**  
  - Model serving API (FastAPI/Flask) interfacing with the fine-tuned Gemma3n.  
  - Translation and data augmentation pipelines leveraging AI provider APIs (e.g., Gemini).
- **Frontend:**  
  - Web UI built with React or Streamlit for interactive Q&A sessions.  
  - Supports image uploads and conversational input.

---

## Key Features

- **Fine-tuned Multimodal LLM:** Handles physics problems involving diagrams and text in Nepali.
- **Supervised Fine-Tuning:** Utilizes domain-specific (prompt + image + answer) training samples.
- **Interactive Web Interface:** User-friendly chat interface tailored for students.
- **Scalable Deployment:** Compatible with GPU-enabled servers (e.g., RTX 4090) for model inference.
- **Extensible:** Designed to support additional subjects beyond physics with minimal retraining.

---

## Data Preparation

- Data consists of (prompt + image, answer) pairs.  
- English datasets (ScienceQA, TQA) translated to Nepali using AI translation APIs and manual verification.  
- Preprocessing includes image normalization, tokenization, and formatting for Gemma3n multimodal input.  
- Dataset quality and translation accuracy critical for domain-specific terminology.

---

## Training & Fine-tuning

- Leveraging parameter-efficient fine-tuning methods (e.g., QLoRA) to reduce hardware requirements.  
- Training done on RTX 4090 GPU with mixed precision for efficiency.  
- Evaluation metrics: Exact match accuracy, BLEU/ROUGE for descriptive answers, human expert validation.

---

## Deployment

- Model served via RESTful API with endpoints for inference requests.  
- Frontend communicates with backend API for query submission and result retrieval.  
- MongoDB or similar database for storing conversation histories and analytics (optional).  
- Planned support for multi-turn conversations and student progress tracking.

---

## How to Run

> *Instructions to run training scripts, launch API server, and start frontend UI will be provided once the prototype is ready.*

---

## Team

- Nabin Oli  
- Niraj Karki  
- Kusumm Maharjan  
- Pariskar Poudel  

---

## Requirements

- Python 3.10+  
- PyTorch, Hugging Face Transformers, PEFT  
- FastAPI or Flask for serving  
- React or Streamlit for frontend UI  
- RTX 4090 or equivalent GPU for fine-tuning and inference  
- Access to translation APIs (e.g., Gemini)

---

## Future Work

- Add multi-turn conversational capabilities.  
- Implement student progress and analytics dashboard.  
- Expand dataset coverage to other STEM subjects.

---

## Contact

For collaboration or technical inquiries, please reach out to the team via GitHub or email.

