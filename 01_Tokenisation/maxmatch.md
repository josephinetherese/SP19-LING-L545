# MaxMatch

My MaxMatch implementation is in MaxMatch.py
It expects a sentence from stdin and a training corpus filename as its argument.

Example:
```
$ echo 'また 行き たい 、 そんな 気持ち に さ せ て くれる お 店 です 。' | python3 maxmatch.py ../misc/UD_Japanese-GSD/ja_gsd-ud-train.conllu
```

It takes an optional ```-p``` flag, which makes it use my ```maxmatch_punct()``` method rather than the standard ```maxmatch()```.

It also takes an optional ```-e``` flag, which prints the evaluation score (see below)

```maxmatch_punct()``` differs from the standard MaxMatch approach in one small way. Instead of starting from the very end of the sentence and moving down towards the beginning until it finds a word, ```maxmatch_punct()``` finds the first instance of punctuation in the sentence and works towards the front of the sentence from there.
This assumes that no words in Japanese have punctuation in the middle of them (which from a glance at Wikipedia, seems like a safe assumption). Theoretically, this shaves off a bit of time, but I don't know if it actually has a substantial effect.
The resulting arrays from ```maxmatch_punct()``` and ```maxmatch()``` should always be the same.

The example call above will print the resulting tokenization from the ```maxmatch()``` method.

The `-e` flag causes it to follow the tokenization with a score in the form of a percentage. This value is the [WER](https://github.com/zszyellow/WER-in-python) difference score between the input sentence and the sentence output by ```maxmatch()```. Thus, this assumes that the input sentence is given with spaces between the words.


### Evaluation
I would expect this to be close to perfect on sentences from the training corpus, but it does not appear to be. It looks like its accuracy is in the mid 80s
For example, on the example sentence above, it reports 85%. The output looks like so:
また 行き たい 、 そんな 気持ち に させ て くれる お 店 です 。
The original sentence was:
また 行き たい 、 そんな 気持ち に さ せ て くれる お 店 です 。

As you may notice, maxmatch clumped together two characters that should not have been clumped in this case.

On another random sentence from the training corpus:
クロヴィス 2世 と バルティルド の 子供 。
it returns:
クロヴィス 2世 と バルティルド の 子供 。
With a reported accuracy of 88%. What is the difference? I am not sure.

From test corpus:

```
$ echo '幸福の科学 側 から は , 特に どう し て ほしい という 要望 は いただい てい ませ ん 。' | python3 maxmatch.py ../misc/UD_Japanese-GSD/ja_gsd-ud-train.conllu -e
幸福 の 科学 側 から は , 特に どうして ほしい という 要望 は いただい て いま せ ん 。
83.02%
```

```
$ echo '星取り 参加 は 当然 と さ れ , 不参加 は 白眼視 さ れる 。' | python3 maxmatch.py ../misc/UD_Japanese-GSD/ja_gsd-ud-train.conllu -e
星 取り 参加 は 当然 と さ れ , 不 参加 は 白 眼 視 さ れる 。
64.86%
```

```
$ echo '心 が ない ん だ 。' | python3 maxmatch.py ../misc/UD_Japanese-GSD/ja_gsd-ud-train.conllu -e
心 がな い ん だ 。
61.54%
```

'星 取り' does not appear in the training corpus, so when maxmatch reaches the last character in the sentence and hasn't found a match, it just calls the last character a word and then moves on.
'どう し て' was clumped into 'どうして'

The average performance for the test corpus seems to be closer to the mid sixties to low 70s.
