for split in random_split length_split jump_split turn_left_split
do
./env/bin/fairseq-preprocess \
  --source-lang source \
  --target-lang target \
  --trainpref data/${split}_train \
  --validpref data/${split}_train \ #even when not using validation data it still needs to exist in the binarized data
  --testpref data/${split}_test \
  --destdir data-bin/${split}_tokenized
done
