# sustainability_repo
<h1> HooHacks 2021 </h1>

**## Technical Description of Autonomous Wick Irrigation Community Garden System:##**
> Our system has three parts. A composting system, a rainwater reservoir irrigation system, and a plant growth system. Our composting system will take all carbon and nitrogen related inputs from the community in the form of food scraps, lawn clippings, etc. and process it with worms into worm casting and nutrient dense liquid (which is compost and "worm tea"). The compost will then be manualy transfered to the community garden boxes to be used as fertilizer
> 
**##Composting System##**
> We will be using vermicomposting systems for our community gardens as they are much more efficient than traditional aerobic composting systems. They take much less time which is vital for systems that will serve a hundred or more people, and the worms within the bins can self-multiply within a relatively short time frame. This is vital if more people use the worm bins as the community grows, as the worm population will naturally sustain itself and hover around its carrying capacity within the mini ecosystem. It could also help start up more more pop up community gardens in surrounding areas as they would already have a base population of worms to start with, essentially for free.
  itself when compared will consist of multiple horizontally oriented worm bins located next to 
Rudimentary Rain Reservoir System
 
##Rainwater Reservoir System##
> 

##Python File Description##
>This user interface will be implemented in Python through the PyCharm Integrated Developer Environment. The environment will utilize data collected from theoretical sensors placed in the wick irrigation system. The code consists of three main functions: a plant growth monitor, compost renewal alerter, and a water tank level monitor. All three functions will begin collecting data in real-time (hours, weeks, months, etc.), which is made possible by the "dateset" and "initializor" helper methods. These begin the timer and start all three functions at the same time. The plant growth monitor takes the photos of the community garden and sets up an array of photo objects so the user can monitor any growth or changes in the garden. The compost renewal system works on a weekly basis, and notifies the user to put in more food waste into the compost bin. Since the compost bin should spread the earthworms out, the notification also indicates which side the user should place the food waste so the earthworms drop compost into the garden evenly. Finally, the water tank level monitor will take the water levels from the float system and send the data to the user. Based off of the water levels, the user can manually open the overflow latch in the resovior.
