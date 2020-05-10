


function displayDate(){
    var myDate = new Date(),

        date = myDate.getDate(),
        month = myDate.getMonth(),
        year = myDate.getFullYear();

    var months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "Novermber", "December"];

    const date_str = months[month] + " " + date + " " + year;

    document.getElementById("ShowDate").innerHTML = date_str;
}
