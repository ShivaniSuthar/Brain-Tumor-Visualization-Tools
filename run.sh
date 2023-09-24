
#!/bin/sh
if [ "$1" = "graphvis" ]; then
    docker build -t ucla_su23_work -f Dockerfile.graphvis .
    docker run -p 8050:8050 ucla_su23_work
elif [ "$1" = "demo" ]; then
    docker build -t ucla_su23_work -f Dockerfile.demo .
    docker run -p 5000:5000 -it ucla_su23_work
elif [ "$1" = "slicer" ]; then
    docker build -t ucla_su23_work -f Dockerfile.slicer .
    docker run -p 8069:8069 -it ucla_su23_work
else
    echo "Invalid service name."
fi
