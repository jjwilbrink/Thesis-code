for split in random_split length_split jump_split turn_left_split
do
  ./env/bin/fairseq-train \
    data-bin/${split}_tokenized \
    --arch fconv_wmt_en_de \
    --max-tokens 4000 \
    --disable-validation \
    --lr 0.01 \
    --batch-size 25 \
    --dropout 0.25 \
    --optimizer nag \
    --encoder-layers "[(512, 5), (512, 5), (512, 5), (512, 5), (512, 5), (512, 5)]" \
    --decoder-layers "[(512, 5), (512, 5), (512, 5), (512, 5), (512, 5), (512, 5)]" \
    --save-dir checkpoints/${split}
done
