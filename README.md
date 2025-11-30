# **Khmer Orthographic Correction System (KOCS)**

### _PrahokBART: Specialized Khmer Sequence-to-Sequence Model for Noise-Robust Text Correction_

---

## 🌐 **Project Overview**

This repository contains the full pipeline for building the **Khmer Orthographic Correction System (KOCS)** — an open-source effort to solve real-world Khmer text noise, including **spacing errors**, **spelling mistakes**, and **phonetic confusions**. The system is powered by **PrahokBART**, a Khmer-specialized sequence-to-sequence model trained from scratch to handle noisy inputs from OCR, social media, and messaging platforms.

The project also includes a **prompt-engineering-based evaluation framework** to compare KOCS against large models (GPT-4o, Claude) in a controlled, structured format.

| Quick Start                                                                                       | Training                                                                       |
| :------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------- |
| **[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](YOUR_COLAB_LINK)** | [`scripts/training/train_prahokbart.py`](scripts/training/train_prahokbart.py) |

---

## 💡 **Why This Project Matters**

Khmer text processing faces a critical bottleneck: **noise**. With no mandatory spaces and high variation in typing practices, Khmer digital text often contains:

### 1. **Segmentation Errors (Most Common)**

Spaces are frequently omitted in Khmer social media and OCR, making word boundary detection difficult and inconsistent.

### 2. **Spelling Errors**

Typists often confuse:

- A-series vs O-series consonants
- Vowel diacritics
- Subscripts and dependent signs

Error probability can reach **20–30%** in fast typing contexts.

➡️ **Our scope** focuses _exclusively_ on correcting **spacing + spelling**.

---

## 🧠 **Methodology: PrahokBART & Linguistic Pre-Training**

### **Model Architecture**

- Built using the **BART** sequence-to-sequence design.
- Pretrained _from scratch_ using Khmer-specific segmentation.
- Tuned for denoising: input = noisy text, output = corrected text.

### **Key Linguistic Advantages**

- Vocabulary tokens follow **linguistically motivated segmentation**, unlike mBART50.
- Better handling of:

  - Homophones
  - Khmer morphology
  - Subscripts & diacritics
  - Real-world Khmer misspellings

### **Correction Pipeline**

1. Input text is normalized
2. Noisy tokens are mapped to clean Khmer sequences
3. Output is evaluated using CER or matched against LLM JSON outputs (for cross-model comparisons)

---

## 🧪 **Data Generation & Evaluation**

### 🔧 **Synthetic Data Generation (100k+ pairs)**

We generate (Noisy_X → Corrected_Y) pairs using linguistically informed error maps:

| Error Type                                         | Probability         | Description                                                         |
| -------------------------------------------------- | ------------------- | ------------------------------------------------------------------- |
| **Spacing Deletion** (`STRUCTURAL_MAP`)            | **~30%**            | Mirrors real Khmer typing patterns—missing spaces are the #1 issue. |
| **Phonetic Confusions** (`PHONETIC_CONFUSION_MAP`) | **10–15%** per char | Handles sound-alike swaps (e.g., ា vs ឲ, s-series vs k-series).     |
| **Diacritic/Subscript Omission**                   | **20–30%**          | Common in fast smartphone typing.                                   |

### 📏 **Evaluation Framework**

1. **Baseline Model Comparison**

   - Baseline: **mBART50**
   - Metric: **Character Error Rate (CER)** only

2. **LLM Evaluation: Prompt Engineering**
   LLMs (GPT-4o, Claude) are queried using:

   - A fixed **structured JSON prompt**
   - Deterministic formatting for reproducible comparisons
   - API-based batch evaluation scripts

This allows clean statistical comparisons between:

- PrahokBART
- Baseline models
- Proprietary LLMs

---

## 📂 **Repository Structure**

```
khmer-kocs-prahokbart/
├── data/
│   ├── raw/                  # Clean Khmer corpora
│   ├── ground_truth/         # Manually segmented evaluation sets
│   └── synthetic_data/       # (Noisy_X, Corrected_Y) pairs
│
├── scripts/
│   ├── data_generation/
│   │   ├── error_injection.py
│   │   ├── phonetic_map.py
│   │   └── structural_map.py
│   ├── training/
│   │   └── train_prahokbart.py
│   └── evaluation/
│       ├── evaluate_hf.py
│       └── evaluate_llm_api.py
│
├── notebooks/
│   ├── 01_Data_Exploration.ipynb
│   ├── 02_PrahokBART_Quickstart.ipynb   # Recommended Colab
│   └── 03_LLM_Prompt_Testing.ipynb
│
├── models/
│   └── checkpoints/
│
├── README.md
└── requirements.txt
```

---

## 🚀 **Installation**

```bash
git clone https://github.com/YOUR_USERNAME/khmer-kocs-prahokbart.git
cd khmer-kocs-prahokbart
pip install -r requirements.txt
```

---

## ▶️ **Quickstart Example**

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("prahokbart")
model = AutoModelForSeq2SeqLM.from_pretrained("prahokbart")

noisy_text = "ខ្ញុំពិតជាស្រលាញ់អ្នាក់"
inputs = tokenizer(noisy_text, return_tensors="pt")

outputs = model.generate(**inputs)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## 🔗 **Colab Notebook**

A full quickstart tutorial is available:

**[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](YOUR_COLAB_LINK)**

---

## 🤝 **Contributing**

Contributions are welcome!
You can contribute via:

- New error maps
- Dataset improvements
- New evaluation scripts
- Better prompt engineering for LLM evaluation

Please open an Issue or Pull Request.

---

## 📜 **License**

Choose one:

- MIT License
- Apache 2.0
- Creative Commons Attribution 4.0

(If you tell me which one you prefer, I’ll add the license file.)

---

## 📧 Contact

**Maintainer:** _Panha (Sethisak San)_
If you use this project in academic research, please cite and credit appropriately.
