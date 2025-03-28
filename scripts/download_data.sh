#! /bin/bash

scripts=$(dirname "$0")
base=$scripts/..

data=$base/data

mkdir -p $data

tools=$base/tools

# link default training data for easier access

mkdir -p $data/wikitext-2

for corpus in train valid test; do
    absolute_path=$(realpath $tools/pytorch-examples/word_language_model/data/wikitext-2/$corpus.txt)
    ln -snf $absolute_path $data/wikitext-2/$corpus.txt
done

# download a different interesting data set!

mkdir -p $data/moby

mkdir -p $data/moby/raw

wget https://www.gutenberg.org/cache/epub/2701/pg2701.txt
mv pg2701.txt $data/moby/raw/story.txt

# preprocess slightly

cat $data/moby/raw/story.txt | python $base/scripts/preprocess_raw.py > $data/moby/raw/story.cleaned.txt

# tokenize, fix vocabulary upper bound

cat $data/moby/raw/story.cleaned.txt | python $base/scripts/preprocess.py --vocab-size 5000 --tokenize --lang "en" --sent-tokenize > \
    $data/moby/raw/story.preprocessed.txt

# split into train, valid and test

head -n 440 $data/moby/raw/story.preprocessed.txt | tail -n 400 > $data/moby/valid.txt
head -n 840 $data/moby/raw/story.preprocessed.txt | tail -n 400 > $data/moby/test.txt
tail -n 3075 $data/moby/raw/story.preprocessed.txt | head -n 2955 > $data/moby/train.txt
