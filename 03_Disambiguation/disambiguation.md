# Disambiguation
### February 20, 2019

I tested UDPipe and conllu-perceptron-tagger on the [Universal Dependencies Finnish TDT Treebank](https://github.com/UniversalDependencies/UD_Finnish-TDT).

For evaluation of performance, I used the [CoNLL-2017 evaluation script](http://universaldependencies.org/conll17/eval.zip).

The evaluation metrics are defined by [Universal Dependencies](http://universaldependencies.org/conll17/evaluation.html) as follows:  

>**Precision** (P) is the number of correct relations divided by the number of system-produced nodes.
**Recall** (R) is the number of correct relations divided by the number of gold-standard nodes.
The **Labeled Attachment Score (LAS)** reports the percentage of words that are assigned both the correct syntactic head and the correct dependency label.
The **F1 score** can be calculated as 2PR / (P+R)

# Results
### UDPipe

| Metrics    | Precision | Recall | F1 Score | AligndAcc |
|----------:|----------:|-------:|---------:|----------:|
| Tokens    | 100.00    | 100.00 | 100.00   |           |
| Sentences | 100.00    | 100.00 | 100.00   |           |
| Words     | 100.00    | 100.00 | 100.00   |           |
| UPOS      | 94.64     | 94.64  | 94.64    | 94.64     |
| XPOS      | 95.81     | 95.81  | 95.81    | 95.81     |
| Feats     | 90.77     | 90.77  | 90.77    | 90.77     |
| AllTags   | 89.75     | 89.75  | 89.75    | 89.75     |
| Lemmas    | 84.52     | 84.52  | 84.52    | 84.52     |
| UAS       | 100.00    | 100.00 | 100.00   | 100.00    |
| LAS       | 100.00    | 100.00 | 100.00   | 100.00    |

### perceptron tagger

|Metrics    | Precision |    Recall |  F1 Score | AligndAcc |
|----------:|----------:|----------:|----------:|----------:|
|Tokens     |    100.00 |    100.00 |    100.00 |           |
|Sentences  |    100.00 |    100.00 |    100.00 |           |
|Words      |    100.00 |    100.00 |    100.00 |           |
|UPOS       |     90.42 |     90.42 |     90.42 |     90.42 |
|XPOS       |    100.00 |    100.00 |    100.00 |    100.00 |
|Feats      |    100.00 |    100.00 |    100.00 |    100.00 |
|AllTags    |     90.42 |     90.42 |     90.42 |     90.42 |
|Lemmas     |    100.00 |    100.00 |    100.00 |    100.00 |
|UAS        |    100.00 |    100.00 |    100.00 |    100.00 |
|LAS        |    100.00 |    100.00 |    100.00 |    100.00 |


ask about UPOS
