# Verification & Learning Test Report v1.1

**Date:** 2026-01-15 23:14:01
**Executor:** Automated Test Script

## Summary
This report documents the execution of the Verification & Learning Test v1.1.

## Test Results
| ID | Input | Decision | Result | Details |
|---|---|---|---|---|
| T1 | 3x + 5x を計算せよ | Action.PROMOTE | PASS | {'prob': 0.49198471830418306} |
| T2 | 3x と 5x をまとめて | Action.PROMOTE | PASS | {'resonance': 0.9979188208210152} |
| T3 | まず両辺から3を引き、その後2で割れ | Action.PROMOTE | PASS | {} |
| T4 | いい感じに解いて | Action.SUPPRESS | PASS | {'persisted': True} |
| T5 | この式を詩的に説明して | Action.SUPPRESS | PASS | {'persisted': True} |
| T6 | 未定義の演算Zを実行せよ | Action.SUPPRESS | PASS | {'persisted': True} |
| T7 | 7x + x をまとめよ | Action.PROMOTE | PASS | {'resonance': 0.9423472071815223, 'duration': 3.1948089599609375e-05} |

## Raw Logs
```json
[
  {
    "decision_state": "DecisionState(resonance_score=0.49198471830418306, margin=0.49198471830418306, repetition_count=1, entropy_estimate=0.508015281695817, memory_origin='Dynamic', historical_conflict_rate=0.0)",
    "action": "Action.PROMOTE",
    "metadata": {
      "id": "T1_REQ",
      "content": "3x + 5x \u3092\u8a08\u7b97\u305b\u3088",
      "validation_confidence": 1.0
    }
  },
  {
    "decision_state": "DecisionState(resonance_score=0.9979188208210152, margin=0.0, repetition_count=1, entropy_estimate=0.00208117917898476, memory_origin='Dynamic', historical_conflict_rate=0.0)",
    "action": "Action.PROMOTE",
    "metadata": {
      "id": "T2_REQ",
      "content": "3x \u3068 5x \u3092\u307e\u3068\u3081\u3066"
    }
  },
  {
    "decision_state": "DecisionState(resonance_score=0.6211832764183152, margin=0.3067696962095472, repetition_count=1, entropy_estimate=0.37881672358168483, memory_origin='Dynamic', historical_conflict_rate=0.0)",
    "action": "Action.PROMOTE",
    "metadata": {
      "id": "T3_REQ",
      "content": "\u307e\u305a\u4e21\u8fba\u304b\u30893\u3092\u5f15\u304d\u3001\u305d\u306e\u5f8c2\u3067\u5272\u308c",
      "validation_confidence": 0.95
    }
  },
  {
    "decision_state": "DecisionState(resonance_score=0.18827019717520774, margin=0.07778167709957713, repetition_count=1, entropy_estimate=0.8117298028247922, memory_origin='Dynamic', historical_conflict_rate=0.0)",
    "action": "Action.SUPPRESS",
    "metadata": {
      "id": "T4_REQ",
      "content": "\u3044\u3044\u611f\u3058\u306b\u89e3\u3044\u3066"
    }
  },
  {
    "decision_state": "DecisionState(resonance_score=0.03246989440346057, margin=0.0, repetition_count=1, entropy_estimate=0.9675301055965394, memory_origin='Dynamic', historical_conflict_rate=0.0)",
    "action": "Action.SUPPRESS",
    "metadata": {
      "id": "T5_REQ",
      "content": "\u3053\u306e\u5f0f\u3092\u8a69\u7684\u306b\u8aac\u660e\u3057\u3066"
    }
  },
  {
    "decision_state": "DecisionState(resonance_score=0.01433863113219872, margin=0.0027094212889668835, repetition_count=1, entropy_estimate=0.9856613688678013, memory_origin='Dynamic', historical_conflict_rate=0.0)",
    "action": "Action.SUPPRESS",
    "metadata": {
      "id": "T6_REQ",
      "content": "\u672a\u5b9a\u7fa9\u306e\u6f14\u7b97Z\u3092\u5b9f\u884c\u305b\u3088"
    }
  },
  {
    "decision_state": "DecisionState(resonance_score=0.9423472071815223, margin=0.0, repetition_count=1, entropy_estimate=0.05765279281847768, memory_origin='Dynamic', historical_conflict_rate=0.0)",
    "action": "Action.PROMOTE",
    "metadata": {
      "id": "T7_REQ"
    }
  }
]
```