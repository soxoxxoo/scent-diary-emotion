# Scent Emotion Model v6 

## 모델 버전: `scent_emotion_model_v6.keras`

---

## 학습 데이터
- **파일명**: `emotion_diary_merged_sorted_unique_fixed (1).xlsx`
- **총 문장 수**: 800개
- **구성**: 감정별 균등 분포 / 중복 제거 완료
- **감정 클래스 (총 8개)**:
  - `['기쁨', '불안', '당황', '분노', '상처', '슬픔', '우울', '흥분']`
  - 숫자 레이블 0~7로 변환하여 학습

---

## 모델 구조
- 사전학습 모델: `klue/roberta-base`
- 분류기 구성:
  - `[CLS]` → Dense(128, relu)
  - Dropout(0.3)
  - Dense(8, softmax)

---

## 입력값 예시 (`text`, 감정 일기 문장)
```python
test_texts = [
    "향기를 맡자마자 눈물이 날 뻔했다. 마음이 먹먹했다.",
    "상쾌하고 기분 좋은 풀냄새가 하루를 열어줬다.",
    "너무 강한 스파이시 향에 깜짝 놀랐다. 숨이 턱 막혔다.",
    "무언가 편안하면서도 어릴 적 기억이 떠오르는 향이었다.",
]
```

## 출력값 예시 (`label`, 감정 레이블 숫자)
```python
inputs = tokenizer(test_texts, return_tensors="tf", padding=True, truncation=True)
outputs = model(**inputs)
predicted = tf.argmax(outputs.logits, axis=1)

print(predicted.numpy())  # 예: [5, 0, 2, 4]
```

---

## 학습 성능 (v6 기준)
```text
Epoch 1/5
train_accuracy:  24.6% | val_accuracy:  55.1%
loss:           1.9229 | val_loss:      1.2595

Epoch 2/5
train_accuracy:  64.6% | val_accuracy:  65.1%
loss:           0.9840 | val_loss:      0.9167

Epoch 3/5
train_accuracy:  80.1% | val_accuracy:  72.8%
loss:           0.5831 | val_loss:      0.8217

Epoch 4/5
train_accuracy:  85.4% | val_accuracy:  69.3%
loss:           0.3930 | val_loss:      1.0186

Epoch 5/5
train_accuracy:  91.0% | val_accuracy:  70.1%
loss:           0.2694 | val_loss:      1.0159
```

→ 과적합 없이 학습 성능 향상. 검증 정확도는 70% 수준에서 유지.
