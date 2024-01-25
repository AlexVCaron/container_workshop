# Containers and images

**What is an image ?**

> An image is a read-only template with instructions for creating a Docker container. 

This does not talk a lot, in simpler words :

> An image is a cooking recipe for an ensemble of softwares, executables, libraries and datasets

What an image is not : **A CONTAINER**. You cannot execute code or get files in it. You can pre-bake it; that's what we do when we call `docker build`.

**What is a container ?**

> A container is a runnable instance of an image, equipped with a filesystem, drivers to peripherals and possibly a network interface.

A container is :
- a running process
- isolated from the host system
- resource controlled (CPU, GPU, memory, disk space, network)
- ephemeral (it can be destroyed and recreated at will)
- portable (it can be moved to another host and run there)
