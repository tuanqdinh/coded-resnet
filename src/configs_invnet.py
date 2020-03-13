"""
	@author Tuan Dinh tuandinh@cs.wisc.edu
	@date 08/14/2019
	Loading data
"""

import argparse

parser = argparse.ArgumentParser(description='Train i-ResNet on Cifar')

# --nBlocks 7 7 7 --nStrides 1 2 2 --nChannels 32 64 128 --coeff 0.9 --batch 128 --init_ds 1 --inj_pad 0 --powerIterSpectralNorm 5 --nonlin elu --optimizer sgd --vis_server localhost  --vis_port 8097
# data and paths
parser.add_argument('--nBlocks', nargs='+', type=int, default=[7, 7, 7])
parser.add_argument('--nStrides', nargs='+', type=int, default=[1, 2, 2])
parser.add_argument('--nChannels', nargs='+', type=int, default=[32, 64, 128])
parser.add_argument('--inj_pad', default=0, type=int, help='initial inj padding')
parser.add_argument('--coeff', default=0.9, type=float, help='contraction coefficient for linear layers')
parser.add_argument('--lr', default=0.1, type=float, help='learning rate')

# training
parser.add_argument('--batch', default=128, type=int, help='batch size')

parser.add_argument('--init_batch', default=1024,
                    type=int, help='init batch size')
parser.add_argument('--init_ds', default=2, type=int,
                    help='initial downsampling')
parser.add_argument('--warmup_epochs', default=10,
                    type=int, help='epochs for warmup')
parser.add_argument('--epochs', default=200, type=int, help='number of epochs')


parser.add_argument('--model_name', default='model', type=str, help='dataset')
parser.add_argument('--data_root', default='../data/')
parser.add_argument('--dataset', default='cifar10', type=str, help='dataset')
parser.add_argument('--save_dir', default='../results/iresnet',
                    type=str, help='directory to save results')
parser.add_argument('--log_steps', type=int, default=30)
parser.add_argument('--save_steps', type=int, default=10)
# modes
parser.add_argument('-densityEstimation', '--densityEstimation', dest='densityEstimation',
                    action='store_true', help='perform density estimation')
parser.add_argument('--eval_sensitivity', action='store_true')
parser.add_argument('--eps', default=0.01, type=float)
parser.add_argument('--eval_invertibility', action='store_true')
parser.add_argument('--generate_fused_image', action='store_true')
parser.add_argument('--eval_fusion_net', action='store_true')
parser.add_argument('--test_inversed_images', action='store_true')
parser.add_argument('--plot_tnse', action='store_true')

parser.add_argument('-e', '--evaluate', dest='evaluate', action='store_true',
                    help='evaluate model on validation set')
parser.add_argument('-interpolate', '--interpolate',
                    dest='interpolate', action='store_true', help='train iresnet')
parser.add_argument('-norm', '--norm', dest='norm', action='store_true',
                    help='compute norms of conv operators')
parser.add_argument('-analysisTraceEst', '--analysisTraceEst', dest='analysisTraceEst', action='store_true',
                    help='analysis of trace estimation')

# optimization
parser.add_argument('--optimizer', default="adam", type=str,
                    help="optimizer", choices=["adam", "adamax", "sgd"])
parser.add_argument('--weight_decay', default=5e-4,
                    type=float, help='coefficient for weight decay')
parser.add_argument('--drop_rate', default=0.1,
                    type=float, help='dropout rate')
parser.add_argument('-drop_two', '--drop_two', dest='drop_two',
                    action='store_true', help='2d dropout on')
parser.add_argument('-nesterov', '--nesterov', dest='nesterov', action='store_true',
                    help='nesterov momentum')

parser.add_argument('--niter', type=int, default=200, help='# of iter at starting learning rate')
parser.add_argument('--niter_decay', type=int, default=200, help='# of iter to linearly decay learning rate to zero')
parser.add_argument('--lr_policy', type=str, default='lambda', help='learning rate policy: lambda|step|plateau|cosine')
parser.add_argument('--lr_decay_iters', type=int, default=50, help='multiply by a gamma every lr_decay_iters iterations')
parser.add_argument('--epoch_count', type=int, default=1, help='the starting epoch count')

# models

parser.add_argument('--numTraceSamples', default=1, type=int,
                    help='number of samples used for trace estimation')
parser.add_argument('--numSeriesTerms', default=1, type=int,
                    help='number of terms used in power series for matrix log')
parser.add_argument('--powerIterSpectralNorm', default=5, type=int,
                    help='number of power iterations used for spectral norm')

# networks
parser.add_argument('-multiScale', '--multiScale', dest='multiScale', action='store_true', help='use multiscale')
parser.add_argument('-fixedPrior', '--fixedPrior', dest='fixedPrior', action='store_true',
                    help='use fixed prior, default is learned prior')
parser.add_argument('-noActnorm', '--noActnorm', dest='noActnorm', action='store_true',
                    help='disable actnorm, default uses actnorm')
parser.add_argument('--nonlin', default="elu", type=str,
                    choices=["relu", "elu", "sorting", "softplus"])


# flags
parser.add_argument('--debug', action='store_true',
                    help='debug')
parser.add_argument('--flag_retrain', action='store_true',
                    help='resume')
parser.add_argument('--flag_test', action='store_true',
                    help='test')
parser.add_argument('--resume', default='', type=str, metavar='PATH',
                    help='path to latest checkpoint (default: none)')
parser.add_argument('--resume_g', default='', type=str, metavar='PATH',
                    help='path to latest checkpoint (default: none)')
parser.add_argument('--flag_reg', action='store_true')


# servers
parser.add_argument('--vis_port', default=8097,
                    type=int, help="port for visdom")
parser.add_argument('--vis_server', default="localhost",
                    type=str, help="server for visdom")

# others
parser.add_argument('--log_every', default=10,
                    type=int, help='logs every x iters')
parser.add_argument('-log_verbose', '--log_verbose', dest='log_verbose', action='store_true',
                    help='verbose logging: sigmas, max gradient')
parser.add_argument('-deterministic', '--deterministic', dest='deterministic', action='store_true',
                    help='fix random seeds and set cuda deterministic')
parser.add_argument('--extension', default='.npy', type=str, help='extension')

### mixup
parser.add_argument('--mixup_alpha', default=1, type=float, help='dropout rate')
parser.add_argument('--mixup', action='store_true')
parser.add_argument('--mixup_hidden', action='store_true')
parser.add_argument('--flag_combined_loss', action='store_true')

# Model parameters
args = parser.parse_args()
# print(args)