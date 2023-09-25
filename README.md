# BRAIN_TUMOR_VISUALIZATION_TOOLS



![download](https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/9c5a1cdf-7fbb-43d3-91f4-fa7a512c1a33)

# About
This repository contains code that creates visualizations which aid in the research and treatment for individuals affected by metastatic brain tumors.

# Applications & Code Organization
All the code for this project is contained within the "UCLA_SU23_Work" folder. There are 3 main folders within UCLA_SU23_Work:

1) "Demo"
2) "Graphvis"
3) "Slicer"

#### Demo: #### 
The demo folder contains a python file, "Codefile.py", in which I modified existing code that launched a 3D interactive brain viewer to include a drop-down menu that contains the options "Lung", "Breast", "Kidney", "Melanoma", and "Colorectal". When applied to real-world patient data, this drop down menu would allow users to see how these different types of cancers have metastasized in patient's brains. For example, when a user clicks on "lung", the 3D brain that appears in the interactive viewer will display areas in the brain affected by tumors for lung cancer patients only. In order to interact with the visualization, a user can click on the brain and move it around with their mouse to see different areas of it. The image below displays the brain viewer when "lung" is selected using randomized data. However, when real-patient data is fed in, the delineations between the tumorous and non-tumorous regions should become more clear.

Expected output if "demo" is ran correctly: 
<img width="960" alt="demo_image_1" src="https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/a0ba15a5-36d0-42c0-947a-9eaeff2a8a3e">

Lastly, the original code I modified can be found at this link: 
https://gallantlab.org/pycortex/auto_examples/webgl/multiple_datasets.html#sphx-glr-auto-examples-webgl-multiple-datasets-py


#### Graphvis: #### 
The graphvis folder contains an initializer file, "init.py" and the main code file, "app.py". This file contains code that launches an interactive x-y axis and linear graph. When combined with the "demo" tool and patient data, this graphing framework can be utilized to graph various relationships involving tumor type and tumor location. For example, a user can click on a specific location in the "demo" 3D viewer and can manipulate the graphing tool to graph a desired relationship. These two features are shown below:

Selecting a specific location in "demo":
<img width="960" alt="demo_image_2" src="https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/7f1acf33-58b8-4b6e-b3bd-01c861ec62f2">










Expected output if "graphvis" is ran correctly:
<img width="960" alt="graphvis_image_1" src="https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/024eb407-bd8d-4807-815f-907af3d7edcb">


#### Slicer: #### 
The slicer folder contains an "assets" folder, a "brain_images" folder, and a "MNIST_data" folder. It also contains 5 code files - the initializer file ("init.py"), "main.py", "main2.py", "main3.py", and "MNIST_images.ipynb." 
- In main.py, I used existing code that launched an interactive 3D animation of slices of a brain scan but I modified the code to run using Dash. The pause/play buttons can be used to view different layers of the brain scan and the x, y, z coordinates specify the location in the brain scan the user is hovering over. The brain image used in the animation is contained in the "attention-mri.tif" file in the "assets" folder.

  Expected output if "main" is ran correctly:


<img width="370" alt="main_image1" src="https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/97ac6101-a70a-4aaa-af96-c1e8f8d013e1">

  
- Main2.py launches the same animation as main.py except it incorporates a tooltip to show different images in the hover textbox of the brain animation based on the x-value the user is currently hovering on. Specifically, if the user is hovering on x-values [0:50], it displays "Image1.jpg". If the user is hovering on x-values [51:100], it displays "Image2.jpg". Lastly, if the user is hovering on x-values 101 or greater, it displays "Image3.jpg". These 3 images can be found in the "brain_images" folder.

  Expected output if "main2" is ran correctly:

<img width="959" alt="main2_image1" src="https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/f70370a6-bcca-4037-a5b6-e6d3012ae785">

- Main3.py is similar to main2.py but it displays a different image for every possible x-value a user can hover over (values 0-155). These images are saved in the "MNIST_data" folder which were drawn from the "mini-mnist-1000.pickle" file and converted to jpeg images using code found in the "MNIST_images.ipynb" file.

  Expected output if "main3" is ran correctly:

  <img width="959" alt="main3_image1" src="https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/e335b868-052f-434f-b6b5-152f1aa0a1b5">


When incorporating real-patient data, these visualizations can be used to display select patient brain scan images according to a range of x-direction locations in the brain or a specified x-direction location. In addition, the user can manipulate the "random number" variable in the hover textbox to display a desired feature of their choice based on the patient data. Furthermore, deploying the visualizations on Dash aid in their efficiency.                                                         
Lastly, the original code I modified can be found at this link:
https://dash.plotly.com/dash-core-components/tooltip





# How To Run The Code

