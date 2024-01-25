# Using devcontainers in VSCode

Visual Studio Code has a very good support for containers, and it is very easy to use. For VS Code, a devcontainer is a full development environment, with all the tools and dependencies needed to develop a project.

## 1 - Useful commands in VS Code

Commands are accessed using the palette (CTRL+SHIFT+P); those specific to devcontainers are prefixed with `Dev Containers`.

- *Add Dev Container Configuration Files ...* : create a new devcontainer recipe with pre-built templates and comprehensive user interface
- *Attach to running container* : attach to a container already running in Docker
- *Reopen in Container* : reopen the current folder in a container (must have a devcontainer recipe)
- *Rebuild and Reopen in Container* : rebuild the current devcontainer recipe and reopen the folder in the container (useful when checking out or pulling changes to the recipe)

## 2 - Create a devcontainer recipe

1. Open the command palette (CTRL+SHIFT+P) and select `Dev Containers: Add Dev Container Configuration Files ...`, add the configuration to workspace

2. Select `Ubuntu` as the template and choose jammy

3. Select `pre-installed` devcontainer features to be included

    - git (from source)
    - Docker (docker-in-docker)

3. Choose to keep the default options

4. You now have a devcontainer recipe, which should have opened automatically. It is located in `.devcontainer/devcontainer.json`.

6. Change the `image` to `ubuntu:jammy-20230301`

5. Open the current folder in the devcontainer by clicking on the bottom left corner of the VS Code window, where it says `><` and selecting `Reopen in Container`, or using the command palette (CTRL+SHIFT+P) and selecting `Reopen in Container`

## 3 - Preinstall tools in the devcontainer

There is 2 ways to preinstall tools in the devcontainer:

- using the `postCreateCommand` option in the devcontainer.json file, you provide a command or a script to be executed
- using a Dockerfile instead of specifying an image

A good thing to note : the `Dockerfile` is executed before everything else gets built, the `postCreateCommand` is executed after.

## 4 - Using the Dockerfile

1. Copy the Dockerfile, scripts and entrypoints created in the previous section to the `.devcontainer` folder

2. In the Dockerfile :
    - On the first line, replace `FROM alpine:latest` with `FROM ubuntu:jammy-20230301`
    - Remove the call to `apk add --no-cache bash`
    - For the other calls, replace `apk add --no-cache` with `apt update && apt-get install -y`

3. In the `devcontainer.json` file and replace `"image": ...` with `"build": { "dockerfile": "Dockerfile" }`

4. Rebuild the devcontainer, open a terminal and launch `python3 /resources/print_infos_inside_container.py` in the terminal
