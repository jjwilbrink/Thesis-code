#!python

import pandas
import os

SCAN_RAW_OUTPUTS = './outputs/scan/'
NACS_RAW_OUTPUTS = './outputs/nacs/'
SCAN_FOLDER = './SCAN/'
SCAN_PROCESSED_OUTPUTS = './processed_outputs/scan/'
NACS_PROCESSED_OUTPUTS = './processed_outputs/nacs/'

print(os.getcwd(), SCAN_FOLDER)

# Load original data to check answers with later on.
correct_answers = {}

with open(f'{SCAN_FOLDER}tasks.txt') as file:
    while True:
        line = file.readline()
        if line == '':
            break
        out, in_ = line.split(' OUT: ')
        correct_answers[out[4:]] = in_[:-1]

for raw_outputs, processed_outputs in ((SCAN_RAW_OUTPUTS, SCAN_PROCESSED_OUTPUTS), (NACS_RAW_OUTPUTS, NACS_PROCESSED_OUTPUTS)):
    scores = ''
    for split in ['random_split', 'length_split', 'jump_split', 'turn_left_split', 'around_right_split']:
        # Load fairseq generated data.
        with open(f'{raw_outputs}{split}.txt') as file:
            text = file.readlines()
        text = text[/:-1]
    
        data = []

        # Get id type and data from the raw data.
        for line in text:
            index = line.find('\t')
            row = [line[2:index], line[0], line[index+1:-1]]
            data.append(row)
    
        df = pandas.DataFrame(data)
        df.columns = ['id', 'type', 'data']
        # Group by id to because input and output are on different rows but with same id.
        df = df.groupby('id')

        # Process data into clean input output pairs.
        new_data = []
        for group in df.groups:
            group_df = df.get_group(group)
            new_data.append([group, group_df[group_df['type'] == 'S']['data'].iloc[0], group_df[group_df['type'] == 'D']['data'].iloc[0].split('\t')[1]])
        new_df = pandas.DataFrame(new_data)
        new_df.columns = ['id', 'input', 'output']

        # For both dataset the action sequence is loaded from the correct answers by using the command: in one case that is the output and in the other case the input.
        if raw_outputs == NACS_RAW_OUTPUTS:
            new_df['correct_input'] = new_df.apply(lambda x: correct_answers.get(x['output']), axis=1)
            new_df['correct'] = new_df['correct_input'] == new_df['input']
            new_df.to_csv(f'{processed_outputs}{split}.csv', index=False)
        else:
            new_df['correct'] = new_df.apply(lambda x: correct_answers.get(x['input']) == x['output'], axis=1)
            new_df.to_csv(f'{processed_outputs}{split}.csv', index=False)

        # Accuracies are calculated to quickly check if everythin is correct, more processing is done in the the stats notebook.
        accuracy = sum(new_df['correct']) / len(new_df)
        scores += f'{split}: {accuracy}\n'

    # Print all scores to a file as well.
    with open(f'{processed_outputs}scores.txt', 'w') as file:
        file.write(scores)
    
    print(scores)
