SCAN_FOLDER = './SCAN/'
DATA_FOLDER = './data/'
SPLITS = {
    'random_split_{split}': 'simple_split/tasks_{split}_simple.txt',
    'length_split_{split}': 'length_split/tasks_{split}_length.txt',
    'jump_split_{split}': 'add_prim_split/tasks_{split}_addprim_jump.txt',
    'turn_left_split_{split}': 'add_prim_split/tasks_{split}_addprim_turn_left.txt',
    'around_right_split_{split}': 'template_split/tasks_{split}_template_around_right.txt'
}
for split in SPLITS:
    for train_test in ['train', 'test']:
        with open(SCAN_FOLDER + SPLITS[split].format(split=train_test), 'r') as input_file,\
             open(DATA_FOLDER + split.format(split=train_test)+'.source', 'w') as output_source_file,\
             open(DATA_FOLDER + split.format(split=train_test)+'.target', 'w') as output_target_file:
            for line in input_file:
                target, source = line.split(' OUT: ')
                output_source_file.write(source[:-1] + '\n')
                output_target_file.write(target[4:] + '\n')
