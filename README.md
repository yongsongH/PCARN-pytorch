# Efficient Deep Neural Network for Photo-realistic Image Super-Resolution
Namhyuk Ahn, Byungkon Kang, Kyung-Ah Sohn. [[arXiv](https://arxiv.org/abs/1903.02240)]

## Requirements
- Python 3
- [PyTorch](https://github.com/pytorch/pytorch) (1.0.0), [torchvision](https://github.com/pytorch/vision)
- Numpy, Scipy
- Pillow, Scikit-image
- h5py
- importlib
- [PerceptualSimilarity](https://github.com/richzhang/PerceptualSimilarity)

## Dataset
We use the same protocols of CARN, our prior work. Please see the details on this [repo](https://github.com/nmhkahn/CARN-pytorch#dataset).


1. Download [DIV2K](https://data.vision.ee.ethz.ch/cvl/DIV2K) and unzip on `dataset` directory as below:
  ```
  dataset
  └── DIV2K
      ├── DIV2K_train_HR
      ├── DIV2K_train_LR_bicubic
      ├── DIV2K_valid_HR
      └── DIV2K_valid_LR_bicubic
 ```    
 🙌 Download [MURA](https://figshare.com/articles/dataset/Rethinking_Degradation_Radiograph_Super-Resolution_via_AID-SRGAN_Dataset_/20418036/3) and unzip on `dataset` directory as below (x4):
  ```
  dataset
  └── MURA
      ├── MURA_SR_GT
      ├── MURA_mini_X4
      ├── MURA_Test_HR
      └── MURA_LR_X4
  ```

## Test models on given directory
To test on given image directory,
```shell
$ python pcarn/inference_dir.py \
    --model pcarn \
    --ckpt ./checkpoints/<path>.pth \
    --data_root <dataset_root> \
    --scale [2|3|4] \
    --save_root <sample_dir_root>
```
More argument details are on the below section.

## Test models on benchmark dataset
We provide the pretrained models in the `checkpoints` directory. To test the PCARN on benchmark dataset:
```shell
# For PCARN and PCARN (L1)
$ python pcarn/inference.py \
    --model pcarn \
    --ckpt ./checkpoints/<path>.pth \
    --data ./dataset/<dataset> \
    --scale [2|3|4] \
    --sample_dir <sample_dir>

# For PCARN-M and PCARN-M (L1)
$ python pcarn/inference.py \
    --model pcarn \
    --ckpt ./checkpoints/<path>.pth \
    --data ./dataset/<dataset> \
    --scale [2|3|4] \
    --sample_dir <sample_dir> \
    --mobile --group 4
```
We provide our results on four benchmark dataset (Set5, Set14, B100 and Urban100). [Google Drive](https://drive.google.com/file/d/1rDUNFt_1mJZTBWd6bK460ZOeHfUqQZBY/view?usp=sharing)

### Training models
Before train the PCARN(-M), models have to be pretrained with L1 loss.
```shell
# For PCARN (L1)
python pcarn/main.py \
    --model pcarn \
    --ckpt_dir ./checkpoints/<save_directory> \
    --batch_size 64 --patch_size 48 \
    --scale 0 --max_steps 600000 --decay 400000 \
    --memo <message_shown_in_logfile>

# For PCARN-M (L1)
python pcarn/main.py \
    --model pcarn \
    --ckpt_dir ./checkpoints/<save_directory> \
    --mobile --group 4 \
    --batch_size 64 --patch_size 48 \
    --scale 0 --max_steps 600000 --decay 400000 \
    --memo <message_shown_in_logfile>
```

Train the PCARN(-M) using below commands. Note that [PerceptualSimilarity](https://github.com/richzhang/PerceptualSimilarity) has to be ready to evaluate the model performance during training.
```
# For PCARN
python pcarn/main.py \
    --model pcarn \
    --ckpt_dir ./checkpoints/<save_directory> \
    --perceptual --msd \
    --pretrained_ckpt <pretrained_model_path> \
    --batch_size 32 --patch_size 48 \
    --scale 0 --max_steps 600000 --decay 400000 \
    --memo <message_shown_in_logfile>
    
# For PCARN-M
python pcarn/main.py \
    --model pcarn \
    --ckpt_dir ./checkpoints/<save_directory> \
    --perceptual --msd \
    --pretrained_ckpt <pretrained_model_path> \
    --mobile --group 4 \
    --batch_size 32 --patch_size 48 \
    --scale 0 --max_steps 600000 --decay 400000 \
    --memo <message_shown_in_logfile>
```

## Results
![](./assets/fig_visual_perception.png)

## Citation
```
@article{ahn2019efficient,
  title={Efficient Deep Neural Network for Photo-realistic Image Super-Resolution},
  author={Ahn, Namhyuk and Kang, Byungkon and Sohn, Kyung-Ah},
  journal={arXiv preprint arXiv:1903.02240},
  year={2019}
}
```
