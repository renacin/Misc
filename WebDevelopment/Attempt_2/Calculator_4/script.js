
// Create A Function So I can Iterate It Every Couple Of Seconds
function UpdateClock() {


    // ---------------  Grab Date Information   ---------------
    // Basic Date Information
    var myDate = new Date(),
    day = myDate.getDate(),
    month = myDate.getMonth(),
    year = myDate.getFullYear();

    var months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "Novermber", "December"];

    var time_24hr;
    var time_24hr_r = myDate.getHours();
    if (time_24hr_r > 12) {time_24hr = time_24hr_r - 12}
    else {time_24hr = time_24hr_r}

    var time_minutes;
    var time_minutes_r = myDate.getMinutes();
    if (time_minutes_r < 10) {time_minutes = "0" + String(time_minutes_r);}
    else {time_minutes = time_minutes_r}

    var time_seconds;
    var time_seconds_r = myDate.getSeconds();
    if (time_seconds_r < 10) {time_seconds = "0" + String(time_seconds_r);}
    else {time_seconds = time_seconds_r}

    var am_pm;
    if (time_24hr_r >= 12) {am_pm = "PM";}
    else if (time_24hr_r < 12) {am_pm = "AM";}


    // ---------------  Grab Greeting Information   ---------------
    // Determine The Appropriate Greeting For The Day
    var greeting;
    if (time_24hr_r >= 0 && time_24hr_r <= 6) {greeting = "Early Morning Regards Everyone!";}
    else if (time_24hr_r >= 7 && time_24hr_r <= 11) {greeting = "Good Morning Everyone!";}
    else if (time_24hr_r >= 12 && time_24hr_r <= 16) {greeting = "Good Afternoon Everyone!";}
    else if (time_24hr_r >= 17 && time_24hr_r <= 20) {greeting = "Good Evening Everyone!";}
    else if (time_24hr_r >= 23) {greeting = "Good Night Everyone!";}


    // ---------------  Print Information To A Specific Tag   ---------------
    var greeting_str = greeting;
    var date_str = months[month] + " " + day + " " + year + ",";
    var time_str = time_24hr + ":" + time_minutes + ":" + time_seconds + " " + am_pm;


    document.getElementById("parsed_Greeting").innerHTML = greeting_str;
    document.getElementById("parsed_Date").innerHTML = date_str;
    document.getElementById("parsed_Time").innerHTML = time_str;


    // ---------------  Print Information To Console   ---------------
    // console.log(time_24hr, time_minutes, time_seconds, greeting)

}


// --------------------------------------------------------------------------------------------------------------------
setInterval(UpdateClock, 100); // Measured In Milliseconds
