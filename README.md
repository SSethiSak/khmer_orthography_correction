# **Khmer Orthographic Correction System (KOCS)**

---

## 🌐 **Project Overview**

This repository contains the full pipeline for building the **Khmer Orthographic Correction System (KOCS)** — an open-source effort to solve real-world Khmer text noise, including **spacing errors**, **spelling mistakes**, and **phonetic confusions**. The system is powered by **PrahokBART**, a Khmer-specialized sequence-to-sequence model trained from scratch to handle noisy inputs from OCR, social media, and messaging platforms.

## 🔗 **Colab Notebook**

mBART Notebook: https://colab.research.google.com/drive/1McOajSM5o45u4g_HJnUfMEZhTe4jjZPx?usp=sharing 
PrahokBART Notebook: https://colab.research.google.com/drive/1h063DWgYBsrQrUI3I3gLhCYkEybS_UEZ?usp=sharing
NLLB Notebook: https://colab.research.google.com/drive/1Hl1d_x-sRtujbdQMnHkbxoBfORAhEnTO?usp=sharing

Evaluation of the 3 models: https://colab.research.google.com/drive/1OqbHn75Wr8GqeA1LPBJpnaCVZHnYB5AD?usp=sharing

Data Corruption Pipeline: https://colab.research.google.com/drive/1ZWp75Pthij9LlZA7P01YcB55YN4E2Wzk?usp=sharing

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




