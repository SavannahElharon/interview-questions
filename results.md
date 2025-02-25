Results for the Software Interview Problems
===

# Problem - 1

- C++ Docker Image

```
# Get the GCC preinstalled image from Docker Hub
FROM gcc

# Copy the current folder which contains C++ source code to the Docker image under /usr/src
COPY src /usr/src/src
COPY Makefile /usr/src/

# Specify the working directory
WORKDIR /usr/src/

# Use GCC to compile the Test.cpp source file
RUN make

# Run the program output from the previous step
CMD ["./target/lru_cpp"]
```

-  Python Docker Image

```
# Get the python3 preinstalled image from Docker Hub
FROM python:3
# Specify the working directory
WORKDIR /usr/src/app
# Copy the source code to the destination
COPY src/ .

# Run the program output from the previous step
CMD ["python","__init__.py"]
```

- Java Docker Image

```
# Get the GCC preinstalled image from Docker Hub
FROM maven:3.8.6-openjdk-11

# Specify the working directory
WORKDIR /usr/src/app
#copy pom.xml file
COPY pom.xml .

# Copy the current folder which contains C++ source code to the Docker image under /usr/src
COPY src ./src

# Use maven to package the jar assuming the tests passed
RUN mvn package clean package

# Run the program output from the previous step
CMD ["java", "-jar", "target/lru-java-0.0.1.jar"]
```

# Problem - 2

- C++ Build

```
sae65@tux4:~/momEdit/interview-questions/c++$ docker build -t lru-cpp .
[+] Building 1.5s (8/8) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 37B
 => [internal] load .dockerignore
 => => transferring context: 2B
 => [internal] load metadata for docker.io/library/gcc:latest
 => [1/3] FROM docker.io/library/gcc
 => [internal] load build context
 => => transferring context: 1.23kB
 => [2/3] COPY src /usr/src/src
 => [3/3] COPY Makefile /usr/src/
 => exporting to image
 => => exporting layers
 => => writing image sha256:...
 => => naming to docker.io/library/lru-cpp
```

- Java Build

```
sae65@tux4:~/momEdit/interview-questions/java$ docker build -t lru-java .
[+] Building 2.3s (8/8) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 37B
 => [internal] load .dockerignore
 => => transferring context: 2B
 => [internal] load metadata for docker.io/library/maven:3.8.6-openjdk-11
 => [1/3] FROM docker.io/library/maven:3.8.6-openjdk-11
 => [internal] load build context
 => => transferring context: 1.23kB
 => [2/3] COPY pom.xml .
 => [3/3] COPY src ./src
 => exporting to image
 => => exporting layers
 => => writing image sha256:...
 => => naming to docker.io/library/lru-java
```

- Python Run

```
sae65@tux4:~/momEdit/interview-questions/python$ docker build -t lru-python .
[+] Building 1.2s (7/7) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 37B
 => [internal] load .dockerignore
 => => transferring context: 2B
 => [internal] load metadata for docker.io/library/python:3
 => [1/2] FROM docker.io/library/python:3
 => [internal] load build context
 => => transferring context: 1.23kB
 => [2/2] COPY src/ .
 => exporting to image
 => => exporting layers
 => => writing image sha256:...
 => => naming to docker.io/library/lru-python
```

# Problem - 3

- C++ Docker Run Output

```
sae65@tux4:~/momEdit/interview-questions/c++$ docker run lru-cpp
5 4 1 3
```

- Java Docker Run Output

```
sae65@tux4:~/momEdit/interview-questions/java$ docker run lru-java
5 4 1 3
```

- Python Docker Run Output

```sae65@tux4:~/momEdit/interview-questions/python$ docker run lru-python
5 4 1 3
```
