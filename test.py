from util import read_jsonl, set_random_seed, fix_tokenizer


# with open('../../config/train_data/kosmos_train.jsonl', 'r', encoding='utf8') as json_file:
#     train_records = list(json_file)
    
train_records = list(read_jsonl('../../config/train_data/kosmos_train.jsonl'))

print(train_records)