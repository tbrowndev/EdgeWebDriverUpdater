# EdgeWebDriverUpdater
 
I created this as a way to automatically update the microsoft edge web driver for Automation testing. 
If the Edge driver is not the same version as the edge browser, the automation test will not work in edge. 

Steps:
 - check browser and driver version
 - If they match, we are done
 - If mismatch, download version that matches browser version, replace the currect driver file with the updated file
 
 Drivers are downloaded from Microsoft Edge Web Driver site: https://msedgewebdriverstorage.z22.web.core.windows.net