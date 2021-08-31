_base_ = './htc_without_semantic_r50_fpn_1x_coco_fashion.py'

model = dict(
    test_cfg=dict(
        rcnn=dict(
            score_thr=0.001,
            nms=dict(type='soft_nms'),
        )
    )
)