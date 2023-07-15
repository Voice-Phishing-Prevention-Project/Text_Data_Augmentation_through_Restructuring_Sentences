# -*- coding: utf-8 -*-
"""(한국어)데이터 증강 by 문장 재구성.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c2JZ4TlWM4xV8mqlcK9zIljU3ul6sdNS
"""

import random

def sentence_rearrangement(sentence):
    words = sentence.split()  # 문장을 단어로 분리
    random.shuffle(words)  # 단어의 순서를 무작위로 섞음
    new_sentence = ' '.join(words)  # 단어들을 다시 문장으로 조합
    return new_sentence

# 증강할 문장
original_sentence = "한국어 문장을 재구성하는 예시입니다."

# 문장 재구성을 통한 데이터 증강
augmented_sentences = []
for _ in range(5):  # 5개의 재구성된 문장 생성
    augmented_sentence = sentence_rearrangement(original_sentence)
    augmented_sentences.append(augmented_sentence)

# 결과 출력
print("원본 문장:", original_sentence)
print("증강된 문장:")
for sentence in augmented_sentences:
    print(sentence)