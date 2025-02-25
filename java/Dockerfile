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
