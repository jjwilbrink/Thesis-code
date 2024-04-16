for split in random_split length_split jump_split turn_left_split
do
  ./env/bin/fairseq-generate \
    data-bin/${split}_tokenized \
    --path checkpoints/${split}/checkpoint_last.pt \
    > ${split}_output.txt
done
