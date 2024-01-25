
# Containers workshop

## Requirements

This workshop is intended for people with a little to no experience with containers. It will cover the basics of containers, how to use them, how to build them and how they integrate in development environments such as Visual Studio Code.

**You must have at least 50GiB of free space on your computer to be able to follow this workshop, as images will be downloaded and built using Docker**

## Pre-installation

This workshop uses the following technologies, that you need to install prior to the workshop on your computer (installation procedure can change from an OS to antoher) :

- [Docker Desktop](https://www.docker.com/products/docker-desktop) : you can install only [docker](https://docs.docker.com/engine/install/), but now Docker Desktop is available for all OSes. It gives you all the features of the docker engine, but is way easier to configure, inspect and debug since there is a good GUI, with commuity developed extensions. It is my opinion that if you are using Docker through CLI right now, you should have Docker Desktop installed as well for all supporting features.
- [Visual Studio Code](https://code.visualstudio.com/) : has the best support for development in containers and a lot of extensions to streamline the development process.

Once Docker Desktop is installed and running, open the terminal and download the following images :

```bash
docker pull scilus/scilus:1.6.0
docker pull alpine:latest
docker pull ubuntu:jammy-20230301
```

## Workshop

### 1 - [What are containers ? Is it an image ? What do they do ? (5 min)](docs/1-containers-images.md)

### 2 - [Creating my first image recipe (2min)](docs/234-first-image.md)

### 3 - [Building my first image (5 min)](docs/234-first-image.md)

### 4 - [Running my first container (5 min)](docs/2-3-4-first-image.md)

### 5 - [Launching VS Code in my container (5 min)](docs/5-vscode-devcontainer.md)

### 6 - [Using scilus as a VS Code development backend (30 min)](docs/6-scilus-dev-backend.md)
