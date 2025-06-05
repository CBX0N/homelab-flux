# Homelab Flux

This repository serves as the foundation for a personal homelab environment, leveraging GitOps principles with [Flux CD](https://fluxcd.io/) to manage Kubernetes configurations. The setup integrates tools like Terraform for infrastructure provisioning and custom container images to support various services within the cluster.

## Overview

The homelab is designed to:

- Utilize Flux CD for continuous deployment and synchronization of Kubernetes manifests.
- Employ Terraform for declarative infrastructure management.
- Maintain custom container images tailored for specific services.
- Organize configurations per environment (e.g., development, production) for clarity and scalability.

## Repository Structure

```
homelab-flux/
├── clusters/
│   └── dev/                 # Environment-specific Kubernetes manifests
├── container-images/
│   └── iptables/            # Custom Dockerfiles and configurations
├── docker/
│   └── dns/                 # Docker-related configurations for DNS services
├── terraform/               # Infrastructure as Code configurations
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
```

## Prerequisites

Before deploying this homelab setup, ensure you have the following tools installed:

- [Flux CLI](https://fluxcd.io/docs/installation/)
- [Terraform](https://www.terraform.io/downloads)
- [Docker](https://www.docker.com/get-started)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/CBX0N/homelab-flux.git
   cd homelab-flux
   ```

2. **Set Up Infrastructure with Terraform:**

   Navigate to the `terraform/` directory and initialize Terraform:

   ```bash
   cd terraform
   terraform init
   terraform apply
   ```

   > *Note: Review and customize the Terraform configurations as needed before applying.*

3. **Build and Push Custom Container Images:**

   If you have custom services (e.g., `iptables`), build and push their Docker images:

   ```bash
   cd ../container-images/iptables
   docker build -t your-registry/iptables:latest .
   docker push your-registry/iptables:latest
   ```

4. **Bootstrap Flux:**

   Ensure your Kubernetes context is set to the target cluster, then bootstrap Flux:

   ```bash
   flux install
   kubectl create secret generic flux-system -n flux-system --from-file=identity=./flux-id --from-file=known_hosts=<(ssh-keyscan github.com)
   kubectl apply -f gotk-components.yaml
   kubectl apply -f gotk-sync.yaml
   ```

## Customization

- **Environment Configurations:** Modify the manifests under `clusters/dev/` to suit your environment's needs.
- **Infrastructure:** Adjust the Terraform scripts in the `terraform/` directory to match your infrastructure requirements.
- **Services:** Update or add Dockerfiles in `container-images/` and corresponding configurations in `docker/` for additional services.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
