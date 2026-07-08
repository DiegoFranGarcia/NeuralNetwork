## CI/CD
| Trigger | Workflow | Jobs |
|---|---|---|
| None found | None | None |

## Environment Variables
| Name | Required | Purpose |
|---|---|---|
| None documented | No | N/A |

## Local Dev
1. pip install -r requirements.txt
2. python src/train.py --epochs 20 --batch-size 32 --lr 0.001
3. python src/evaluate.py --checkpoint checkpoints/best_model.pt
4. python src/predict.py --image path/to/image.jpg --checkpoint checkpoints/best_model.pt
5. pytest tests/

## Deployment
Deploy: Not documented
