export CUDA_VISIBLE_DEVICES='0'
export PYTORCH_HIP_ALLOC_CONF=garbage_collection_threshold:0.8,max_split_size_mb:512
python scripts/inverse.py \
    --file_id='00014.png' \
    --prompt='Baby Face' \
    --task_config='configs/box_inpainting_config_psld.yaml' \
    --inpainting=1 \
    --general_inverse=0 \
    --gamma=1e-1 \
    --omega=1e-1 \
    --baseline_model \
    --W=512 \
    --H=512 \
    --C=4 \
    --f=8 \
    --outdir='outputs/psld-ldm-samples-bip'