# Terraform AWS Infrastructure Automation

Hands-on infrastructure provisioning using Terraform on AWS. Covers lifecycle workflows, provider configurations, VPC networking, security groups, subnets, and variable abstractions (lists and dictionary objects).

## Contents
- [setup.md](./setup.md) — step-by-step setup walkthrough, credential routing, deployment guides, and teardown instructions
- [commands.md](./commands.md) — standard CLI execution workflows and state tracking logs

## Projects
| Directory | Description |
|---|---|
| `projects/aws-website-infra` | Production-ready infrastructure blueprint deploying isolated network topographies for secure application hosting |

## Manifests & Configurations
| File | Description |
|---|---|
| `main.tf` | Primary orchestration manifest defining AWS providers, state transitions, subnets, VPC parameters, and security filtering groups |
| `terraform.tfvars` | Input variable definition file handling isolated runtime environments through lists and nested dictionary block objects |