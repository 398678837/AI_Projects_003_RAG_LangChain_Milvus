# NLP基础

## 什么是NLP？

NLP（Natural Language Processing）是自然语言处理的缩写，是人工智能的一个子领域，专注于计算机与人类之间使用自然语言进行交互的技术。

## 基本概念

### 1. 分词

分词是将文本拆分为单词或句子的过程。

```python
from nltk.tokenize import word_tokenize, sent_tokenize

text = "NLP is a subfield of artificial intelligence that focuses on the interaction between computers and humans using natural language."
sentences = sent_tokenize(text)
words = word_tokenize(text)
print(f"句子分词结果: {sentences}")
print(f"单词分词结果: {words}")
```

### 2. 停用词移除

停用词是指在文本中出现频率很高，但对文本语义贡献很小的单词，如“the”、“is”、“a”等。停用词移除是将这些单词从文本中移除的过程。

```python
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
print(f"停用词移除结果: {filtered_words}")
```

### 3. 词形还原

词形还原是将单词还原为其基本形式的过程，如将“running”还原为“run”，将“better”还原为“good”。

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
print(f"词形还原结果: {lemmatized_words}")
```

### 4. 词性标注

词性标注是为文本中的每个单词标注其词性的过程，如名词、动词、形容词等。

```python
from nltk.tag import pos_tag

tagged_words = pos_tag(lemmatized_words)
print(f"词性标注结果: {tagged_words}")
```

## 总结

NLP是人工智能的一个子领域，专注于计算机与人类之间使用自然语言进行交互的技术。本目录提供了NLP的基本概念和技术，帮助您快速掌握NLP的基础知识。
