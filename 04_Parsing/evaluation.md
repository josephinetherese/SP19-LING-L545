# Parsing
### March 20, 2019
Corpus: UD_Hindi-HDTB

```
$ udpipe --tokenizer non --tagger non --train hindi.udpipe < UD_Hindi-HDTB/hi_hdtb-ud-train.conllu
Loading training data: done.
Training the UDPipe model.
Training tokenizer with the following options: tokenize_url=1, allow_spaces=0, dimension=24
  epochs=100, batch_size=50, segment_size=50, learning_rate=0.0050, learning_rate_final=0.0000
  dropout=0.1000, early_stopping=0
Epoch 1, logprob: -4.9226e+04, training acc: 96.48%
Epoch 2, logprob: -4.6512e+03, training acc: 99.64%
Epoch 3, logprob: -4.0197e+03, training acc: 99.68%
Epoch 4, logprob: -3.6016e+03, training acc: 99.70%
Epoch 5, logprob: -3.4918e+03, training acc: 99.72%
Epoch 6, logprob: -3.1444e+03, training acc: 99.74%
Epoch 7, logprob: -3.0037e+03, training acc: 99.75%
Epoch 8, logprob: -2.9883e+03, training acc: 99.75%
Epoch 9, logprob: -3.0597e+03, training acc: 99.75%
Epoch 10, logprob: -2.7163e+03, training acc: 99.77%
Epoch 11, logprob: -2.8302e+03, training acc: 99.76%
Epoch 12, logprob: -2.8916e+03, training acc: 99.77%
Epoch 13, logprob: -2.7566e+03, training acc: 99.77%
Epoch 14, logprob: -2.7476e+03, training acc: 99.78%
Epoch 15, logprob: -2.6364e+03, training acc: 99.78%
Epoch 16, logprob: -2.6399e+03, training acc: 99.78%
Epoch 17, logprob: -2.6197e+03, training acc: 99.78%
Epoch 18, logprob: -2.5223e+03, training acc: 99.79%
Epoch 19, logprob: -2.5323e+03, training acc: 99.78%
Epoch 20, logprob: -2.4662e+03, training acc: 99.80%
Epoch 21, logprob: -2.5540e+03, training acc: 99.78%
Epoch 22, logprob: -2.5287e+03, training acc: 99.79%
Epoch 23, logprob: -2.4489e+03, training acc: 99.80%
Epoch 24, logprob: -2.4086e+03, training acc: 99.80%
Epoch 25, logprob: -2.4363e+03, training acc: 99.79%
Epoch 26, logprob: -2.4222e+03, training acc: 99.79%
Epoch 27, logprob: -2.4159e+03, training acc: 99.80%
Epoch 28, logprob: -2.5039e+03, training acc: 99.80%
Epoch 29, logprob: -2.3808e+03, training acc: 99.80%
Epoch 30, logprob: -2.3635e+03, training acc: 99.80%
Epoch 31, logprob: -2.3359e+03, training acc: 99.80%
Epoch 32, logprob: -2.4491e+03, training acc: 99.80%
Epoch 33, logprob: -2.3203e+03, training acc: 99.81%
Epoch 34, logprob: -2.3410e+03, training acc: 99.81%
Epoch 35, logprob: -2.3401e+03, training acc: 99.81%
Epoch 36, logprob: -2.4301e+03, training acc: 99.79%
Epoch 37, logprob: -2.3611e+03, training acc: 99.81%
Epoch 38, logprob: -2.3229e+03, training acc: 99.80%
Epoch 39, logprob: -2.3228e+03, training acc: 99.81%
Epoch 40, logprob: -2.3427e+03, training acc: 99.81%
Epoch 41, logprob: -2.2963e+03, training acc: 99.81%
Epoch 42, logprob: -2.2434e+03, training acc: 99.82%
Epoch 43, logprob: -2.2048e+03, training acc: 99.82%
Epoch 44, logprob: -2.2574e+03, training acc: 99.82%
Epoch 45, logprob: -2.2935e+03, training acc: 99.81%
Epoch 46, logprob: -2.2400e+03, training acc: 99.82%
Epoch 47, logprob: -2.1944e+03, training acc: 99.82%
Epoch 48, logprob: -2.1387e+03, training acc: 99.82%
Epoch 49, logprob: -2.3125e+03, training acc: 99.82%
Epoch 50, logprob: -2.2792e+03, training acc: 99.81%
Epoch 51, logprob: -2.1454e+03, training acc: 99.83%
Epoch 52, logprob: -2.2769e+03, training acc: 99.82%
Epoch 53, logprob: -2.2041e+03, training acc: 99.82%
Epoch 54, logprob: -2.1863e+03, training acc: 99.82%
Epoch 55, logprob: -2.2548e+03, training acc: 99.82%
Epoch 56, logprob: -2.1153e+03, training acc: 99.83%
Epoch 57, logprob: -2.2472e+03, training acc: 99.81%
Epoch 58, logprob: -2.2048e+03, training acc: 99.82%
Epoch 59, logprob: -2.2407e+03, training acc: 99.81%
Epoch 60, logprob: -2.1616e+03, training acc: 99.82%
Epoch 61, logprob: -2.1415e+03, training acc: 99.83%
Epoch 62, logprob: -2.1417e+03, training acc: 99.83%
Epoch 63, logprob: -2.2060e+03, training acc: 99.82%
Epoch 64, logprob: -2.1493e+03, training acc: 99.82%
Epoch 65, logprob: -2.2440e+03, training acc: 99.82%
Epoch 66, logprob: -2.2739e+03, training acc: 99.82%
Epoch 67, logprob: -2.1285e+03, training acc: 99.82%
Epoch 68, logprob: -2.1957e+03, training acc: 99.81%
Epoch 69, logprob: -2.1701e+03, training acc: 99.83%
Epoch 70, logprob: -2.2017e+03, training acc: 99.82%
Epoch 71, logprob: -2.1583e+03, training acc: 99.82%
Epoch 72, logprob: -2.1456e+03, training acc: 99.82%
Epoch 73, logprob: -2.2314e+03, training acc: 99.82%
Epoch 74, logprob: -2.2691e+03, training acc: 99.82%
Epoch 75, logprob: -2.1674e+03, training acc: 99.82%
Epoch 76, logprob: -2.1130e+03, training acc: 99.83%
Epoch 77, logprob: -2.1890e+03, training acc: 99.82%
Epoch 78, logprob: -2.1618e+03, training acc: 99.82%
Epoch 79, logprob: -2.0395e+03, training acc: 99.83%
Epoch 80, logprob: -2.1764e+03, training acc: 99.82%
Epoch 81, logprob: -2.2378e+03, training acc: 99.82%
Epoch 82, logprob: -2.0614e+03, training acc: 99.82%
Epoch 83, logprob: -2.1703e+03, training acc: 99.82%
Epoch 84, logprob: -2.1409e+03, training acc: 99.83%
Epoch 85, logprob: -2.1952e+03, training acc: 99.83%
Epoch 86, logprob: -2.1914e+03, training acc: 99.82%
Epoch 87, logprob: -2.2199e+03, training acc: 99.83%
Epoch 88, logprob: -2.0607e+03, training acc: 99.83%
Epoch 89, logprob: -2.1005e+03, training acc: 99.83%
Epoch 90, logprob: -2.1306e+03, training acc: 99.82%
Epoch 91, logprob: -2.2026e+03, training acc: 99.82%
Epoch 92, logprob: -2.0582e+03, training acc: 99.83%
Epoch 93, logprob: -2.1928e+03, training acc: 99.82%
Epoch 94, logprob: -2.1514e+03, training acc: 99.82%
Epoch 95, logprob: -2.1214e+03, training acc: 99.83%
Epoch 96, logprob: -2.1028e+03, training acc: 99.82%
Epoch 97, logprob: -1.9968e+03, training acc: 99.84%
Epoch 98, logprob: -2.1055e+03, training acc: 99.82%
Epoch 99, logprob: -2.1539e+03, training acc: 99.83%
Epoch 100, logprob: -2.0862e+03, training acc: 99.83%
Tagger model 1 columns: lemma use=1/provide=1, xpostag use=1/provide=1, feats use=1/provide=1
Creating morphological dictionary for tagger model 1.
Tagger model 1 dictionary options: max_form_analyses=0, custom dictionary_file=none
Tagger model 1 guesser options: suffix_rules=8, prefixes_max=4, prefix_min_count=10, enrich_dictionary=6
Tagger model 1 options: iterations=20, early_stopping=0, templates=tagger
Training tagger model 1.
Iteration 1: done, accuracy 80.98%
Iteration 2: done, accuracy 88.50%
Iteration 3: done, accuracy 90.88%
Iteration 4: done, accuracy 92.46%
Iteration 5: done, accuracy 93.62%
Iteration 6: done, accuracy 94.46%
Iteration 7: done, accuracy 95.08%
Iteration 8: done, accuracy 95.58%
Iteration 9: done, accuracy 96.01%
Iteration 10: done, accuracy 96.26%
Iteration 11: done, accuracy 96.63%
Iteration 12: done, accuracy 96.84%
Iteration 13: done, accuracy 96.99%
Iteration 14: done, accuracy 97.19%
Iteration 15: done, accuracy 97.34%
Iteration 16: done, accuracy 97.45%
Iteration 17: done, accuracy 97.64%
Iteration 18: done, accuracy 97.70%
Iteration 19: done, accuracy 97.74%
Iteration 20: done, accuracy 97.89%
Parser transition options: system=projective, oracle=dynamic, structured_interval=8, single_root=1
Parser uses lemmas/upos/xpos/feats: automatically generated by tagger
Parser embeddings options: upostag=20, feats=20, xpostag=0, form=50, lemma=0, deprel=20
  form mincount=2, precomputed form embeddings=none
  lemma mincount=2, precomputed lemma embeddings=none
Parser network options: iterations=10, hidden_layer=200, batch_size=10,
  learning_rate=0.0200, learning_rate_final=0.0010, l2=0.5000, early_stopping=0
Initialized 'universal_tag' embedding with 0,16 words and 0.0%,100.0% coverage.
Initialized 'feats' embedding with 0,685 words and 0.0%,100.0% coverage.
Initialized 'form' embedding with 0,9663 words and 0.0%,97.6% coverage.
Initialized 'deprel' embedding with 0,27 words and 0.0%,100.0% coverage.
Iteration 1: training logprob -3.0853e+05
Iteration 2: training logprob -4.1445e+05
Iteration 3: training logprob -3.0065e+05
Iteration 4: training logprob -2.4273e+05
Iteration 5: training logprob -2.0372e+05
Iteration 6: training logprob -1.7570e+05
Iteration 7: training logprob -1.5932e+05
Iteration 8: training logprob -1.4530e+05
Iteration 9: training logprob -1.3798e+05
Iteration 10: training logprob -1.2952e+05
The trained UDPipe model was saved.
```

