# Config for simple baseline of only one transformer block.
wandb_log = True
wandb_project = 'RecursiveGPT'
wandb_run_name='gpt_l1'

out_dir = f"out/{wandb_run_name}"
dataset = 'shakespeare_char'
batch_size = 64
block_size = 256 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 1
n_head = 6
n_embd = 384
dropout = 0.

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 1000
eval_interval = 250
decay_lr = False

compile = False
device = 'cuda:0'