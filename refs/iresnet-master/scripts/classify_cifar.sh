<<<<<<< HEAD
python ./CIFAR_main.py --nBlocks 7 7 7 --nStrides 1 2 2 --nChannels 32 64 128 --coeff 0.9 --batch 128 --dataset cifar10 --init_ds 1 --inj_pad 13 --powerIterSpectralNorm 1 --save_dir ./results/zca_clf_full_cifar10_wrn22_inj_pad_coeff09 --nonlin elu --optimizer sgd --vis_server localhost  --vis_port  8097 --resume 0 --epochs 200
=======
python ./CIFAR_main.py --nBlocks 7 7 7 --nStrides 1 2 2 --nChannels 32 64 128 --coeff 0.9 --batch 128 --dataset cifar10 --init_ds 1 --inj_pad 13 --powerIterSpectralNorm 1 --save_dir ./results/zca_clf_full_cifar10_wrn22_inj_pad_coeff09 --nonlin elu --optimizer sgd --vis_server localhost  --vis_port  8097 --resume 7 --epochs 10 --evaluate
>>>>>>> de56206e152ffdcd4259d319dd41f4f8441138cd