```
$ udpipe --parse hindi.udpipe < UD_Hindi-HDTB/hi_hdtb-ud-test.conllu > testingout.conllu
Loading UDPipe model: done.
```

```
$ python3 conll17_ud_eval.py UD_Hindi-HDTB/hi_hdtb-ud-test.conllu testingout.conllu
LAS F1 Score: 90.09
```

sentence1: इसके अतिरिक्त गुग्गुल कुंड, भीम गुफा तथा भीमशिला भी दर्शनीय स्थल हैं

कुंड is tagged as an nmod but it is nsubj

sentence10: दूसरा मंदिर राधाकृष्ण का है, जिसे कृष्ण भक्तों का नूतन प्रयास समझा जाना ही उत्तम होगा

मंदिर is tagged as an nmod of राधाकृष्ण but it is actually the root. The tagger labeled होगा as the root, which makes sense because it is a VERB whereas मंदिर is a NOUN. I assume this is related to the copula, as the theme of copula constructions is often marked as root (rather than the verb) in DG.

sentence17: पार्वती का मायका अर्थात हिमालय नरेश का निवास (संभवतः ग्रीष्म निवास) भी यही बताया जाता ह

निवास is tagged as being the object of the root, rather than as a modifier of the object of the root.

sentence22: भोज का खर्च भारतीय सेना उठाती है

