export CUDA_VISIBLE_DEVICES='0'
export PYTORCH_HIP_ALLOC_CONF=garbage_collection_threshold:0.8,max_split_size_mb:512
python scripts/batch_inverse.py \
    --task_config='configs/random_box_outpainting_config_psld.yaml' \
    --inpainting=1 \
    --general_inverse=0 \
    --gamma=0.2 \
    --omega=1 \
    --baseline_model \
    --W=384 \
    --H=384 \
    --C=4 \
    --f=8 \
    --n_samples=2 \
    --ddim_steps=1000 \
    --dataset='Dataset' \
    --outdir='outputs/train'