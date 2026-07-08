## CI/CD
| Trigger | Workflow | Jobs |
|---|---|---|
| None | None | None (no .github/workflows found) |

## Environment Variables
| Name | Required | Purpose |
|---|---|---|
| None | No | Not documented |

## Local Dev
1. git clone https://github.com/DiegoFranGarcia/NeuralNetwork.git
2. cd NeuralNetwork
3. pip install -r requirements.txt
4. python src/train.py --epochs 20 --batch-size 32 --lr 0.001
5. python src/evaluate.py --checkpoint checkpoints/best_model.pt
6. python src/predict.py --image path/to/image.jpg --checkpoint checkpoints/best_model.pt

## Deployment
Deploy: Not documented