# Ansible Infrastructure Automation

Hands-on multi-OS configuration management using Ansible. Covers bootstrapping, user provisioning, ad-hoc execution, distribution-specific conditionals, variable abstraction, and modular roles.

## Contents
- [setup.md](./setup.md) — full lab setup walkthrough and configuration steps
- [commands.md](./commands.md) — ad-hoc command reference and Ansible cheat sheet
- [tmux-script.sh](./tmux-script.sh) — automation script to split tmux windows for the target lab VMs

## Playbooks & Configurations
| File | Description |
|---|---|
| `ansible.cfg` | Default configurations setting inventory paths, SSH keys, and Python interpreters |
| `inventory` | Production static host file grouping managed servers by distinct network profiles |
| `bootstrap.yml` | Base play initializing the environment: runs multi-OS package upgrades, creates administrative user keys, and configures passwordless sudo elevation |
| `install_apache.yml` | Simple, single-host sequential implementation to install and start the Apache service |
| `install_apache_v2.yml` | Refactored Apache play adding handlers to restart the service only upon asset mutation |
| `install_apache_v3.yml` | Multi-OS conditional play introducing distribution checks (`apt` for Ubuntu vs `dnf` for CentOS) |
| `install_apache_v4.yml` | Abstracted play replacing redundant system tasks with a single, parameter-driven package block |
| `remove_apache.yml` | Uninstallation playbook cleanly removing server packages, configurations, and document roots |
| `site_v1.yml` | Complete structural deployment utilizing raw independent files instead of roles |
| `site_v2.yml` | Playbook scaling out logic across target node layers including database, web, and file servers |
| `site_v3.yml` | Playbook targeting specific host structures to safely ignore missing platform parameters |
| `site_v4.yml` | Playbook optimized with dedicated pre-tasks to handle initial setup procedures on individual clusters |
| `site_v5.yml` | Advanced modular infrastructure mapping using unified include directories and configuration paths |
| `site_v6.yml` | The final production iteration leveraging discrete, reusable Ansible Roles |

## Roles
| Directory | Description |
|---|---|
| `roles/base` | Baseline hardening rule: Updates packages, injects global wheel groups, and deploys custom distribution-specific SSH templates (`sshd_config_arch.j2`, `sshd_config_centos.j2`, `sshd_config_ubuntu.j2`) |
| `roles/web_servers` | Installs HTTP daemons and PHP runtimes, copies index assets, alters firewall restrictions (`firewalld` vs `ufw`), and enables system services |
| `roles/db_servers` | Provisions isolated relational engine parameters, installs database dependencies, and configures MariaDB packages |
| `roles/file_servers` | Automates file hosting workflows, installs target dependencies, and deploys network file systems on Arch Linux nodes |
| `roles/workstations` | Provisions operations profiles, updates local package manager trees, and downloads infrastructure tooling engines |