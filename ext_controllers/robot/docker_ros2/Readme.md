### working on 

# pull images
docker pull osrf/ros:humble-desktop

# check the images
docker images 

docker run -it --network=host --name=ros2 osrf/ros:humble-desktop bash
docker exec -it ros2 ./ros_entrypoint.sh bash
docker ps


### in progress
# docker 
docker build .

docker ps
docker container ls

docker run --name "NAME" -it "image URL"

docker start <id> container 
docker stop <id> container 



