// Name:                                            Renacin Matadeen
// Date:                                               05/11/2020
// Title                                            Open CV Research
//
// ----------------------------------------------------------------------------------------------------------------------

// Create A Function To Store Everything
function JavascriptBasics() {

    // Creating a variable in Javascript | All variables must be instantiated before hand | Var type and val can change
    var x;
    var x = 3;
    var x = "Three" // Note that escape characters work in strings, just like python!

    // Javascript support arrays, just like in Python
    var list_of_months = ["September", "October", "November", "December"]

    // Javascript also supports dictionaries (called objects in JS)
    var data_dictionary = {"ID": [1, 2, 3, 4], "Hours Studied": [3, 5, 4, 6], "Grade Received": [80, 90, 70, 100]}

    // Javascript supports while, and for loops | Becareful Of fencepost issue
    var index;
    var index_upperlimit = 10;
    var text = "";

    for (index = 1; index < index_upperlimit; index++) {
        text += index + "<br>";
        // console.log(index);
    }

    // Javascript Supports Try and Except, in this case however it's called try and catch
    /*
    var numm = 5;
    try {fin_num = numm + nummber;}
    catch(err){console.log("An Error Was Detected")}
    */

    // Printing To The Console Log, and An Element
    /*
    console.log();
    document.getElementById("Data").innerHTML = text;
    */
}

function UserInput() {
    var user_val = document.getElementById('fname').value;
    var greeting = "Hello " + user_val;
    document.getElementById("parsed_greeting").innerHTML = greeting;
}






// --------------------------------------------------------------------------------------------------------------------
