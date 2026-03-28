## Description
AI agent learns to classify emails into urgent, normal, spam.

## Actions
- urgent
- normal
- spam

## Rewards
+1 correct classification
-0.5 wrong classification

## Tasks
- Easy: keyword-based
- Medium: partial logic
- Hard: random baseline

## Run
docker build -t email-env .
docker run email-env

copyright by Harsh Golhani
