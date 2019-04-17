# Improving `conllu-perceptron-tagger`
### March 5, 2019

Starting performance:


|Metrics    | Precision |    Recall |  F1 Score | AligndAcc  |
|----------:|----------:|----------:|----------:|----------- |
|Tokens     |    100.00 |    100.00 |    100.00 |            |
|Sentences  |    100.00 |    100.00 |    100.00 |            |
|Words      |    100.00 |    100.00 |    100.00 |            |
|UPOS       |     96.24 |     96.24 |     96.24 |     96.24  |
|XPOS       |    100.00 |    100.00 |    100.00 |    100.00  |
|Feats      |    100.00 |    100.00 |    100.00 |    100.00  |
|AllTags    |     96.24 |     96.24 |     96.24 |     96.24  |
|Lemmas     |    100.00 |    100.00 |    100.00 |    100.00  |
|UAS        |    100.00 |    100.00 |    100.00 |    100.00  |
|LAS        |    100.00 |    100.00 |    100.00 |    100.00  |

I widened suffix and word to i-2 and i+2.
This did not do much, but it technically didn't hurt anything.

Ending performance: 
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     96.25 |     96.25 |     96.25 |     96.25
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     96.25 |     96.25 |     96.25 |     96.25
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
