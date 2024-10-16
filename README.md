### Why?
---

I've very recently got into running coming from a powerlifting background, and while I've always remained active, I'm struggling to balance the gym and the increased cardio, and I feel that this is mostly due to my nutrition. While I'm able to track my calories in and out using myFitnessPal and a garmin watch respectively, the only change I'm able to measure properly is my weight in Kg. While this is useful, I have access to much more advanced and important metrics 

I want to be able to update my weight with more metrics in the gamrin app.

I'm only able to add weight in kg manually and I'm not able to add any of the other metrics that are available unless I want to buy their really expensive smart scale, which I really can't afford.

### My Setup
---

I currently have a off-brand smart scale that uses the "Fitdays" app, the scales connect to my phone over bluetooth, that collects lots of different data points, the ones im interested in are:

```json
{
    "weight": "my weight in kG",
    "body fat": "my body fat %",
    "fat mass": "the mass of fat in kg",
    "fat free body weight": "the other mass in kg",
    "muscle mass": "muscle mass in kg",
    "Bone mass": "mass of bones in kg",
    "water weight": "fluid weight in kg",
    "subcutaneous fat":"fat under the skin %",
    "visceral fat":"fat around your organs %"
}
```

These options can be added into garmin using an upload portal on their website, however they must be in the form of a binary file called a FIT file.

These are a huge pain to build and you *should* sign up properly through the garmin website for IDs and everything

I also run a server at home, hosting some services one of which is Home Assistant, which is a self hosted OS that allows you to connect a multitude of smart home aplliances all in one place, locally and without having to use the cloud. This will be useful later.

### The plan
---

##### Step 1 - PoC
I want to be able to generate FIT files from a single JSON object, this JSON object will contain all the information manually collected from the fitdays app

This file will then be manually uploaded into the garmin app

##### Step 2 - Portability
I will use the python package streamlit to create a web interface to generate the FIT file form user input, this will then either return a file to the user, or automatically upload the file to garmin, depending on the garmin API.

I use cloud flare tunnels along with a large docker stack to be able to access docker containers that run on my home server from anywhere, so I'll wrap this stremalit app inside a docker container and add it into my compose stack

##### Step 3 - Automation 
I want to use the MQTT IoT messaging protocol to feed the scales data into my Home Assistant instance.
I should be able to subscribe to the scales output and collect the dtaa using my HA instance, pass this through to a Postgres Container which then will trigger a python script to either uploaded the genrated FIT file via the API, or sue something like playwright or selenium to control the browser headlessly


### backup plan
---
I use the proxmox hypervisior to host a bunch of VMs on my servers, while they currently all run some flavour of linux, I could boot a windows VM and use the Garmin SDK to edit some base FIT files rather than build myown from scratch, but that is not as fun
