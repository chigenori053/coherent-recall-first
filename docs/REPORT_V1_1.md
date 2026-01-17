# Verification & Learning Test Report v1.1

**Date:** 2026-01-17 14:42:41
**Executor:** Automated Test Script

## Summary
This report documents the execution of the Verification & Learning Test v1.1.

## Test Results
| ID | Input | Decision | Result | Details |
|---|---|---|---|---|
| T1 | 3x + 5x を計算せよ | Action.PROMOTE | PASS | {'prob': 0.5051624023152613} |
| T2 | 3x と 5x をまとめて | Action.PROMOTE | PASS | {'resonance': 0.9969264693358907} |
| T3 | まず両辺から3を引き、その後2で割れ | Action.PROMOTE | PASS | {} |
| T4 | いい感じに解いて | Action.SUPPRESS | PASS | {'persisted': True} |
| T5 | この式を詩的に説明して | Action.SUPPRESS | PASS | {'persisted': True} |
| T6 | 未定義の演算Zを実行せよ | Action.SUPPRESS | PASS | {'persisted': True} |
| T7 | 7x + x をまとめよ | Action.PROMOTE | PASS | {'resonance': 0.9433073440539985, 'duration': 2.7894973754882812e-05} |

## Raw Logs
```json
[
  {
    "decision_state": "DecisionState(resonance_score=0.5051624023152613, margin=0.5051624023152613, repetition_count=1, entropy_estimate=0.4948375976847387, memory_origin='Dynamic', historical_conflict_rate=0.0)",
    "action": "Action.PROMOTE",
    "metadata": {
      "id": "T1_REQ",
      "content": "3x + 5x \u3092\u8a08\u7b97\u305b\u3088",
      "validation_confidence": 1.0
    }
  },
  {
    "decision_state": "DecisionState(resonance_score=0.9969264693358907, margin=0.0, repetition_count=1, entropy_estimate=0.003073530664109314, memory_origin='Dynamic', historical_conflict_rate=0.0)",
    "action": "Action.PROMOTE",
    "metadata": {
      "id": "T2_REQ",
      "content": "3x \u3068 5x \u3092\u307e\u3068\u3081\u3066"
    }
  },
  {
    "decision_state": "DecisionState(resonance_score=0.6190443397475909, margin=0.3240569233577054, repetition_count=1, entropy_estimate=0.3809556602524091, memory_origin='Dynamic', historical_conflict_rate=0.0)",
    "action": "Action.PROMOTE",
    "metadata": {
      "id": "T3_REQ",
      "content": "\u307e\u305a\u4e21\u8fba\u304b\u30893\u3092\u5f15\u304d\u3001\u305d\u306e\u5f8c2\u3067\u5272\u308c",
      "validation_confidence": 0.95
    }
  },
  {
    "decision_state": "DecisionState(resonance_score=0.1796343756264937, margin=0.061601483498742546, repetition_count=1, entropy_estimate=0.8203656243735062, memory_origin='Dynamic', historical_conflict_rate=0.0)",
    "action": "Action.SUPPRESS",
    "metadata": {
      "id": "T4_REQ",
      "content": "\u3044\u3044\u611f\u3058\u306b\u89e3\u3044\u3066"
    }
  },
  {
    "decision_state": "DecisionState(resonance_score=0.02151685552435009, margin=0.0, repetition_count=1, entropy_estimate=0.9784831444756499, memory_origin='Dynamic', historical_conflict_rate=0.0)",
    "action": "Action.SUPPRESS",
    "metadata": {
      "id": "T5_REQ",
      "content": "\u3053\u306e\u5f0f\u3092\u8a69\u7684\u306b\u8aac\u660e\u3057\u3066"
    }
  },
  {
    "decision_state": "DecisionState(resonance_score=0.03236214094464317, margin=0.007633274970063747, repetition_count=1, entropy_estimate=0.9676378590553568, memory_origin='Dynamic', historical_conflict_rate=0.0)",
    "action": "Action.SUPPRESS",
    "metadata": {
      "id": "T6_REQ",
      "content": "\u672a\u5b9a\u7fa9\u306e\u6f14\u7b97Z\u3092\u5b9f\u884c\u305b\u3088"
    }
  },
  {
    "decision_state": "DecisionState(resonance_score=0.9433073440539985, margin=0.0, repetition_count=1, entropy_estimate=0.05669265594600148, memory_origin='Dynamic', historical_conflict_rate=0.0)",
    "action": "Action.PROMOTE",
    "metadata": {
      "id": "T7_REQ"
    }
  }
]
```