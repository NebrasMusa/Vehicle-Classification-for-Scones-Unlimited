# Vehicle Classification for Scones Unlimited

## Project Overview
As a Machine Learning Engineer at Scones Unlimited, I developed an end-to-end image classification system to optimize delivery operations by automatically identifying courier vehicles (bicycles vs motorcycles). This enables intelligent routing—assigning bicycle couriers to nearby orders and motorcycle couriers to farther destinations.

## Technical Solution
Built on AWS cloud services, the solution features:

**Model Development**: Fine-tuned ResNet50 using PyTorch on SageMaker, trained on CIFAR-100 dataset (bicycle label 8, motorcycle label 48) with >90% accuracy.

**Serverless Architecture**: 
- Real-time inference via SageMaker endpoints
- AWS Lambda functions for image processing
- Step Functions orchestrating the classification workflow
- Automated routing decisions based on vehicle type

**Production Monitoring**: CloudWatch integration for performance tracking, latency monitoring (<500ms), and drift detection.

## Business Impact
The system significantly improves delivery efficiency by matching vehicle capabilities with order distances. The scalable AWS infrastructure ensures reliable performance during peak demand while maintaining cost efficiency through serverless pay-per-use models.

This portfolio-ready project demonstrates comprehensive MLOps expertise—from model development to production deployment—showcasing the ability to deliver business value through machine learning and cloud-native architecture.
