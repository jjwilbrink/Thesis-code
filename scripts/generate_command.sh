for dataset in scan nacs
do
for split in random_split length_split jump_split turn_left_split around_right_split
do
  ../env/bin/fairseq-generate \
    ./data-bin/${dataset}/${split}_tokenized \
    --path checkpoints/${dataset}/${split}/checkpoint_last.pt \
    > ./outputs/${dataset}/${split}.txt
done
done