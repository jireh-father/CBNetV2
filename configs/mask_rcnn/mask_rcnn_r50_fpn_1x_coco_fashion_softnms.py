_base_ = [
    '../_base_/models/mask_rcnn_r50_fpn_fashion.py',
    '../_base_/datasets/coco_instance_fashion.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

model = dict(
    test_cfg=dict(
        rcnn=dict(
            score_thr=0.001,
            nms=dict(type='soft_nms'),
        )
    )
)
