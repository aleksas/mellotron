import argparse
from os.path import join
actors = ["Aiste", "Edvardas", "Regina", "Vladas"]

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--dir', type=str, default='./MII_LIEPA_SYN_V1/', help='wav dir')
parser.add_argument('--output-dir', type=str, default='./filelists/', help='wav dir')

args = parser.parse_args()
print(args.dir)

filelists = {
    'train':[],
    'val':[]    
}


for a, actor in enumerate(actors):
    actor_dir = join(args.dir, actor)
    db_tr = join(actor_dir, 'db_tr.txt')
    
    with open(db_tr, 'rt', encoding='utf-8') as tfp:
        lines = [l.strip() for l in tfp.readlines()]
        th = int(len(lines) * 0.95)
        for i, line in enumerate(lines):
            if line:
                fn = join(args.dir, actor, 'data', str(i) + '.wav')
                nl = '|'.join([fn, line, str(a)]) + '\n'
                (filelists['train'] if i <= th else filelists['val'] ).append(nl)
    
for k, v in filelists.items():
    flist_path = join(args.output_dir, 'liepa_' + k + '_filelist.txt')
    with open(flist_path, 'wt', encoding='utf-8') as ofp:
        ofp.writelines(v)