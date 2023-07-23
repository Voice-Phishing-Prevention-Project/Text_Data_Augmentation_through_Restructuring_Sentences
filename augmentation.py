import random
import pandas as pd

df1 = pd.read_csv("대출사기형_phising_data.csv")
df2 = pd.read_csv("사칭형_phising_data.csv")

def sentence_rearrangement(sentence):
    words = sentence.split()  # 문장을 단어로 분리
    random.shuffle(words)  # 단어의 순서를 무작위로 섞음
    new_sentence = ' '.join(words)  # 단어들을 다시 문장으로 조합
    return new_sentence

df2 = df2["comments"]
# print(df2)
augmented_sentences = []
#
for i in range(0,188):
    for k in range(5):  # 5개의 재구성된 문장 생성
        augmented_sentence = sentence_rearrangement(df2[i])
        augmented_sentences.append(augmented_sentence)


dff = pd.DataFrame(augmented_sentences)
print(dff)
for i in range(0,len(dff)+1):
    dff["피싱여부"]=1


dff.columns = ["comments",'피싱여부']
print(dff["comments"])
#
dff.to_csv("[데이터증강]문장재구성_사칭형.csv")