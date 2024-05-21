import pandas

SCAN_TASK_FILE = '../SCAN/tasks.txt'
SPLITS = ('random_split', 'length_split', 'jump_split', 'turn_left_split')
OUTPUT_FILE = '../processed_outputs/{split}.csv'

# Open SCAN tasks and make dictionary with the commands as keys and action sequences as values.
correct_answers = {}
line_num=0
with open(SCAN_TASK_FILE) as file:
    while True:
        line = file.readline()
        if line == '':
            break
        out, in_ = line.split(' OUT: ')
        correct_answers[out[4:]] = in_[:-1]

for split in SPLITS:
    with open(f'./outputs/{split}.txt') as file:
        text = file.readlines()
    
    # remove empty last line
    if text[:-1] == '':
        text = text[:-1]

    # Process data in dataframe to make sure that lines with the same id are processed together.
    raw_data = []

    for line in text:
        index = line.find('\t')
        #      id             type     data
        row = [line[2:index], line[0], line[index+1:-1]]
        raw_data.append(row)

    raw_df = pandas.DataFrame(raw_data)
    raw_df.columns = ['id', 'type', 'data']
    raw_df = df.groupby('id')

    # Make the actual dataframe with id input and output columns
    processed_data = []
    for group in df.groups:
        group_df = df.get_group(group)
        processed_data.append(
            [
                group, #id
                 group_df[group_df['type'] == 'S']['data'].iloc[0], #input
                 group_df[group_df['type'] == 'D']['data'].iloc[0].split('\t')[1] #outpt
            ]
        )
        
    processed_df = pandas.DataFrame(processed_data)
    processed_df.columns = ['id', 'input', 'output']

    # Add the 'score' to every row of the dataframe.
    processed_df['correct'] = processed_df.apply(
        lambda x: correct_answers.get(x['output']) == x['input'], axis=1
    )

    processed_df.to_csv(OUTPUT_FILE.format(split=split))

    # Calculate accuracy
    accuracy = sum(new_df['correct']) / len(new_df)
    print(f'{split}: accuracy')