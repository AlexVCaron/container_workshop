# Using the scilus image to develop

Using the scilus image as a backend for development is way easier than you think. We can use it just like we used `Ubuntu` as an image against which to build the devcontainer.

However, as you'll see, we'll go even further.

1. The scilus image is quite bare and we need to install things for the build to go well :

    - Go in the Dockerfile and replace the source image with `scilus/scilus:1.6.0`
    - Remove everything after
    - Add the following lines :

        ```dockerfile
        RUN apt update && apt install -y git
        RUN apt update && apt install -y python3-venv
        RUN apt update && apt install -y wget
        ```

2. Open the current folder in the devcontainer by clicking on the bottom left corner of the VS Code window, where it says `><` and selecting `Reopen in Container`, or using the command palette (CTRL+SHIFT+P) and selecting `Reopen in Container`

3. Test commands of software usually available in `scilus:1.6.0` :

    - ANTs, FSL, Mrtrix are all available
    - Try any scilpy script !

4. We'll now add some VS Code extensions, for fun ! Add the following to the `devcontainer.json` file :

    ```json
    "extensions": [
        "GitHub.vscode-pull-request-github",
        "ms-azuretools.vscode-docker",
        "ms-python.isort",
        "ms-python.vscode-pylance",
        "yzhang.markdown-all-in-one"
    ]
    ```

6. Using the command palette or in the bottom left, trigger a rebuild of the devcontainer. Enjoy the extensions !

7. Lastly, we'll add an instruction to tell docker to create and mount a volume in the container to manage datasets. The reasons :
    - Everything outside `/workspaces` is destroyed between container builds, but not what we put in a volume
    - Everything we add to the image makes the container grow, it could be better to control it
    - Data in a volume is shareable between containers

    Add the following to the `devcontainer.json` file :

    ```json
    "mounts": [
        {"source": "container-workshop-volume", "target": "/workshop_volume", "type": "volume"}
    ]
    ```

8. Rebuild the devcontainer and open a terminal in VS Code.

    - You can now see the volume in `/workshop_volume` and use it to store data.
    - A cool way to interact with the folder in VS Code is adding it to the workspace. In the top menu, click on `File > Add Folder to Workspace...` and select `/workshop_volume`.

## Going even further

We have everything *Scilpy*, but what if we want to run, let's say, *Nextflow* pipelines ?

1. Add the following under features in the `devcontainer.json` file :

    ```json
    "ghcr.io/robsyme/features/nextflow:1": {}
    ```

2. Use mounts to bind to your input and output folders

3. Add the following to the `devcontainer.json` file :

    ```json
    "mounts": [
        {"source": "pipeline-x-input", "target": "/pipeline-x_input", "type": "volume"},
        {"source": "pipeline-x-output", "target": "/pipeline-x_output", "type": "volume"}
    ]
    ```

4. Rebuild the devcontainer to install nextflow and so the volumes get created by docker

4. Place the datasets for input in the volume `pipeline-x-input` through the VS Code interface or using :

    ```bash
    docker cp <dataset> <vs-code-container-name>:/pipeline-x_input
    ```

5. Run your pipeline in VS Code using the terminal
