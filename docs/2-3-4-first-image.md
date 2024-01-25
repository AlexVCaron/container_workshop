# My first image and container

## 1- Preparing the context and the image

We will create a simple image that will run a python script. We will use the `alpine` image as a base, install some dependencies and add a python script and an entrypoint to prepare it's environment.

1. Create a folder named `my-first-image` and open it in VS Code.
2. Create a file named `Dockerfile` and add the following content :

    ```dockerfile
    FROM alpine:latest

    RUN apk add --no-cache python3
    RUN apk add --no-cache bash
    RUN python3 -m venv /cool-workshop-venv

    COPY entrypoint.sh /entrypoint.sh

    ENTRYPOINT ["/entrypoint.sh"]
    ```

3. Create a file named `entrypoint.sh` and add the following content :

    ```bash
    #!/bin/sh

    source /cool-workshop-venv/bin/activate
    python3 /print_infos_inside_container.py
    ```

4. Copy the file `print_infos_inside_container.py` from the `resources` folder to the `my-first-image` folder.

5. Add the following line to the dockerfile to copy the python script to the image :

    ```dockerfile
    COPY print_infos_inside_container.py /print_infos_inside_container.py
    ```

## 2 - Build and inspect the image

1. Open the terminal in VS Code and build the image :

    ```bash
    docker build -t my-first-image .
    ```

2. Run docker with the image, through the entrypoint :

    ```bash
    docker run --rm my-first-image
    ```

3. Inspect the content of the image :

    ```bash
    docker run --rm -it --entrypoint "/bin/bash" my-first-image
    ```

Without realizing we created our first container as well ! For now, when we exit the container, it is destroyed (because of `--rm`). Keeping it alive is easy, but then we need to find it again to reuse or destroy it later.

## 3 - Run my first container

1. Create a container that will stay alive :

    - Replace the content of the entrypoint with `sleep infinity`
    - Rebuild the container using the previous command

2. Run the container in the background :

    ```bash
    docker run --name my-first-container -d my-first-image
    ```

3. The container is now alive and awaiting for you to interact with it. You can see it in the list of containers :

    ```bash
    docker ps -a
    ```

4. Reattach to the container :

    ```bash
    docker exec -it my-first-container /bin/bash
    ```

4. Exit the container and remove it :

    ```bash
    docker stop -s 9 my-first-container
    docker rm my-first-container
    ```
