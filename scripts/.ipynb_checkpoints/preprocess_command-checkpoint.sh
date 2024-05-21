# Preprocessing is the same for both datasets except the source and target are reversed.
for split in random_split length_split jump_split turn_left_split around_right_split
do
../env/bin/fairseq-preprocess \
  --source-lang source \
  --target-lang target \
  --trainpref data/${split}_train \
  --validpref data/${split}_train \
  --testpref data/${split}_test \
  --destdir data-bin/nacs/${split}_tokenized
../env/bin/fairseq-preprocess \
  --source-lang target \
  --target-lang source \
  --trainpref data/${split}_train \
  --validpref data/${split}_train \
  --testpref data/${split}_test \
  --destdir data-bin/scan/${split}_tokenized
done