#### Setup #####
In order to run the different code files, first, a Docker Desktop account and image must be created and kept running in the background since all the code runs using Docker. For instance, your Docker Desktop screen should look something like this:


<img width="960" alt="docker_desktop_screen" src="https://github.com/ShivaniSuthar/BRAIN_TUMOR_VISUALIZATION_TOOLS/assets/122011763/2e885009-ed13-40c7-b33f-ebb4aa62db38">

Second, VSCode must be installed on your computer.

#### Launching the Visualizations ##### 
Then, there are 4 main files involved in running the code - "Dockerfile.demo", "Dockerfile.graphvis", "Dockerfile.slicer", and "run.sh". 
- "Dockerfile.demo" contains the docker script to run "Codefile.py".
- "Dockerfile.graphvis" contains the docker script to run "app.py".
- "Dockerfile.slicer" contains the docker script to run either "main.py", "main2.py", or "main3.py".
- "Run.sh" contains the bash script to build and run any of the docker files.
  
In order to actually launch the visualizations, follow the steps specified below:
- Open VSCode
- Load the code in this repository in your VSCode file explorer. It should look something like this:
   <img width="960" alt="file_explorer" src="https://github.com/ShivaniSuthar/BRAIN_TUMOR_VISUALIZATION_TOOLS/assets/122011763/b70b749e-be74-40f0-9eff-ed5e6f3e0194">
- Open a new bash terminal in VSCode. It should look something like this:
   <img width="757" alt="VSCode_bash_terminal" src="https://github.com/ShivaniSuthar/BRAIN_TUMOR_VISUALIZATION_TOOLS/assets/122011763/071f38e7-4aee-4b27-af44-c92b9469863b">

##### Launching "Demo" #####
If you want to run the "demo" visualization, continue to follow the steps below:
1) Type "bash run.sh" demo in your terminal. This should launch IPython. Your terminal should look something like this:
   <img width="599" alt="demo_terminal_step_1" src="https://github.com/ShivaniSuthar/BRAIN_TUMOR_VISUALIZATION_TOOLS/assets/122011763/7727acf7-122f-47ca-adb6-5dff71c4fe20">
2) Copy and paste the code in "Codefile.py" into your terminal and hit enter. Once it's done loading, your terminal should look something like this:

   
   <img width="675" alt="demo_final_terminal" src="https://github.com/ShivaniSuthar/BRAIN_TUMOR_VISUALIZATION_TOOLS/assets/122011763/f3b84a12-90a5-4036-ba83-8f734b1563c8">
3) In a browser, open the port number that was launched specified in your terminal. Then, the visualization should appear.

##### Launching "Graphvis" #####
If you want to run the "graphvis" visualization, continue to follow the steps below:
1) Type "bash run.sh graphvis" in your terminal and hit enter. Once it's done loading, it should look something like this:
   <img width="585" alt="graphvis_terminal" src="https://github.com/ShivaniSuthar/BRAIN_TUMOR_VISUALIZATION_TOOLS/assets/122011763/ac8d5863-f2e6-4d74-843d-6229fb0f991c">
2) In a browser, open the port number that was launched specified in your terminal. Then, the visualization should appear.

##### Launching "Slicer" #####
If you want to run the "slicer" visualization, continue to follow the steps below.
For slicer, you can either launch "main", "main2", or "main3". However, they all follow a similar procedure. Here, main3 is used as an example:
1) Change the "Dockerfile.slicer" file in the circled locations in the image below to specify whether you want to run "main", "main2", or "main3":
   
   <img width="290" alt="main3_ex" src="https://github.com/ShivaniSuthar/BRAIN_TUMOR_VISUALIZATION_TOOLS/assets/122011763/ddb0f9a5-8ffe-45d8-8268-5eb30aeeb8e8">
   
2) Type "bash run.sh slicer" in your terminal and hit enter. Once it's done loading, it should look something like this:
   <img width="566" alt="slicer_terminal" src="https://github.com/ShivaniSuthar/BRAIN_TUMOR_VISUALIZATION_TOOLS/assets/122011763/505549a4-d0b2-45e6-8306-448afa2a8135">
3) In a browser, open the port number that was launched specified in your terminal. Then, the visualization should appear.

##### Retrieving Data and Other Notes ##### 
- All required data for these visualizations are already included in this repository. Please refer to the "Applications and Code Organization" section above to see the specific location for the image data files. 
- The expected output for each of the visualizations are shown in the "Applications and Code Organization" section above.
- The port numbers for the different visualizations can also be updated by changing the port number in the visualization’s corresponding section in "run.sh" and its corresponding docker file.

##### Dependencies #####
All required dependencies are specified in the "Requirements.txt" file in this repository

# Contact

Shivani Suthar

UCSD, B.S. in Data Science and Cognitive Science w/ML (March 2024) 

ssuthar@ucsd.edu


   

