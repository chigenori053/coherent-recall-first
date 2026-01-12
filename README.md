# COHERENT: Recall-First Holographic Reasoning Foundation

> **Holographic Inference beyond the Generative AI paradigm.**
> *A minimal research prototype demonstrating the feasibility of Recall-First Cognitive Architecture.*
>
> **生成AIパラダイムを超える、ホログラフィック推論基盤。**
> *想起優先型（Recall-First）認知アーキテクチャの実現可能性を示す、最小限の研究プロトタイプ。*

---

## ⚠️ Disclaimer / 免責事項
**This repository is a minimal research prototype prepared for proposal evaluation.**
It does not represent the full system described in the project proposal. It is intended solely to demonstrate the core algorithmic principles of the "Recall-First" architecture.

**本リポジトリは、提案審査のために用意された最小限の研究プロトタイプです。**
本プロジェクト提案で記述されるシステム全体の機能を網羅するものではありません。「想起優先（Recall-First）」アーキテクチャの中核となるアルゴリズム原理を実証することのみを目的としています。

---

## 1. Project Abstract / プロジェクト概要

**Recent AI models generate "plausible" answers, but lack "certainty".**
The COHERENT project proposes a paradigm shift from **"Generation-First"** to **"Recall-First"**. By utilizing high-dimensional Holographic Memory (Hyperdimensional Computing) as the substrate for reasoning, we establish a system that "recalls" the correct path before "generating" an answer.

**昨今のAIモデルは「もっともらしい」回答を生成しますが、「確信」を欠いています。**
COHERENTプロジェクトは、**「生成優先（Generation-First）」**から**「想起優先（Recall-First）」**へのパラダイムシフトを提案します。高次元ホログラフィックメモリ（超次元計算）を推論の基盤として利用することで、回答を「生成」する前に正しい経路を「想起」するシステムを構築します。

This repository provides a proof-of-concept implementation of the core engine: **Holographic Recall Loop** and **Trinary Decision Logic**.

本リポジトリは、その中核エンジンである **「ホログラフィック想起ループ」** と **「三値判断ロジック」** の概念実証実装を提供します。

## 2. Core Philosophy / 中核思想

### 2.1 Generating is NOT Understanding
Current LLMs predict the next token based on probability. They do not distinctively separate "what they know" from "what they hallucinate".
**Recall-First** architecture ensures that decision-making is grounded in retrieved, high-resonance memory states.

**生成は理解ではありません**
現在のLLMは確率に基づいて次のトークンを予測します。彼らは「知っていること」と「幻覚（ハルシネーション）」を明確に区別していません。
**想起優先（Recall-First）**アーキテクチャは、意思決定が高共鳴な（強く想起された）記憶状態に基づいていることを保証します。

### 2.2 Holographic Memory as the Substrate
We use **Holographic Reduced Representations (HRR)** with complex-valued vectors.
*   **Superposition**: Storing multiple concepts without growing memory size.
*   **Interference**: Constructive interference implies "familiarity"; destructive interference implies "novelty".
*   **Resonance**: The intensity of the memory response guides the reasoning process.

**基盤としてのホログラフィックメモリ**
複素数ベクトルを用いた**ホログラフィック縮約表現（HRR）**を採用しています。
*   **重ね合わせ（Superposition）**: メモリサイズを増大させずに複数の概念を保存します。
*   **干渉（Interference）**: 強め合う干渉は「既知」を、弱め合う干渉は「新規性」を意味します。
*   **共鳴（Resonance）**: メモリ応答の強度が推論プロセスを導きます。

### 2.3 Trinary Decision Logic (The "Halt" Problem)
Unlike binary logic (True/False), our system employs Trinary Logic to handle ambiguity:
1.  **ACCEPT (Recall)**: Strong resonance found. Confidence is high.
2.  **REJECT (Error)**: Contradiction detected.
3.  **REVIEW (Uncertain)**: Weak resonance. Requires further observation or hypothesis generation (Abductive Reasoning).

**三値判断ロジック（停止問題へのアプローチ）**
二値論理（真/偽）とは異なり、曖昧性に対処するために三値論理を採用しています：
1.  **ACCEPT (想起)**: 強い共鳴を検知。確信度が高い状態。
2.  **REJECT (拒絶)**: 矛盾を検知。
3.  **REVIEW (保留/再考)**: 共鳴が弱い。さらなる観察や仮説生成（アブダクション）が必要です。

## 3. Repository Structure / リポジトリ構成
This repository contains a minimal, dependency-light implementation of the core algorithms.
本リポジトリには、依存関係を極力排除したコアアルゴリズムの最小実装が含まれています。

*   `src/core/`: The heart of the system. (システムの中核)
    *   `holographic_memory.py`: Complex-vector memory operations (HRR). (複素ベクトルメモリ演算)
    *   `recall_engine.py`: The iterative recall loop. (反復的想起ループ)
    *   `decision_state.py`: Definition of Trinary Logic states. (三値論理状態の定義)
*   `src/demo/`: Executable demonstrations. (実行可能なデモ)
    *   `minimal_demo.py`: A self-contained script showing the "Recall -> Decision" flow. (「想起→判断」フローを示す自己完結型スクリプト)
*   `docs/`: Detailed architectural explanations. (アーキテクチャ詳細解説)

## 4. Quick Start

### Prerequisites / 前提条件
*   Python 3.10+
*   `numpy` (For vector operations / ベクトル演算用)

### Installation / インストール
```bash
git clone https://github.com/chigenori053/coherent-recall-first.git
cd coherent-recall-first
pip install numpy
```

### Running the Demo / デモの実行
Execute the minimal demo to see the Recall-First engine in action:
想起優先エンジンの動作を確認するために、最小デモを実行してください：

```bash
python src/demo/minimal_demo.py
```

You will observe the system:
以下のシステム挙動が確認できます：

1.  **Observing**: Inputing a pattern. (入力パターンを観測)
2.  **Resonating**: Checking resonance against Holographic Memory. (ホログラフィックメモリとの共鳴を確認)
3.  **Deciding**: Determining logic state (ACCEPT/REVIEW) based on resonance thresholds. (共鳴閾値に基づいて判断)
4.  **Learning**: Encoding and superposing if validated. (妥当であればエンコードして重ね合わせ学習)

## 5. License / ライセンス
This research is part of a proposal for the Mitoh Advanced Program.
Licensed under the **Apache License 2.0**.

本研究は未踏アドバンスト事業への提案の一部です。
**Apache License 2.0** の下で公開されています。