खर्च is tagged as a compound but should be an obj

sentence70: भीतरी भाग में चाँदी से बनाए गए कमल के फूल जिसकी हजार पंखुड़ियाँ हैं, पर माँ काली शस्त्रों सहित भगवान शिव के ऊपर खड़ी हुई हैं ।

काली is marked as nmod rather than nsubj.
The test corpus says that पर is dislocated. Unsurprisingly, udpipe did not mark it as such. Instead it labeled it as case.


sentence71: काली माँ का मंदिर नवरत्न की तरह निर्मित है और यह 46 फुट चौड़ा तथा 100 फुट ऊँचा है ।

फुट should have been advmod. udpipe called it nmod.

sentence74: यह मंदिर हरे - भरे - मैदान पर स्थित है ।

हरे was labeled as amod rather than nsubj
भरे was labeled as compound rather than amod

sentence88: भारत के सांस्कृतिक धार्मिक तीर्थ स्थलों में माँ काली का मंदिर सबसे प्राचीन माना जाता है ।

प्राचीन was labeled as acl rather than compound.

sentence92: कैसे जाएँ वहाँ -

जाएँ was marked as acl of कैसे rather than root.
वहाँ was marked as root rather than obl of जाएँ.

sentence99:  घाजी तलाबानी नाम के अधिकारी की काम करने जाते समय हत्या की गई ।

जाते was marked as obl rather than advcl
