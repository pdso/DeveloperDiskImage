This project archived. [Apple Developer Forums](https://developer.apple.com/forums/thread/730947?answerId=756651022#756651022), 

```
With iOS 17+, we are using a new device stack (CoreDevice) to communicate with devices. With this new device stack, there is one DDI per platform (as opposed to per OS release). This same device stack will be shared across all versions of Xcode on your system, and installing a newer version of Xcode will update CoreDevice and its DDIs (just like how CoreSimulator is updated, if you are familiar with that).

This effectively means that you now have a supported way of updating the device stack on your system to support newer target OS devices. With CoreDevice, you should be able to debug devices running future versions of iOS using Xcode 15. This *may* require first installing a newer Xcode in order to install newer CoreDevice and DDIs, so keep that in mind.

Of course, this also means there is a temporary hiccup in which the old unsupported path doesn't work, but the good news is that future-you will have a supported way of doing this which works out-of-the-box, no need to modify your Xcode.app.
```



# DeveloperDiskImage

iOS latest DeveloperDiskImage.Extract from latest Xcode.

# How to use

## Manual

Click on "Finder" in MAC OS  
Click on "Go to Folder"  
Paste this path over their (make sure that you have installed xcode with named : "Xcode.app") `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport`   
Paste your extracted directory to that place  
quite Xcode and restart it. you can run your projects successfully in your real device  

![DeveloperDiskImage](DeveloperDiskImage.png)