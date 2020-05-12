//
// Name:                                            Renacin Matadeen
// Date:                                               05/12/2020
// Title                                            Web-Design Basics
//
// ----------------------------------------------------------------------------------------------------------------------

// navigator["appCodeName"]
// navigator["appName"]
// navigator["appMinorVersion"]
// navigator["cpuClass"]
// navigator["platform"]
// navigator["plugins"]
// navigator["opsProfile"]
// navigator["userProfile"]
// navigator["systemLanguage"]
// navigator["userLanguage"]
// navigator["appVersion"]
// navigator["userAgent"]
// navigator["onLine"]
// navigator["cookieEnabled"]
// navigator["mimeTypes"]

// Create A Function To Store Everything
function display_computerstats() {

    const browser_width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
    const browser_height = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);

    var str_width = "Display Width: " + browser_width;
    var str_height = "Display Height: " + browser_height;

    document.getElementById("Display_Width").innerHTML = str_width;
    document.getElementById("Display_Height").innerHTML = str_height;

    console.log(navigator);

    var OSName="Unknown OS";
    if (navigator.appVersion.indexOf("Win")!=-1) OSName="Windows";
    if (navigator.appVersion.indexOf("Mac")!=-1) OSName="MacOS";
    if (navigator.appVersion.indexOf("X11")!=-1) OSName="UNIX";
    if (navigator.appVersion.indexOf("Linux")!=-1) OSName="Linux";

    console.log('Your OS: '+OSName);


}

// --------------------------------------------------------------------------------------------------------------------
display_computerstats()
