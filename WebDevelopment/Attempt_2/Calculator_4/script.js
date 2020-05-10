
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

    var time_24hr = myDate.getHours();
    var time_minutes = myDate.getMinutes();
    var time_seconds = myDate.getSeconds();

    // Determine Which Half Of The Day
    var am_pm;

    if (time_24hr >= 12) {am_pm = "PM";}
    else if (time_24hr < 12) {am_pm = "AM";}

    // ---------------  Grab Greeting Information   ---------------
    // Determine The Appropriate Greeting For The Day
    var greeting;

    if (time_24hr >= 0 && time_24hr <= 6) {greeting = "Early Morning Regards Everyone!";}
    else if (time_24hr >= 7 && time_24hr <= 11) {greeting = "Good Morning Everyone!";}
    else if (time_24hr >= 12 && time_24hr <= 16) {greeting = "Good Afternoon Everyone!";}
    else if (time_24hr >= 17 && time_24hr <= 20) {greeting = "Good Evening Everyone!";}
    else if (time_24hr >= 23) {greeting = "Good Night Everyone!";}


    // ---------------  Print Information To A Specific Tag   ---------------
    var greeting_str = greeting
    var date_str = months[month] + " " + day + " " + year
    var time_str = time_24hr + ":" + time_minutes + ":" + time_seconds + " " + am_pm


    document.getElementById("parsed_Greeting").innerHTML = greeting_str;
    document.getElementById("parsed_Date").innerHTML = date_str;
    document.getElementById("parsed_Time").innerHTML = time_str;


    // ---------------  Print Information To Console   ---------------
    // console.log(time_24hr, time_minutes, time_seconds, greeting)

}

// --------------------------------------------------------------------------------------------------------------------



// ---------------  Print Information To Console   ---------------
setInterval(UpdateClock, 100); // Measured In Milliseconds
