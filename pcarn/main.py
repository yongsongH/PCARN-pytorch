import json
import argparse
import importlib

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="pcarn")
    parser.add_argument("--ckpt_dir", type=str, default="./checkpoint/pcarn")
    parser.add_argument("--train_data", type=str, default="./dataset/DIV2K.h5")

    parser.add_argument("--memo", type=str, default="")
    parser.add_argument("--num_gpu", type=int, default=1)
    parser.add_argument("--print_interval", type=int, default=1000)

    parser.add_argument("--scale", type=int, default=0)
    parser.add_argument("--num_channels", type=int, default=64)
    parser.add_argument("--init_type", type=str, default="default")
    parser.add_argument("--init_scale", type=float, default=1.0)

    parser.add_argument("--patch_size", type=int, default=48)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--max_steps", type=int, default=600000)
    parser.add_argument("--decay", type=int, default=400000)
    parser.add_argument("--lr", type=float, default=0.0001)
    parser.add_argument("--clip", type=float, default=10.0)

    # for mobile version
    parser.add_argument("--mobile", action="store_true", default=False)
    parser.add_argument("--group", type=int, default=1)

    # for perceptual model
    parser.add_argument("--perceptual", action="store_true", default=False)
    parser.add_argument("--pretrained_ckpt", type=str)
    parser.add_argument("--gamma_vgg", type=float, default=1.0)
    parser.add_argument("--gamma_gan", type=float, default=5e-3)
    parser.add_argument("--msd", action="store_true", default=False)

    return parser.parse_args()

def main(config):
    # dynamic import using --model argument
    module = importlib.import_module("model.{}".format(config.model))
    print(json.dumps(vars(config), indent=4, sort_keys=True))

    if config.perceptual:
        from solver_gan import Solver
    else:
        from solver import Solver

    solver = Solver(module, config)
    solver.fit()

if __name__ == "__main__":
    args = parse_args()
    main(args)
