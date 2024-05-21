#!/bin/bash

if [ -f "/usr/local/anaconda3/etc/profile.d/conda.sh" ]; then
    . "/usr/local/anaconda3/etc/profile.d/conda.sh"
else
    export PATH="/usr/local/anaconda3/bin:$PATH"
fi

conda activate thesis

# Datasets are loaded and results are save in different directories, but otherwise the commands for both datasets are the same
for dataset in scan nacs
do
for split in random_split length_split jump_split turn_left_split
do
  conda run fairseq-train \
    data-bin/${dataset}/${split}_tokenized \
    --arch fconv_wmt_en_de \
    --max-tokens 3000 \
    --disable-validation \
    --lr 0.01 \
    --lr-scheduler fixed\
    --force-anneal 50 \
    --batch-size 25 \
    --dropout 0.25 \
    --optimizer nag \
    --clip-norm 0.1 \
    --criterion label_smoothed_cross_entropy \
    --label-smoothing 0.1 \
    --encoder-layers "[(512, 5), (512, 5), (512, 5), (512, 5), (512, 5), (512, 5)]" \
    --decoder-layers "[(512, 5), (512, 5), (512, 5), (512, 5), (512, 5), (512, 5)]" \
    --save-dir checkpoints/${dataset}/${split} \
    --max-epoch 100
done
done