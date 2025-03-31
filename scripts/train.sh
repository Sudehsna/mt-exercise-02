#! /bin/bash

scripts=$(dirname "$0")
base=$(realpath $scripts/..)

models=$base/models
data=$base/data
tools=$base/tools

mkdir -p $models

num_threads=4
device=""

SECONDS=0

(cd $tools/pytorch-examples/word_language_model &&
    CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python main.py --data $data/moby \
        --epochs 20 \
        --log-interval 100 \
        --emsize 200 --nhid 200 --dropout 0.5 --tied \
        --save $models/model.pt #\
        # --log-epoch $data/logs/epoch-0.9-ppl.tsv \
        # --log-test $data/logs/test-0.9-ppl.tsv \
        # --log-valid $data/logs/valid-0.9-ppl.tsv
)

echo "time taken:"
echo "$SECONDS seconds"
